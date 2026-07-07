---
Department: Inventory
Source_Document: Inventory.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

### Process Name:
Identify Cost of Allocation

### Roles (Swimlanes):
1. Costing Manager
2. CFO

### Steps in Markdown Table:

| Step # | Role          | Action                                                                       | Next Step/Logic                     |
|--------|---------------|------------------------------------------------------------------------------|-------------------------------------|
| 1      | Costing Manager | Identify all GL (General Ledger) which will be allocated to inventory and shares for review and approval. | 2                                   |
| 2      | CFO           | Approve                                                                      | Yes -> 3, No -> 1                   |
| 3      | Costing Manager | Update GL in SAP for allocation of cost                                      | 4                                   |
| 4      | Costing Manager | Review overall cost of goods sold and inventory valuation monthly           | End                                 |

### Logic in Mermaid.js:

```mermaid
graph TD;
    A(Start) --> B1[Costing Manager identifies all GL which will be allocated to inventory and shares for review and approval]
    B1 --> C{Approve}
    C -- No --> B1
    C -- Yes --> D2[Update GL in SAP for allocation of cost]
    D2 --> E3[Review overall cost of goods sold and inventory valuation monthly]
    E3 --> F(End)
```
