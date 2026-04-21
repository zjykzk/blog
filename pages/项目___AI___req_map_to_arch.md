---
title: 项目/AI/req_map_to_arch source note
type: source
status: archived
updated: 2026-04-21
aliases:
  - 项目___AI___req_map_to_arch
  - 项目/AI/req_map_to_arch
---

# 项目/AI/req_map_to_arch source note

沉淀后的主题页：[[wiki/topics/Requirement to Architecture Mapping]]

## 原始摘录

## Input Normalization

Normalize all inputs into this structure before validating:

  feature: <business capability>
  use_case: <system action>
  entry:
    protocol: <http | rpc | mq | cron | internal>
    handler: <entrypoint>
  input:
	- <field>
	  output:
	- <field>
	  business_rules:
	- <rule>
	  domain_objects:
	- <entity>
	  data_access:
	- <db/cache/storage operation>
	  external_calls:
	- <rpc/http/mq/third-party call>
	  errors:
	- <business error>
	  shared_utils:
	- <pure utility>
	  assumptions:
	- <inference if needed>
	  
	  If the source input is incomplete, infer conservatively and mark assumptions.
- ## Source Mapping Rules
- ### Free-Form Requirement
  
  Example:
  
    Add create order API with inventory validation.
  
  Expand into:
  
  • entry
  • request/response
  • business rules
  • domain objects
  • data access
  • external calls
  • errors
  • shared utilities
- ### User Story
  
  Example:
  
    As a merchant, I want order creation to validate inventory, so that overselling is prevented.
  
  Map as:
  
  • actor → context only
  • goal → use case
  • value → business rule or success criteria
  • user action → API entry
  • business decision → service/
  • storage/integration need → Service-defined repo interface + Infra implementation
- ### PRD
  
  Use this transformation:
  
    PRD -> Features -> Use Cases -> Normalized Requirement Units -> Architecture Mapping
  
  Interpret PRD sections like this:
  
   PRD Section             │ Architectural meaning
  ─────────────────────────┼─────────────────────────────────────────────────────
   user flow / scenarios   │ use cases and entrypoints
   functional requirements │ service use cases
   payload fields          │ API contract
   business rules          │ service logic
   state transitions       │ service logic
   data requirements       │ repo interfaces in service, implementation in infra
   dependency systems      │ service-owned interfaces, infra implementations
   failure cases           │ business errors in service + protocol errors in api
- ## Mapping Rules
- ### Map to api/
  
  Put these in api/:
  
  • HTTP/RPC/MQ/Cron entrypoints
  • handlers
  • request/response DTOs
  • service interfaces consumed by handlers
  • protocol error codes
  • mapping service errors to external responses
  
  Typical outputs:
  
  • api/handler/*.go
  • API-defined service interface
  • api/error_code.go
  • api/server.go
- ### Map to service/
  
  Put these in service/:
  
  • use cases
  • business validation
  • state transitions
  • orchestration logic
  • domain entities
  • business errors
  • transaction decisions
  
  Typical outputs:
  
  • service/<module>/service.go
  • service/<module>/<entity>.go
  • service/<module>/errors.go
- ### Map repo interfaces to service/
  
  If Service needs these capabilities, define interfaces in service/:
  
  • save/load/update/query data
  • cache access
  • publish events
  • call RPC/HTTP dependencies
  • use storage or third-party systems
  
  Typical outputs:
  
  • service/<module>/<entity>_repo.go
  • or capability-specific files like:
    • order_repo.go
    • inventory_repo.go
    • event_repo.go
- ### Map to infra/
  
  Put technical implementations in infra/:
  
  • MySQL / Redis / ES / S3
  • RPC/HTTP clients
  • MQ producers/consumers
  • SDK adapters
  • SQL construction and execution
  
  Typical outputs:
  
  • infra/mysql/<module>/*.go
  • infra/rpc/<dependency>/*.go
  • infra/http/<dependency>/*.go
  • infra/mq/<module>/*.go
- ### Map to pkg/
  
  Only pure technical helpers go to pkg/:
  
  • ID generation
  • time helpers
  • serialization helpers
  • string/map/slice utilities
  • retry/backoff helpers without business meaning
  
  Never put these in pkg/:
  
  • business validation
  • workflow logic
  • domain decisions
  • business RPC/HTTP integrations
- ## Decision Heuristics
  
  When unsure, ask in this order:
  
  1. Is this about protocol entry, handler contract, or external error exposure?
    • api/
  2. Is this about business judgment, validation, workflow, or state change?
    • service/
  3. Is this a capability Service needs from outside?
    • define interface in service/
  4. Is this a concrete technical implementation?
    • infra/
  5. Is this a pure reusable helper?
    • pkg/

## Related

- [[wiki/topics/Requirement to Architecture Mapping]]
- [[wiki/syntheses/AI Engineering Workflow]]
- [[wiki/maps/AI Map]]
