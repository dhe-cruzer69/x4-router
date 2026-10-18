# x4-router

X4 independent parent — **routing** (policies, registry). gRPC. Fleet id **2**.

| Field | Value |
|-------|-------|
| Completion | **L0** — bootstrapped |
| Boundary | independent-parent |

No production routing is claimed until evidence states advance.

## APEX Architecture Map

> Status: architecture documentation; implementation and deployment claims require independent verification.

```mermaid
flowchart TB
  Request[Inference request] --> Validate[Validate size, model, and policy]
  Validate --> Classify[Estimate task class and constraints]
  Classify --> Policy{Provider policy}
  Policy -->|local-only| Local[Local model candidate]
  Policy -->|approved remote allowed| Remote[Eligible remote candidate]
  Policy -->|no eligible provider| Block[Return no-provider error]
  Local --> Health{Provider healthy and model ready?}
  Remote --> Health
  Health -->|no| Fallback{Fallback permitted?}
  Fallback -->|no| Unavailable[Return unavailable]
  Fallback -->|yes| Alternate[Select next eligible provider]
  Alternate --> Health
  Health -->|yes| Invoke[Invoke with timeout and budget]
  Invoke --> Check{Response valid?}
  Check -->|no| Fallback
  Check -->|yes| Result[Return response + routing rationale]
```
**Evidence note:** Routing policy, health probes, fallback ordering, and budget enforcement must be validated in code; do not imply remote routing is active unless explicitly configured.

