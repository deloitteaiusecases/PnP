---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

#### 1. Process Name
- Spare Parts Management

#### 2. Roles (Swimlanes)
- Maintenance
- Store Team
- SAP PM/MM Administrator
- Technician
- Supervisor
- Procurement Department

#### 3. Steps in Markdown Table

| Step # | Role                    | Action                                                                                     | Next Step/Logic               |
|--------|-------------------------|--------------------------------------------------------------------------------------------|-------------------------------|
| 1      | Maintenance             | Tag parts with safety, regulatory, or high downtime impact as "critical" in SAP            | 2                             |
| 2      | Store Team              | Review movement history and classify parts with minimal annual usage as low-moving         | 3                             |
| 3      | Store Team              | Define and enter min/max stock and reorder points for all stocked parts in SAP             | 4                             |
| 4      | Maintenance             | Review and approve any proposed changes to reorder levels or MRP parameters                | 5                             |
| 5      | SAP PM/MM Administrator | Run Material Requirements Planning (MRP) in SAP to trigger proposals for purchase requisitions | 6                         |
| 6      | Technician              | Raise material reservations or PRs through SAP against a work order                        | 7                             |
| 7      | Supervisor              | Review and approve spare part requisitions for processing                                   | 8                             |
| 8      | Procurement Department  | Convert approved PRs into POs in SAP and issue to vendor                                   | 10                            |
| 9      | Maintenance             | Authorize emergency spares procurement due to breakdown or safety-critical needs            | 10                            |
| 10     | Store Team              | Receive delivered parts, verify quantity/quality, and record goods receipt in SAP          | 11, 14                        |
| 11     | Technician              | Issue spare parts through SAP against the relevant maintenance work order                  | 12                            |
| 12     | Technician              | Log part usage details in the SAP work order and return unused materials                   | 15                            |
| 13     | Store Team              | Reconcile physical and SAP stock, investigate variances, and adjust where necessary        | 15                            |
| 14     | SAP PM/MM Administrator | Generate SAP reports to flag non-moving, excess, or obsolete inventory                     | 15                            |
| 15     | Maintenance             | Evaluate SAP reports and recommend corrective actions (write-off, reallocation, etc.)      | End                           |

#### 4. Logic as Mermaid.js Code Block

```mermaid
graph TD
    A(Start) --> B[1. Tag parts as "critical" in SAP]
    B --> C[2. Review movement history and classify parts]
    C --> D[3. Define and enter min/max stock points in SAP]
    D --> E[4. Review and approve changes to reorder levels or MRP parameters]
    E --> F[5. Run MRP in SAP]
    F --> G[6. Raise material reservations or PRs in SAP]
    G --> H[7. Review and approve spare part requisitions]
    H --> I[8. Convert approved PRs into POs in SAP]
    I --> J[10. Receive delivered parts, verify and record in SAP]
    E --> K[9. Authorize emergency spares procurement]
    K --> J
    J --> L[11. Issue spare parts through SAP]
    L --> M[12. Log part usage in SAP and return unused materials]
    M --> N[15. Evaluate SAP reports and recommend actions]
    J --> O[14. Generate SAP reports for inventory]
    O --> N
    J --> P[13. Reconcile physical and SAP stock]
    P --> N
    N --> Q(End)
```
