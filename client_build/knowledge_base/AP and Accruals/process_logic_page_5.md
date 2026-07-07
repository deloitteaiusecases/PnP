---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:** GR IR reconciliation

2. **Roles (Swimlanes):**
   - SAP
   - GL Manager
   - Accounting Manager
   - AP Unit Team

3. **Steps in Markdown Table:**

| Step # | Role              | Action                                                                                                                                     | Next Step/Logic |
|--------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| 1      | GL Manager        | Extract the GR/IR report from SAP, detailing supplier-wise and Goods/Service Receipt Note (GSRN) wise information.                         | Step 2          |
| 2      | GL Manager        | Review validates the GR/IR balance on a monthly basis and shares the report with the Accounting Manager via email for review of the final working. | Step 3          |
| 3      | Accounting Manager| Review the final working and approve.                                                                                                      | Step 4          |
| 4      | AP Unit Team      | Follow up with the procurement department, who in turn follows up with relevant suppliers to expedite the receipt of outstanding invoices. Once the invoice is received and processed, the GR/IR balance is reversed automatically as per invoice processing procedures. | End             |

4. **Logic in Mermaid.js Code Block:**

```mermaid
graph TD;
    Start --> A1;
    A1[Extract the GR/IR report from SAP, detailing supplier-wise and Goods/Service Receipt Note (GSRN) wise information.] --> A2;
    A2[Review validates the GR/IR balance on a monthly basis and shares the report with the Accounting Manager via email for review of the final working.] --> A3;
    A3[Review the final working and approve.] --> A4;
    A4[Follow up with the procurement department, expedite the receipt of outstanding invoices. Once the invoice is received and processed, the GR/IR balance is reversed automatically.] --> End;
```