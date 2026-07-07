---
Department: Sales P&P
Source_Document: Sales P&P.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

### 1. Process Name
B2C Sales Process

### 2. Roles (Swimlanes)
- Sales
- Finance Manager
- Supply Chain Manager
- Logistics Manager

### 3. Steps

| Step # | Role                 | Action                                                                                              | Next Step/Logic                                                               |
|--------|----------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 1      | Sales                | Received Purchase order/Sales Order form and cash deposit evidence. (A)                             | Step 2                                                                        |
| 2      | Sales                | Generate Sales Order in the SAP system on same day of receiving PO/Order form. (A)                  | Step 3.1                                                                      |
| 3.1    | Finance Manager      | Verify all data of Sales order and approves or rejects. (M)                                         | If approved, go to Step 3.2; if not, go to Step 3.3                           |
| 3.2    | Supply Chain Manager | Verify stock position in the warehouse and approves or rejects. (M)                                 | If approved, go to Step 4; if not, go to Step 3.3                             |
| 3.2.1  | Supply Chain Manager | Approved?                                                                                           | Yes: Step 4; No: Step 3.3                                                     |
| 3.3    | Finance Manager      | Discuss delivery timelines with Sales team/customer and modify or cancel Sales order. (M)           | Back to Step 3.1                                                              |
| 4      | Sales                | Issues loading order in the system immediately after approval of SO. (A)                            | Step 5                                                                        |
| 5      | Logistics Manager    | Arrange vehicle for dispatch and load it with required stock. Loaded vehicle will be dispatched. (M) | Step 6                                                                        |
| 6      | Logistics Manager    | Receive customer Goods Receiving Note (GRN) along with Invoice receiving copy by the driver. (A/M)  | End                                                                           |

### 4. Logic in Mermaid.js

```mermaid
graph TD;
    A1(Start) --> A2[1. Received Purchase order/Sales Order form and cash deposit evidence. (A)]
    A2 --> A3[2. Generate Sales Order in the SAP system on same day of receiving PO/Order form. (A)]
    A3 --> B1[3.1. Verify all data of Sales order and approves or rejects. (M)]
    B1 -->|Approved| C1[3.2. Verify stock position in the warehouse according to Sales order and approves or rejects. (M)]
    B1 -->|Rejected| D1[3.3. Discuss delivery timelines with Sales team/customer and modify or cancel Sales order. (M)]
    C1 -->|Approved| E1[4. Issues loading order in the system immediately after approval of SO. (A)]
    C1 -->|Rejected| D1
    D1 --> B1
    E1 --> F1[5. Arrange vehicle for dispatch and load it with required stock. (M)]
    F1 --> G1[6. Receive customer Goods Receiving Note (GRN) along with Invoice receiving copy by the driver. (A/M)]
    G1 --> H1(End)
```
