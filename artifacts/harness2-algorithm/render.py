"""Deterministic 1080p explainer animation of the Harness² algorithm.

Usage:
  python render.py --stills 5,30,60      # write check frames to frames-check/
  python render.py                       # render the full MP4 with the prepared audio
"""
import argparse
import functools
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SCRIPT = json.loads((ROOT / 'script.json').read_text())
TIMELINE = json.loads((ROOT / 'timeline.json').read_text())
W, H, FPS = SCRIPT['width'], SCRIPT['height'], SCRIPT['fps']
OUT = ROOT / 'harness2-algorithm-1080p.mp4'

BG = '#0B151B'; PANEL = '#13242B'; LINE = '#2A4A52'; WHITE = '#F3F4ED'; MUTED = '#8FA7A9'
MINT = '#B7F76D'; BLUE = '#73C7F5'; ORANGE = '#FFAD77'; RED = '#FF6B6B'; YELLOW = '#F5D76E'
FONT = '/System/Library/Fonts/STHeiti Medium.ttc'
FONT_LIGHT = '/System/Library/Fonts/STHeiti Light.ttc'
CX = 1190  # centre of the main canvas (x 520..1860, y 150..880)
G = {'fade': 1.0}


# ---------- drawing primitives ----------

@functools.lru_cache(maxsize=64)
def font(size, light=False):
    return ImageFont.truetype(FONT_LIGHT if light else FONT, size)


@functools.lru_cache(maxsize=256)
def rgb(c):
    c = c.lstrip('#')
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ap(t, t0, dur=0.5):
    """Appearance factor: 0 before t0, eases to 1 over dur."""
    return ease((t - t0) / dur)


def mix(c, a=1.0, bg=BG):
    a = clamp(a) * G['fade']
    f, b = rgb(c), rgb(bg)
    return tuple(int(b[i] + (f[i] - b[i]) * a) for i in range(3))


def lerp(a, b, p):
    return tuple(x + (y - x) * p for x, y in zip(a, b))


def text(d, xy, s, size=30, color=WHITE, anchor='lt', a=1.0, light=False):
    if a <= 0:
        return
    d.text(xy, s, font=font(size, light), fill=mix(color, a), anchor=anchor)


def wrap(d, s, size, width):
    out, cur = [], ''
    for ch in s:
        if d.textlength(cur + ch, font=font(size)) > width and cur:
            out.append(cur)
            cur = ch.lstrip()
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def para(d, xy, s, size, width, color=WHITE, a=1.0, spacing=10, anchor='lt'):
    x, y = xy
    rows = wrap(d, s, size, width)
    for i, row in enumerate(rows):
        text(d, (x, y + i * (size + spacing)), row, size, color, anchor, a)
    return len(rows) * (size + spacing)


def box(d, rect, a=1.0, fill=PANEL, outline=LINE, width=2, radius=14):
    if a <= 0:
        return
    d.rounded_rectangle(rect, radius=radius, fill=mix(fill, a), outline=mix(outline, a), width=width)


def arrow(d, p, q, color=MUTED, a=1.0, width=4, head=15, dashed=False):
    if a <= 0:
        return
    (ax, ay), (bx, by) = p, q
    n = math.hypot(bx - ax, by - ay)
    if n < 1:
        return
    ux, uy = (bx - ax) / n, (by - ay) / n
    col = mix(color, a)
    end = n - head
    if dashed:
        s = 0.0
        while s < end:
            e = min(s + 13, end)
            d.line((ax + ux * s, ay + uy * s, ax + ux * e, ay + uy * e), fill=col, width=width)
            s += 23
    else:
        d.line((ax, ay, ax + ux * end, ay + uy * end), fill=col, width=width)
    d.polygon([(bx, by), (bx - ux * head - uy * head * .55, by - uy * head + ux * head * .55),
               (bx - ux * head + uy * head * .55, by - uy * head - ux * head * .55)], fill=col)


def grow_arrow(d, p, q, prog, **kw):
    if prog <= 0:
        return
    arrow(d, p, lerp(p, q, prog), a=kw.pop('a', 1.0) * min(1, prog * 3), **kw)


def chip(d, xy, label, color=WHITE, bg='#1B3A35', size=24, a=1.0, anchor='m'):
    tw = d.textlength(label, font=font(size))
    x, y = xy
    if anchor == 'l':
        x += tw / 2 + 16
    box(d, (x - tw / 2 - 16, y - size / 2 - 10, x + tw / 2 + 16, y + size / 2 + 10), a, bg, bg, 1, 10)
    text(d, (x, y), label, size, color, 'mm', a)
    return tw + 32


def check(d, c, s=18, color=MINT, a=1.0):
    if a <= 0:
        return
    x, y = c
    d.line([(x - s * .55, y), (x - s * .15, y + s * .4), (x + s * .6, y - s * .45)],
           fill=mix(color, a), width=max(3, int(s / 4)), joint='curve')


def cross(d, c, s=16, color=RED, a=1.0):
    if a <= 0:
        return
    x, y = c
    w = max(3, int(s / 4))
    d.line((x - s * .45, y - s * .45, x + s * .45, y + s * .45), fill=mix(color, a), width=w)
    d.line((x - s * .45, y + s * .45, x + s * .45, y - s * .45), fill=mix(color, a), width=w)


def eye_off(d, c, s=22, a=1.0):
    x, y = c
    d.ellipse((x - s, y - s * .55, x + s, y + s * .55), outline=mix(MUTED, a), width=3)
    d.ellipse((x - s * .25, y - s * .25, x + s * .25, y + s * .25), fill=mix(MUTED, a))
    d.line((x - s * .9, y + s * .8, x + s * .9, y - s * .8), fill=mix(RED, a), width=4)


def lock(d, c, s=20, color=YELLOW, a=1.0):
    x, y = c
    d.arc((x - s * .6, y - s * 1.3, x + s * .6, y - s * .1), 180, 360, fill=mix(color, a), width=4)
    d.rounded_rectangle((x - s * .85, y - s * .6, x + s * .85, y + s * .7), radius=4, fill=mix(color, a))


def file_icon(d, xy, a=1.0, color=BLUE):
    x, y = xy
    d.polygon([(x, y), (x + 20, y), (x + 28, y + 8), (x + 28, y + 34), (x, y + 34)], outline=mix(color, a), width=2)


def progress_dot(d, c, r, color, a=1.0):
    x, y = c
    d.ellipse((x - r, y - r, x + r, y + r), fill=mix(color, a))


def banner(d, y, s, a=1.0, color=YELLOW, size=30):
    tw = d.textlength(s, font=font(size))
    box(d, (CX - tw / 2 - 34, y, CX + tw / 2 + 34, y + size + 34), a, '#2A2716', color, 2, 12)
    text(d, (CX, y + (size + 34) / 2), s, size, color, 'mm', a)


# ---------- scenes ----------

def s_intro(d, t, L, D):
    text(d, (CX, 220), '模型', 36, WHITE, 'mm', ap(t, 0.2))
    box(d, (CX - 170, 180, CX + 170, 262), ap(t, 0.2), PANEL, BLUE)
    text(d, (CX, 221), '同一个模型', 34, WHITE, 'mm', ap(t, 0.2))
    for i, (x, label, score, color) in enumerate([(880, 'Harness A', .42, ORANGE), (1500, 'Harness B', .86, MINT)]):
        a = ap(t, 1.0 + i * .7)
        grow_arrow(d, (CX, 262), (x, 380), ap(t, .6 + i * .7, .6), color=MUTED, a=a)
        box(d, (x - 210, 385, x + 210, 545), a)
        text(d, (x, 425), label, 32, color, 'mm', a)
        d.rounded_rectangle((x - 170, 475, x + 170, 503), radius=8, fill=mix(LINE, a))
        prog = ease((t - 1.6 - i * .7) / 1.4) * score
        if prog > 0:
            d.rounded_rectangle((x - 170, 475, x - 170 + 340 * prog, 503), radius=8, fill=mix(color, a))
        text(d, (x, 525), '表现', 22, MUTED, 'mm', a)
    a = ap(t, L[1])
    box(d, (CX - 360, 620, CX + 360, 830), a, '#1A1F2B', BLUE)
    text(d, (CX, 662), '没有标准答案的新任务', 34, WHITE, 'mm', a)
    for i, (k, v) in enumerate([('标准答案', '？'), ('评分标准', '不可见'), ('怎么办', '边做边改 harness')]):
        aa = ap(t, L[1] + .6 + i * .6)
        text(d, (CX - 260, 718 + i * 38), k, 26, MUTED, 'lm', aa)
        text(d, (CX + 260, 718 + i * 38), v, 26, MINT if i == 2 else ORANGE, 'rm', aa)


def s_harness(d, t, L, D):
    c = (CX, 500)
    parts = ['全局指令', '领域手册', '长期记忆', '技能与脚本', '工具设置', '子代理分派', '检查钩子']
    ring_a = ap(t, L[1])
    if ring_a > 0:
        d.ellipse((c[0] - 470, c[1] - 300, c[0] + 470, c[1] + 300), outline=mix(MINT, ring_a * .8), width=3)
        chip(d, (CX, 175), 'harness：被修改的对象', MINT, '#1E3A22', 28, ring_a)
    for i, p in enumerate(parts):
        ang = -math.pi / 2 + i * 2 * math.pi / len(parts)
        pos = (c[0] + 400 * math.cos(ang), c[1] + 250 * math.sin(ang))
        a = ap(t, 0.8 + i * (max(1.0, L[1] - 1.5) / len(parts)))
        d.line((c, pos), fill=mix(LINE, a), width=2)
        chip(d, pos, p, MINT if ring_a > .5 else WHITE, '#1B3A35', 27, a)
    d.ellipse((c[0] - 105, c[1] - 105, c[0] + 105, c[1] + 105), fill=mix(PANEL), outline=mix(BLUE), width=4)
    text(d, (c[0], c[1] - 14), '模型', 38, WHITE, 'mm')
    la = ap(t, L[1] + .8)
    if la > 0:
        lock(d, (c[0] - 52, c[1] + 40), 14, YELLOW, la)
        text(d, (c[0] + 12, c[1] + 38), '参数不变', 24, YELLOW, 'mm', la)


TRACE_ROWS = ['读取 拍摄日程.xlsx', '读取 预算表.xlsx', '生成 交付清单.xlsx', '写入 备忘录.docx', '结束任务']


def s_reference(d, t, L, D):
    a = ap(t, .2)
    box(d, (545, 250, 880, 770), a)
    text(d, (712, 290), '任务：制片交付物', 28, WHITE, 'mm', a)
    for i, f in enumerate(['拍摄日程.xlsx', '人员名单.xlsx', '场地信息.pdf', '预算表.xlsx']):
        aa = ap(t, .6 + i * .5)
        file_icon(d, (580, 340 + i * 70), aa)
        text(d, (625, 357 + i * 70), f, 26, WHITE, 'lm', aa)
    text(d, (580, 650), '要求：互相衔接的交付物', 23, MUTED, 'lt', ap(t, 2.8))
    text(d, (580, 684), '其中包括一份备忘录', 23, MUTED, 'lt', ap(t, 2.8))
    ha = ap(t, L[1])
    grow_arrow(d, (885, 490), (935, 490), ap(t, L[1], .5), color=MUTED)
    box(d, (940, 425, 1150, 555), ha, PANEL, BLUE)
    text(d, (1045, 470), '原始', 26, MUTED, 'mm', ha)
    text(d, (1045, 508), 'harness', 30, WHITE, 'mm', ha)
    grow_arrow(d, (1155, 490), (1205, 490), ap(t, L[1] + .4, .5), color=MUTED)
    ta = ap(t, L[1] + .5)
    box(d, (1210, 230, 1845, 820), ta)
    text(d, (1240, 262), '参考轨迹', 28, BLUE, 'lm', ta)
    span = max(1.0, L[2] - L[1] - 1.2)
    for i, row in enumerate(TRACE_ROWS):
        ra = ap(t, L[1] + 1 + i * span / len(TRACE_ROWS), .35)
        y = 320 + i * 72
        progress_dot(d, (1250, y), 7, BLUE, ra)
        if i < len(TRACE_ROWS) - 1:
            d.line((1250, y + 10, 1250, y + 62), fill=mix(LINE, ra), width=2)
        text(d, (1275, y), f'{i + 1}  {row}', 26, WHITE, 'lm', ra)
    flags = [(392, '未跨文件核对数字'), (608, '写完没有重新打开复查'), (536, '备忘录缺少应有部分')]
    for i, (y, s) in enumerate(flags):
        fa = ap(t, L[2] + .3 + i * 1.6)
        if fa > 0:
            chip(d, (1820 - d.textlength(s, font=font(23)) / 2 - 16, y), s, RED, '#3A1D22', 23, fa)
    banner(d, 838, '参考轨迹只说明“怎么做”，不判定“对不对”', ap(t, L[3]), YELLOW, 27)


def s_propose(d, t, L, D):
    a = ap(t, .1)
    box(d, (CX - 230, 175, CX + 230, 255), a, PANEL, BLUE)
    text(d, (CX, 215), '原始 harness + 参考轨迹', 28, WHITE, 'mm', a)
    eds = [(870, '通用编辑者', '规划 · 工具 · 信息管理 · 委派 · 复查', MINT),
           (1510, '领域编辑者', '行业知识 · 流程 · 约束 · 数据格式', ORANGE)]
    for i, (x, name, sub, col) in enumerate(eds):
        ea = ap(t, .5 + i * .5)
        grow_arrow(d, (CX + (i * 2 - 1) * 120, 258), (x, 318), ap(t, .4 + i * .5, .5), color=MUTED)
        box(d, (x - 260, 322, x + 260, 432), ea, PANEL, col)
        text(d, (x, 357), name, 30, col, 'mm', ea)
        text(d, (x, 400), sub, 22, MUTED, 'mm', ea)
    cards = [
        (L[1], 590, '候选 A', MINT, ['+ 守则：动手前清点全部输入，每个数字追到出处',
                                    '+ 脚本：结束前重新打开每份产出复查',
                                    '理由：“文件存在，不等于文件正确”']),
        (L[2], 1230, '候选 B', ORANGE, ['+ 手册：核对日程、场地、人工与预算',
                                       '+ 工具提示：“$50”“1,200”存的是文字，先去掉符号和逗号再计算'])]
    for i, (t0, x0, title, col, rows) in enumerate(cards):
        ca = ap(t, t0)
        cx = x0 + 280
        grow_arrow(d, (cx, 436), (cx, 488), ap(t, t0, .4), color=col)
        box(d, (x0, 492, x0 + 560, 840), ca, '#14281F' if i == 0 else '#2A2016', col)
        text(d, (x0 + 28, 528), title, 30, col, 'lm', ca)
        y = 572
        for j, r in enumerate(rows):
            ra = ap(t, t0 + .6 + j * 1.3)
            y += para(d, (x0 + 28, y), r, 24, 505, MUTED if r.startswith('理由') else WHITE, ra, 8) + 14


def lane_marks(d, x, y, kind, a):
    if kind == 'ok':
        check(d, (x, y), 22, MINT, a)
    elif kind == 'bad':
        cross(d, (x, y), 18, RED, a)
    else:
        text(d, (x, y), '—', 26, MUTED, 'mm', a)


def s_probe(d, t, L, D):
    a = ap(t, .1)
    for i, s in enumerate(['同一任务', '同一模型', '同一环境']):
        chip(d, (CX - 260 + i * 260, 185), s, BLUE, '#16303D', 27, ap(t, .1 + i * .3))
    lanes = [('参考：原始 harness', BLUE, ['读取', '读取', '生成', '写入', '结束'], [0, 0, 0, 0, 0]),
             ('候选 A', MINT, ['清点输入', '交叉核对', '生成', '写入', '脚本复查'], [1, 1, 0, 0, 1]),
             ('候选 B', ORANGE, ['读取', '按手册核对', '解析金额', '写入', '结束'], [0, 1, 1, 0, 0])]
    x0, x1 = 830, 1820
    for i, (name, col, steps, new) in enumerate(lanes):
        y = 285 + i * 105
        la = ap(t, .4 + i * .3)
        text(d, (560, y), name, 27, col, 'lm', la)
        d.line((x0, y, x1, y), fill=mix(LINE, la), width=4)
        prog = ease((t - .8 - i * .25) / max(1.0, L[1] - 1.2))
        for j, s in enumerate(steps):
            px = x0 + 40 + j * (x1 - x0 - 80) / (len(steps) - 1)
            reached = prog * (len(steps) - 1) + 1e-6 >= j
            sa = la * (1 if reached else .25)
            progress_dot(d, (px, y), 10 if new[j] else 8, (MINT if i == 1 else ORANGE) if new[j] else MUTED, sa)
            text(d, (px, y + 32), s, 22, WHITE if new[j] else MUTED, 'mm', sa)
        hx = x0 + 40 + prog * (x1 - x0 - 80)
        if 0 < prog < 1:
            progress_dot(d, (hx, y), 14, col, la)
    ta = ap(t, L[1])
    box(d, (560, 600, 1820, 785), ta)
    text(d, (590, 630), '与参考轨迹并排比较', 26, BLUE, 'lm', ta)
    chip(d, (1760, 630), '示意', MUTED, '#1E2C31', 20, ta)
    headers = ['原问题：跨文件核对', '原问题：产出复查', '新问题']
    for k, h in enumerate(headers):
        text(d, (1040 + k * 280, 670), h, 22, MUTED, 'mm', ta)
    rows = [('候选 A', MINT, ['ok', 'ok', 'none']), ('候选 B', ORANGE, ['ok', 'none', 'none'])]
    for r, (name, col, marks) in enumerate(rows):
        ra = ap(t, L[1] + .8 + r * .9)
        yy = 715 + r * 45
        text(d, (600, yy), name, 25, col, 'lm', ra)
        for k, m in enumerate(marks):
            if k == 2:
                text(d, (1040 + k * 280, yy), '未发现', 23, MUTED, 'mm', ra)
            else:
                lane_marks(d, 1040 + k * 280, yy, m, ra)
    banner(d, 805, '比较的是行为变化，不是答案对错', ap(t, L[2]), YELLOW, 27)


EDITS = [('A', '守则：清点输入并追溯数字', '证据：试跑中出现交叉核对'),
         ('A', '脚本：结束前复查产出', '证据：试跑中重新打开了文件'),
         ('B', '手册：日程/场地/人工/预算核对', '证据：试跑按手册逐项核对'),
         ('B', '提示：金额先去符号和逗号', '证据：金额按数字参与计算')]


def s_compose(d, t, L, D):
    comp = (1250, 430)
    target = (1490, 330)
    ca = ap(t, .3)
    box(d, (comp[0] - 95, comp[1] - 55, comp[0] + 95, comp[1] + 55), ca, PANEL, BLUE)
    text(d, (comp[0], comp[1]), '组合者', 30, BLUE, 'mm', ca)
    na = ap(t, .5)
    chip(d, (1010, 190), '证据为示意', MUTED, '#1E2C31', 18, ap(t, .4))
    box(d, (1400, 230, 1845, 600), na, '#14281F', MINT)
    text(d, (1430, 265), '新 harness', 30, MINT, 'lm', na)
    for i, (src, edit, ev) in enumerate(EDITS):
        y = 260 + i * 105
        col = MINT if src == 'A' else ORANGE
        a0 = ap(t, .2 + i * .35)
        start = L[1] + .3 + i * .9
        p = clamp((t - start) / 1.2)
        ghost = 1 - .6 * ease(p)
        box(d, (545, y - 34, 1080, y + 46), a0 * ghost, PANEL, col)
        text(d, (570, y - 10), f'{src} · {edit}', 24, WHITE, 'lm', a0 * ghost)
        text(d, (570, y + 22), ev, 20, MUTED, 'lm', a0 * ghost)
        if 0 < p < 1:
            if p < .5:
                pos = lerp((1080, y), comp, ease(p * 2))
            else:
                pos = lerp(comp, (target[0] + 60, target[1] + i * 60), ease(p * 2 - 1))
            progress_dot(d, pos, 12, col)
        if p >= 1:
            ia = ap(t, start + 1.2, .3)
            check(d, (1438, 330 + i * 60), 16, MINT, ia)
            text(d, (1462, 330 + i * 60), edit, 23, WHITE, 'lm', ia)
    xa = ap(t, L[1] + 4.2)
    if xa > 0:
        y = 700
        fade_out = 1 - .55 * ap(t, L[1] + 5.4)
        box(d, (545, y - 34, 1080, y + 34), xa * fade_out, PANEL, LINE)
        text(d, (570, y), '某处没有试跑证据的修改', 24, MUTED, 'lm', xa * fade_out)
        chip(d, (1010, y), '示意', MUTED, '#1E2C31', 18, xa * fade_out)
        cross(d, (1120, y), 22, RED, ap(t, L[1] + 5.0))
        text(d, (1150, y), '舍弃', 26, RED, 'lm', ap(t, L[1] + 5.0))
    ra = ap(t, L[2] + .8)
    grow_arrow(d, (1622, 604), (1622, 650), ap(t, L[2] + .3, .5), color=MINT)
    box(d, (1400, 655, 1845, 830), ra)
    text(d, (1430, 690), '新 harness 运行结果', 26, MINT, 'lm', ra)
    for i, s in enumerate(['跨文件数字已核对', '备忘录缺少的部分已补齐']):
        aa = ap(t, L[2] + 1.8 + i * 1.2)
        check(d, (1440, 740 + i * 46), 16, MINT, aa)
        text(d, (1465, 740 + i * 46), s, 24, WHITE, 'lm', aa)


def bar(d, x, y, w, h, value, color, a, label, vmax=100):
    d.rounded_rectangle((x, y, x + w, y + h), radius=8, fill=mix(LINE, a))
    if value > 0:
        d.rounded_rectangle((x, y, x + max(h, w * value / vmax), y + h), radius=8, fill=mix(color, a))
    text(d, (x, y - 22), label, 23, MUTED, 'lm', a)
    text(d, (x + w * value / vmax + 14, y + h / 2), f'{value:.1f}', 26, color, 'lm', a)


def s_score(d, t, L, D):
    a = ap(t, .2)
    box(d, (545, 200, 1110, 820), a)
    text(d, (827, 240), '改进过程中', 30, WHITE, 'mm', a)
    for i, r in enumerate(['编辑者', '组合者', '挑选者']):
        ra = ap(t, .6 + i * .5)
        y = 330 + i * 110
        box(d, (600, y - 40, 1055, y + 40), ra, '#182C33', LINE)
        text(d, (640, y), r, 28, WHITE, 'lm', ra)
        eye_off(d, (850, y), 20, ra)
        text(d, (890, y), '看不到分数', 24, MUTED, 'lm', ra)
    la = ap(t, 2.4)
    lock(d, (650, 715), 18, YELLOW, la)
    text(d, (690, 712), '评分标准与分数被隔离', 26, YELLOW, 'lm', la)
    ra = ap(t, L[1])
    box(d, (1170, 200, 1845, 820), ra)
    text(d, (1200, 240), '事后评分（论文实验）', 28, BLUE, 'lm', ra)
    v0 = 43.1
    v1 = 43.1 + (77.8 - 43.1) * ease((t - L[1] - 1.5) / 1.8)
    bar(d, 1200, 320, 480, 30, v0, MUTED, ra, '制片任务 · 改进前')
    bar(d, 1200, 410, 480, 30, v1, MINT, ap(t, L[1] + .8), '制片任务 · 改进后')
    ga = ap(t, L[2])
    text(d, (1200, 510), 'WorkBuddy-Bench 平均分', 24, BLUE, 'lm', ga)
    grow = ease((t - L[2] - .6) / 1.6)
    bar(d, 1200, 580, 480, 26, 64.2, MUTED, ga, 'GLM-5 · 原 harness')
    bar(d, 1200, 660, 480, 26, 64.2 + (75.7 - 64.2) * grow, MINT, ap(t, L[2] + .4), 'GLM-5 · 改进后')
    bar(d, 1200, 740, 480, 26, 72.4, BLUE, ap(t, L[2] + 2.4), '更强的 Gemini · 原 harness')


def s_budget(d, t, L, D):
    pa = ap(t, .1)
    box(d, (545, 190, 1175, 610), pa)
    text(d, (575, 222), '并行：一轮写出 k 组候选', 26, MINT, 'lm', pa)
    h = (620, 420)
    box(d, (h[0] - 50, h[1] - 32, h[0] + 50, h[1] + 32), pa, PANEL, BLUE)
    text(d, h, 'H', 28, WHITE, 'mm', pa)
    for i in range(3):
        y = 300 + i * 120
        a = ap(t, .6 + i * .35)
        grow_arrow(d, (h[0] + 52, h[1]), (760, y), ap(t, .5 + i * .35, .5), color=MUTED)
        chip(d, (830, y), f'候选对 {i + 1}', WHITE, '#1B3A35', 22, a)
        grow_arrow(d, (905, y), (950, y), ap(t, 1.0 + i * .35, .4), color=MUTED)
        chip(d, (1000, y), '组合', BLUE, '#16303D', 22, a)
        grow_arrow(d, (1040, y), (1075, y), ap(t, 1.3 + i * .35, .4), color=MUTED)
        chip(d, (1120, y), f'结果{i + 1}', MINT, '#1E3A22', 22, a)
    sa = ap(t, 2.2)
    box(d, (1215, 190, 1845, 610), sa)
    text(d, (1245, 222), '顺序：连续修改 k 轮', 26, ORANGE, 'lm', sa)
    xs = [1290, 1430, 1570, 1710]
    for i, x in enumerate(xs):
        a = ap(t, 2.5 + i * .5)
        box(d, (x - 50, 300, x + 50, 360), a, PANEL, BLUE if i == 0 else ORANGE)
        text(d, (x, 330), 'H' if i == 0 else f'第{i}轮', 24, WHITE, 'mm', a)
        if i:
            grow_arrow(d, (xs[i - 1] + 52, 330), (x - 52, 330), ap(t, 2.4 + i * .5, .4), color=MUTED)
            grow_arrow(d, (x, 362), (x, 450), ap(t, 2.7 + i * .5, .4), color=MUTED)
            chip(d, (x, 485), f'结果{i}', MINT, '#1E3A22', 22, a)
    sel = (CX, 725)
    ka = ap(t, L[1])
    for x in (900, 1010, 1120, 1430, 1570, 1710):
        grow_arrow(d, (x, 614), (sel[0] + (x - CX) * .15, sel[1] - 52), ap(t, L[1] + .3, .8),
                   color=MINT, a=.6, width=3, dashed=True)
    box(d, (sel[0] - 190, sel[1] - 48, sel[0] + 190, sel[1] + 48), ka, '#16303D', BLUE)
    eye_off(d, (sel[0] - 135, sel[1] - 8), 16, ka)
    text(d, (sel[0] + 20, sel[1] - 12), '挑选者：盲选一份', 28, WHITE, 'mm', ka)
    text(d, (sel[0] + 20, sel[1] + 24), '只对照任务要求与原始材料', 20, MUTED, 'mm', ka)
    ba = ap(t, L[2])
    left = 1 - ease((t - L[2] - .8) / 3.0)
    box(d, (1440, 680, 1845, 790), ba)
    text(d, (1470, 708), '计算预算', 24, MUTED, 'lm', ba)
    d.rounded_rectangle((1470, 735, 1815, 760), radius=8, fill=mix(LINE, ba))
    if left > 0:
        d.rounded_rectangle((1470, 735, 1470 + max(20, 345 * left), 760), radius=8,
                            fill=mix(MINT if left > .3 else ORANGE, ba))
    stop = ap(t, L[2] + 3.9)
    text(d, (1815, 708), '用完 → 停止', 24, ORANGE, 'rm', stop)
    chip(d, (800, 735), '停止 ≠ 已证明正确', YELLOW, '#2A2716', 25, stop)


def s_library(d, t, L, D):
    a = ap(t, .1)
    box(d, (545, 200, 870, 580), a)
    text(d, (575, 235), '改进记录', 28, BLUE, 'lm', a)
    for i, s in enumerate(['参考轨迹', '候选差异', '试跑轨迹', '组合决定']):
        aa = ap(t, .4 + i * .4)
        file_icon(d, (575, 290 + i * 70), aa)
        text(d, (620, 307 + i * 70), s, 25, WHITE, 'lm', aa)
    grow_arrow(d, (874, 390), (925, 390), ap(t, 1.8, .4), color=MUTED)
    ra = ap(t, 2.0)
    box(d, (930, 320, 1140, 460), ra, PANEL, YELLOW)
    text(d, (1035, 362), '反思者', 30, YELLOW, 'mm', ra)
    para(d, (1035, 400), '只留有试跑证据的经验', 20, 170, MUTED, ra, 6, 'mt')
    grow_arrow(d, (1144, 390), (1195, 390), ap(t, 2.6, .4), color=MUTED)
    ca = ap(t, 2.8)
    box(d, (1200, 190, 1845, 590), ca, '#14281F', MINT)
    text(d, (1230, 225), '经验库', 30, MINT, 'lm', ca)
    cards = ['采用的完整 harness', '可运行脚本：复查产出', '适用情形：多份表格需交叉核对', '支持证据：试跑对比记录']
    for i, s in enumerate(cards):
        aa = ap(t, L[1] + .3 + i * 1.0)
        box(d, (1230, 270 + i * 76, 1815, 330 + i * 76), aa, '#1A3324', LINE, 2, 10)
        text(d, (1255, 300 + i * 76), s, 24, WHITE, 'lm', aa)
    na = ap(t, L[2])
    text(d, (560, 660), '下一项任务', 26, ORANGE, 'lm', na)
    steps = [(720, '原始 harness'), (1010, '提出'), (1250, '试跑'), (1490, '组合'), (1730, '交付')]
    for i, (x, s) in enumerate(steps):
        aa = ap(t, L[2] + .3 + i * .35)
        box(d, (x - 105, 720, x + 105, 790), aa, PANEL, BLUE if i == 0 else LINE)
        text(d, (x, 755), s, 25, WHITE, 'mm', aa)
        if i:
            grow_arrow(d, (steps[i - 1][0] + 107, 755), (x - 107, 755), ap(t, L[2] + .2 + i * .35, .3), color=MUTED)
    text(d, (720, 812), '起点不变', 20, BLUE, 'mt', ap(t, L[2] + .6))
    qa = ap(t, L[2] + 2.4)
    for x in (1010, 1490):
        arrow(d, (x + (1520 - x) * .25, 594), (x, 716), MINT, qa, 3, 14, True)
    text(d, (1250, 650), '查阅', 24, MINT, 'mm', qa)
    xa = ap(t, L[2] + 3.6)
    arrow(d, (1300, 594), (760, 716), MUTED, xa * .6, 3, 14, True)
    cross(d, (1030, 655), 22, RED, xa)
    text(d, (880, 640), '不直接继承', 22, RED, 'mm', xa)


def s_boundary(d, t, L, D):
    big = ap(t, .2) * (1 - ap(t, L[1] - .3, .4))
    text(d, (CX, 480), '行为变化  ≠  结果正确', 64, YELLOW, 'mm', big)
    scores = [95, 85, 85, 80, 55]
    pick = L[1] + 3.0
    reveal = L[1] + 5.0
    for i, sc in enumerate(scores):
        x = 640 + i * 275
        a = ap(t, L[1] + i * .25)
        chosen = i == 4 and t >= pick
        outline = RED if chosen and t >= reveal else (BLUE if chosen else LINE)
        box(d, (x - 115, 220, x + 115, 420), a, PANEL, outline, 4 if chosen else 2)
        text(d, (x, 260), f'结果 {i + 1}', 26, WHITE, 'mm', a)
        ra = ap(t, reveal + i * .15, .4)
        text(d, (x, 345), '？', 44, MUTED, 'mm', a * (1 - ra))
        text(d, (x, 345), str(sc), 52, RED if i == 4 else MINT, 'mm', a * ra)
    pa = ap(t, pick, .3)
    if pa > 0:
        chip(d, (640 + 4 * 275, 455), '被挑中：“最完整、最朴素”', BLUE, '#16303D', 21, pa)
    fa = ap(t, reveal + 1.0)
    text(d, (CX, 520), '实际：代码渲染出空列表，9 个测试没有通过', 28, RED, 'mm', fa)
    sa = ap(t, L[2])
    box(d, (545, 590, 1845, 830), sa)
    text(d, (575, 622), '共同盲点', 26, ORANGE, 'lm', sa)
    for i in range(3):
        x = 760 + i * 430
        aa = ap(t, L[2] + .5 + i * .4)
        box(d, (x - 165, 660, x + 165, 760), aa, '#182C33', LINE)
        text(d, (x, 690), f'候选 {"ABC"[i]}', 24, WHITE, 'mm', aa)
        chip(d, (x, 732), '假设：缓存规则（未核实）', RED, '#3A1D22', 19, aa)
        if i:
            arrow(d, (x - 430 + 170, 710), (x - 170, 710), MUTED, ap(t, L[2] + 2.0), 3, 12, True)
    text(d, (CX, 800), '大家犯同样的错 → 对比没有差异 → 错误照不出来', 24, MUTED, 'mm', ap(t, L[2] + 2.6))


def s_summary(d, t, L, D):
    oc, rx, ry = (CX, 475), 640, 300
    oa = ap(t, 1.2)
    d.ellipse((oc[0] - rx, oc[1] - ry, oc[0] + rx, oc[1] + ry), outline=mix(ORANGE, oa * .7), width=3)
    ic, r = (1000, 475), 205
    ia = ap(t, .2)
    d.ellipse((ic[0] - r, ic[1] - r, ic[0] + r, ic[1] + r), outline=mix(MINT, ia), width=4)
    nodes = ['参考运行', '提出', '试跑', '组合', '选择']
    for i, s in enumerate(nodes):
        ang = -math.pi / 2 + i * 2 * math.pi / len(nodes)
        chip(d, (ic[0] + r * math.cos(ang), ic[1] + r * math.sin(ang)), s, WHITE, '#1B3A35', 24, ap(t, .3 + i * .2))
    text(d, ic, '任务内', 30, MINT, 'mm', ia)
    text(d, (ic[0], ic[1] + 40), '同条件试跑筛选修改', 20, MUTED, 'mm', ia)
    ang = -math.pi / 2 + t * 1.1
    progress_dot(d, (ic[0] + r * math.cos(ang), ic[1] + r * math.sin(ang)), 9, MINT, ia)
    chip(d, (oc[0] + rx * .707, oc[1] + ry * .707), '沉淀经验 → 经验库', ORANGE, '#2A2016', 25, oa)
    chip(d, (oc[0] + 260, oc[1] - ry), '下一项任务', ORANGE, '#2A2016', 25, oa)
    text(d, (1540, 400), '任务间', 30, ORANGE, 'mm', oa)
    text(d, (1540, 440), '有证据的经验交给下一项任务', 20, MUTED, 'mm', oa)
    oang = t * .45
    progress_dot(d, (oc[0] + rx * math.cos(oang), oc[1] + ry * math.sin(oang)), 9, ORANGE, oa)
    for i, s in enumerate(['试跑决定留下什么', '预算决定何时停止', '正确性仍需独立验证']):
        chip(d, (CX - 420 + i * 420, 838), s, YELLOW if i == 2 else WHITE, '#2A2716' if i == 2 else '#1B3A35',
             25, ap(t, L[1] + .3 + i * .6))


SCENES = {'intro': s_intro, 'harness': s_harness, 'reference': s_reference, 'propose': s_propose,
          'probe': s_probe, 'compose': s_compose, 'score': s_score, 'budget': s_budget,
          'library': s_library, 'boundary': s_boundary, 'summary': s_summary}


# ---------- chrome ----------

def rail(d, stage, all_on):
    G['fade'] = 1.0
    text(d, (60, 62), 'Harness²', 46, WHITE, 'lm')
    text(d, (60, 108), '算法执行过程', 28, MUTED, 'lm')
    stages = SCRIPT['stages']
    text(d, (78, 172), '任务内循环', 22, MINT, 'lm')
    text(d, (78, 686), '任务间递归', 22, ORANGE, 'lm')
    for i, s in enumerate(stages):
        y = 205 + i * 92 if i < 5 else 715
        on = all_on or stage == i
        done = stage is not None and i < stage
        col = (MINT if i < 5 else ORANGE) if on else (WHITE if done else MUTED)
        fill = '#1E3A22' if on and i < 5 else ('#2A2016' if on else PANEL)
        d.rounded_rectangle((70, y, 450, y + 70), radius=14, fill=mix(fill),
                            outline=mix(col if on else LINE), width=3 if on else 2)
        text(d, (104, y + 35), f'{i}', 26, col, 'mm')
        text(d, (140, y + 35), s, 28, col, 'lm')
        if done:
            check(d, (415, y + 35), 16, MINT, .8)
    d.line((490, 150, 490, 880), fill=mix(LINE), width=2)


def find(t):
    for i, sc in enumerate(TIMELINE['scenes']):
        if t < sc['start'] + sc['duration'] or i == len(TIMELINE['scenes']) - 1:
            return i, sc
    raise ValueError(t)


def frame(t):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    idx, sc = find(t)
    meta = SCRIPT['scenes'][idx]
    local = t - sc['start']
    rail(d, meta['stage'], meta['id'] == 'summary')
    text(d, (540, 80), meta['title'], 40, WHITE, 'lm')
    text(d, (1860, 80), f'{idx + 1:02d} / {len(SCRIPT["scenes"])}', 24, MUTED, 'rm')
    G['fade'] = ease(local / .45) * (1 - ease((local - sc['duration'] + .35) / .35))
    SCENES[meta['id']](d, local, [ln['start'] for ln in sc['lines']], sc['duration'])
    G['fade'] = 1.0
    cue = next((ln for ln in sc['lines'] if ln['start'] - .05 <= local <= ln['end'] + .25), None)
    if cue:
        rows = wrap(d, cue['text'], 34, 1640)
        y = 975 - (len(rows) - 1) * 23
        for k, row in enumerate(rows):
            tw = d.textlength(row, font=font(34))
            d.rounded_rectangle((960 - tw / 2 - 18, y + k * 46 - 24, 960 + tw / 2 + 18, y + k * 46 + 24),
                                radius=8, fill=rgb('#060C10'))
            text(d, (960, y + k * 46), row, 34, WHITE, 'mm')
    total = TIMELINE['total']
    d.rectangle((0, H - 6, W, H), fill=rgb('#112027'))
    d.rectangle((0, H - 6, int(W * t / total), H), fill=rgb(MINT))
    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stills', help='comma separated seconds')
    args = parser.parse_args()
    if args.stills:
        out = ROOT / 'frames-check'
        out.mkdir(exist_ok=True)
        for s in args.stills.split(','):
            frame(float(s)).save(out / f'{float(s):07.2f}.png')
        return
    total = TIMELINE['total']
    frames = int(math.ceil(total * FPS))
    silent = ROOT / '_build' / 'video.mp4'
    proc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                             '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264',
                             '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', str(silent)],
                            stdin=subprocess.PIPE)
    for n in range(frames):
        proc.stdin.write(frame(n / FPS).tobytes())
        if n % 500 == 0:
            print(f'frame {n}/{frames}', flush=True)
    proc.stdin.close()
    proc.wait()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(silent), '-i', str(ROOT / '_build' / 'mix.wav'),
                    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-af', 'volume=2.4dB', '-c:a', 'aac', '-b:a', '192k',
                    '-ar', '48000', '-shortest', '-movflags', '+faststart', str(OUT)], check=True)
    frame(TIMELINE['scenes'][4]['start'] + 12).save(ROOT / 'poster.jpg', quality=90)
    print(f'wrote {OUT}')


if __name__ == '__main__':
    main()
