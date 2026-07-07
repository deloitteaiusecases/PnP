---
Department: Inventory
Source_Document: Inventory.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Flowchart Analysis

1. **Process Name**: Slow-moving

2. **Roles (Swimlanes)**:
   - GL Manager
   - Accounting Manager
   - CFO
   - Consultant

3. **Steps in a Markdown Table**:

| Step # | Role               | Action                                                               | Next Step/Logic                                   |
|--------|--------------------|----------------------------------------------------------------------|---------------------------------------------------|
| 1      | GL Manager         | Start                                                                | Step 2                                            |
| 2      | GL Manager         | Shares data with consultant                                          | Step 3                                            |
| 3      | Consultant         | Prepare detailed working for slow moving as per IFRS (M)             | Step 4                                            |
| 4      | Accounting Manager | Review the working (M)                                               | Step 5                                            |
| 5      | CFO                | Approve                                                              | If Yes: Step 6 / If No: Step 4                    |
| 6      | CFO                | In case of provisioning, review by Senior Management and record in SAP | End (For Adjustment) / Step 7 (For No Adjustment) |
| 7      | CFO                | No adjustment                                                        | End                                               |

4. **Mermaid.js Code Block**:

```mermaid
graph TD
    A1(Start) --> A2(Shares data with consultant)
    A2 --> A3(Prepare detailed working for slow moving as per IFRS)
    A3 --> A4(Review the working)
    A4 --> A5{Approve}
    A5 -- Yes --> A6(In case of provisioning, review by Senior Management and record in SAP)
    A5 -- No --> A4
    A6 --> A7[End]
    A6 -.-> A8(No adjustment)
    A8 --> A7
```