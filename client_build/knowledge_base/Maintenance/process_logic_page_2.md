---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

#### 1. Process Name

- **Corrective Maintenance**

#### 2. Roles (Swimlanes)

- Operator
- Technician
- Supervisor
- Maintenance
- Stores Team
- SAP PM Administrator

#### 3. Steps in a Markdown Table

| Step # | Role              | Action                                                                                               | Next Step/Logic            |
|--------|-------------------|------------------------------------------------------------------------------------------------------|----------------------------|
| 1      | Operator          | Detect and report equipment malfunction or deviation. (M)                                            | Step 2                     |
| 2      | Technician        | Create SAP breakdown notification with equipment ID, problem description, and timestamp. (A/M)       | Step 3                     |
| 3      | Supervisor        | Review the notification details for completeness and accuracy (M)                                    | Step 4                     |
| 4      | Maintenance       | Convert valid notifications into work orders. Assign priority using the plant priority matrix. (M)   | Step 5                     |
| 5      | Maintenance       | Define job scope, resource requirements, tools, and duration. Update this information in SAP. (M)    | Step 6                     |
| 6      | Supervisor        | Raise a material reservation or purchase requisition in SAP for required spares, tools, or consumables (M) | Step 7                |
| 7      | Stores Team       | Issue parts and materials from stores against the work order. (M)                                    | Step 8                     |
| 8      | Technician        | Carry out repair tasks per SAP work order. Record task completion and observations. (M)              | Step 9                     |
| 9      | Technician        | Verify execution quality, ensure LOTO and safety compliance, and update SAP with work status. (A/M)  | Step 10                    |
| 10     | Technician        | Conduct post-repair testing and release the equipment for operation. (M)                             | Step 11                    |
| 11     | Technician        | Review all logged details. Return unused materials to stores and record returns in SAP. (M)          | Step 12                    |
| 12     | SAP PM Administrator | Technically complete the work order in SAP, entering final fault codes and resolution status. (A/M) | Step 13                    |
| 13     | Maintenance       | Initiate root cause analysis for repeated or critical failures. Document findings and attach to SAP work order (M) | Step 14         |
| 14     | SAP PM Administrator | Prepare reports on breakdown frequency and common failure modes using SAP data. (M)                  | Step 15                    |
| 15     | Maintenance       | Review CM performance reports and identify improvement opportunities. (A/M)                          | End                        |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A1[Start] --> A2[1. Detect and report equipment malfunction or deviation.]
    A2 --> A3[2. Create SAP breakdown notification.]
    A3 --> A4[3. Review notification details for completeness and accuracy.]
    A4 --> A5[4. Convert valid notifications into work orders.]
    A5 --> A6[5. Define job scope and update SAP.]
    A6 --> A7[6. Raise material reservation/purchase requisition in SAP.]
    A7 --> A8[7. Issue parts and materials from stores.]
    A8 --> A9[8. Carry out repair tasks per SAP work order.]
    A9 --> A10[9. Verify execution quality and update SAP.]
    A10 --> A11[10. Conduct post-repair testing and release equipment.]
    A11 --> A12[11. Review all logged details and return unused materials.]
    A12 --> A13[12. Technically complete the work order in SAP.]
    A13 --> A14[13. Initiate root cause analysis for failures.]
    A14 --> A15[14. Prepare reports on breakdown frequency.]
    A15 --> A16[15. Review CM performance reports and identify improvement opportunities.]
    A16 --> End[End]
```