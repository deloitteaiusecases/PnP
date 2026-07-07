---
Department: Inventory
Source_Document: Inventory.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

#### Process Name
- Inventory Classification

#### Roles (Swimlanes)
1. User
2. Costing Manager
3. Accounting Manager
4. Supply Chain P&P
5. Operations

#### Steps in a Markdown Table

| Step # | Role               | Action                                                                                     | Next Step / Logic                    |
|--------|--------------------|--------------------------------------------------------------------------------------------|-------------------------------------|
| 1      | User               | Initiate request duly approved by Department head for purchase the inventory (M)           | Step 2                              |
| 2      | Costing Manager    | Inventory is created in SAP (M)                                                            | Step 3                              |
| 3      | Supply Chain P&P   | Generation of PO                                                                           | Step 4                              |
| 4      | Supply Chain P&P   | Receipt of inventory                                                                       | Step 5                              |
| 5      | Supply Chain P&P   | System generated entry is posted for inventory and GR/IR and validated by Accounting team (A) | Step 6                            |
| 6      | Operations         | Upon issuance of inventory during manufacturing process, classification of inventory is updated to WIP or FG (A) | Step 7                |
| 7      | Accounting Manager | Inventory classification is reviewed                                                       | End                                 |

#### Mermaid.js Code Block

```mermaid
graph TD;
    A(Start) --> B[Initiate request duly approved by Department head for purchase the inventory (M)];
    B --> C[Inventory is created in SAP (M)];
    C --> D[Generation of PO];
    D --> E[Receipt of inventory];
    E --> F[System generated entry is posted for inventory and GR/IR and validated by Accounting team (A)];
    F --> G[Upon issuance of inventory during manufacturing process, classification of inventory is updated to WIP or FG (A)];
    G --> H[Inventory classification is reviewed];
    H --> I(End);
```
