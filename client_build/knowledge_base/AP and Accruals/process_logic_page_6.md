---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

### 1. Process Name
Payable Reconciliation

### 2. Roles (Swimlanes)
- AP Accountant
- AP Unit Head
- GL Manager/Accounting Manager

### 3. Steps in Markdown Table

| Step # | Role                      | Action                                                                    | Next Step/Logic             |
|--------|---------------------------|---------------------------------------------------------------------------|-----------------------------|
| 1      | AP Accountant             | Reconciliation (a) GL and Sub-ledger and (b) Reconcile email received vs recorded in SAP | Step 2                      |
| 2      | AP Unit Head              | Review reconciliation                                                     | Approved?                   |
| 3      | GL Manager/Accounting Manager | Approved?                                                                   | Yes: Share reconciliation with CFO / No: Step 2 |
| 4      | GL Manager/Accounting Manager | Share reconciliation with CFO to keep him informed and for discussion purpose | End                         |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1
    A1[Reconciliation (a) GL and Sub-ledger and (b) Reconcile email received vs recorded in SAP] --> A2
    A2[Review reconciliation] --> A3{Approved?}
    A3 -- Yes --> A4[Share reconciliation with CFO to keep him informed and for discussion purpose]
    A3 -- No --> A2
    A4 --> End
```
