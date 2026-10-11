---
title: Arithmetic Intensity
type: concept
status: seed
category: concepts
summary: Arithmetic intensity measures FLOPs per byte moved; the roofline threshold predicts whether a workload is limited by compute throughput or memory bandwidth.
tags:
  - llm
  - inference
  - systems
  - optimization
aliases:
  - operational intensity
  - compute-to-memory ratio
relationships:
  - target: "[[wiki/topics/LLM Inference Systems]]"
    type: related_to
  - target: "[[wiki/concepts/Prefill Decode Split]]"
    type: related_to
  - target: "[[wiki/concepts/Continuous Batching]]"
    type: related_to
  - target: "[[wiki/concepts/KV Cache]]"
    type: related_to
  - target: "[[wiki/sources/Principles of Mechanical Sympathy Source Guide]]"
    type: related_to
sources:
  - https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb
created: 2026-08-30T21:03:10+0800
updated: 2026-08-30T21:03:10+0800
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-08-30
tier: supporting
---

# Arithmetic Intensity

Arithmetic intensity describes how much arithmetic a workload performs for each byte it moves across a chosen memory boundary:

$$
I = \frac{\text{FLOPs}}{\text{bytes moved}}
$$

The boundary matters. A kernel can have different intensities with respect to GPU HBM, on-chip cache, or host-to-device traffic. In GPU inference, the usual first approximation counts bytes transferred from HBM to the compute units. High intensity means data is reused for many operations; low intensity means execution spends comparatively more time moving data.

## Roofline Threshold

The roofline model bounds attainable throughput by the smaller of peak arithmetic throughput and the throughput supported by memory bandwidth:

$$
P_{\text{attainable}} \leq \min\left(P_{\text{peak}},\; B_{\text{memory}} I\right)
$$

The two ceilings meet at the ridge point:

$$
I_{\text{ridge}} = \frac{P_{\text{peak}}}{B_{\text{memory}}}
$$

- If $I < I_{\text{ridge}}$, memory cannot deliver bytes fast enough to occupy all arithmetic units, so the workload is bandwidth-bound.
- If $I > I_{\text{ridge}}$, the workload has enough reuse to approach the compute ceiling and is compute-bound.

Using the source's rounded A100 figures, $312$ TFLOPS divided by $2$ TB/s gives a ridge point of about $156$ FLOPs/byte. This is the hardware balance that a kernel must exceed before peak compute, rather than HBM bandwidth, becomes the first-order ceiling.

## Why Single-Token Decode Is Bandwidth-Bound

During one-token decode, a transformer applies large weight matrices to only one new token per sequence. Consider an FP16 matrix with shape $4096 \times 14336$:

- It contains $58{,}720{,}256$ weights.
- At two bytes per FP16 weight, it occupies $117{,}440{,}512$ bytes, or about $112$ MiB.
- A matrix-vector multiplication performs roughly $2mn$, or $117.4$ million, FLOPs when one multiply-add is counted as two FLOPs.
- Ignoring activation and output traffic, that is only about $1$ FLOP per byte of weight data—far below the A100's approximate $156$ FLOPs/byte ridge point.

The source rounds the idealized transfer time for that matrix to about $56\,\mu s$ at $2$ TB/s, versus about $0.4\,\mu s$ of ideal arithmetic at $312$ TFLOPS: roughly a $140{:}1$ ratio. The arithmetic units can therefore finish their share much faster than HBM can supply a fresh pass over the weights. This is the core reason low-batch decode is usually memory-bandwidth-bound in [[wiki/topics/LLM Inference Systems]].

> [!warning] Theoretical estimate, not a measurement
> The A100 rates, the $56\,\mu s$ transfer time, the $0.4\,\mu s$ compute time, and the $140{:}1$ ratio are roofline-style theoretical estimates, not profiler measurements. Results depend on the exact A100 model, precision and sparsity mode, clocks, memory configuration, tensor shapes, kernel implementation, fusion, cache behavior, and achieved rather than advertised bandwidth. Binary-versus-decimal byte conventions also shift the rounded transfer time.

This contrast helps explain the [[wiki/concepts/Prefill Decode Split]]. Prefill processes many known prompt tokens together and turns large projections into matrix-matrix operations with substantial weight reuse. Decode has a serial dependency between generated tokens and, at batch size one, reduces those projections toward matrix-vector operations with little reuse.

## Why Batching Raises Reuse

Batching applies one weight load to several token vectors. In a simplified weight-dominated FP16 projection with batch size $b$:

$$
\text{FLOPs} \approx 2mnb, \qquad \text{weight bytes} \approx 2mn, \qquad I \approx b
$$

The weight traffic stays approximately fixed while useful arithmetic grows with the number of tokens sharing the operation. The kernel changes from a low-reuse matrix-vector multiply toward a matrix-matrix multiply that better occupies GPU tensor cores. This linear relation is only a first-order model: activation traffic, tiling, caches, quantization, padding, and [[wiki/concepts/KV Cache]] reads eventually prevent intensity from scaling exactly with batch size. ^[inferred]

[[wiki/concepts/Continuous Batching]] makes this reuse available under online traffic by assembling active decode tokens from different requests into each engine step. It can raise aggregate throughput even though every individual request still advances autoregressively one token at a time. The scheduler trades that gain against queueing delay, KV-cache capacity, and latency objectives. ^[inferred]

## GPU Memory Residency

Saying that model weights are "resident on the GPU" normally means they fit in GPU HBM and do not need to cross PCIe from host memory on every step. It does **not** mean every weight is already in a register or on-chip cache when a layer executes. Resident weights still have to travel through the GPU memory hierarchy to the arithmetic units, and a model-sized working set is too large for on-chip storage.

This separates two constraints:

- **capacity** asks whether weights plus [[wiki/concepts/KV Cache|KV-cache]] state fit in device memory;
- **bandwidth** asks how quickly the resident bytes can be streamed to the compute units for each forward pass.

If weights are offloaded, PCIe or interconnect traffic introduces another, usually lower, bandwidth roof. If weights remain in HBM, memory residency removes that transfer but does not remove the HBM bandwidth cost. KV cache saves the compute that would otherwise recreate past keys and values, yet decode must still read an expanding cache during attention, adding its own memory traffic. ^[inferred]

## Design Use

Arithmetic intensity turns [[wiki/sources/Principles of Mechanical Sympathy Source Guide|Principles of Mechanical Sympathy]] into a quantitative question: does a change reduce bytes moved, increase useful work per byte, or merely rearrange computation? It suggests several levers for inference systems—batching more tokens, reusing prefixes and KV state, quantizing weights, fusing kernels, and keeping data near the compute—but the right lever depends on the measured bottleneck. ^[inferred]

The roofline estimate is a diagnosis boundary, not a substitute for profiling. A production analysis should use the actual kernel's FLOP count, bytes at the relevant memory level, achieved bandwidth, occupancy, and latency, then account separately for launch overhead, communication, sampling, and scheduling.

## Related

- [[wiki/topics/LLM Inference Systems]]
- [[wiki/concepts/Prefill Decode Split]]
- [[wiki/concepts/Continuous Batching]]
- [[wiki/concepts/KV Cache]]
- [[wiki/sources/Principles of Mechanical Sympathy Source Guide|Principles of Mechanical Sympathy]]

## Sources

- [Arithmetic-intensity notes](https://kcnrpnk9jqxn.feishu.cn/wiki/LDSUwt1Gfi5uOmkhRXScfIExnBb)
