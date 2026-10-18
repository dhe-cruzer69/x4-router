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

