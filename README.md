# x4-router

X4 independent parent — **routing** (policies, registry). gRPC. Fleet id **2**.

| Field | Value |
|-------|-------|
| Completion | **L0** — bootstrapped |
| Boundary | independent-parent |

No production routing is claimed until evidence states advance.

<!-- X4-APEX-DIAGRAM-START:x4-router -->

```mermaid
flowchart TD
    REQUEST[Model or Tool Request] --> REGISTRY[Provider and Capability Registry]
    REGISTRY --> POLICY[Routing Policy]
    POLICY --> DECIDE{Eligible Route?}
    DECIDE -->|none or unknown| UNKNOWN[Return UNKNOWN / No Production Claim]
    DECIDE -->|candidate found| SELECT[Select Candidate]
    SELECT --> DISPATCH[Dispatch Through Configured Adapter]
    DISPATCH --> VERIFY[Check Response Status]
    VERIFY --> RESULT[Return Result and Routing Metadata]
    NOTE[L0 bootstrapped repository] -. current maturity boundary .-> UNKNOWN
```

<!-- X4-APEX-DIAGRAM-END:x4-router -->

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
