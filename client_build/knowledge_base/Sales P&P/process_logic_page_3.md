---
Department: Sales P&P
Source_Document: Sales P&P.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**
   - B2B Sales Process

2. **Roles (Swimlanes)**
   - Sales
   - Finance Manager
   - Supply Chain Manager
   - Logistics Manager

3. **Steps in Markdown Table**

| Step # | Role                | Action                                                                                                            | Next Step/Logic   |
|--------|---------------------|-------------------------------------------------------------------------------------------------------------------|-------------------|
| 1      | Sales               | Received Purchase order/Sales Order form and payment evidence. (A)                                                | Step 2            |
| 2      | Sales               | Generate Sales Order in the SAP system on same day of receiving PO/Order form. (A)                                 | Step 3.1          |
| 3.1    | Finance Manager     | Verify all data of Sales order and approves or rejects. (M)                                                       | Step 3.2          |
| 3.2    | Supply Chain Manager| Verify stock position in the warehouse and approves or rejects. If stock is not available, communicate to Sales. (M)| Step 3.2.1        |
| 3.2.1  | Supply Chain Manager| Approved?                                                                                                         | Yes: Step 4       |
|        |                     |                                                                                                                   | No: Step 3.3      |
| 3.3    | Sales               | Discuss delivery timelines with Sales team/customer and modify or cancel Sales order after aligning with customer.(M)| Step 2            |
| 4      | Sales               | Issues loading order in the system immediately after approval of SO. (A)                                          | Step 5            |
| 5      | Logistics Manager   | Arrange vehicle for dispatch and load it with required stock. Loaded vehicle dispatched to weighing bridge. (M)    | Step 6            |
| 6      | Logistics Manager   | Receive customer Goods receiving note (GRN) and Invoice receiving copy. Driver delivers to logistics department. (A/M)| End               |

4. **Mermaid.js Code Block**

```mermaid
graph TD;
    Start-->A1[Received Purchase order/Sales Order form and payment evidence. (A)]
    A1-->A2[Generate Sales Order in the SAP system. (A)]
    A2-->M1[Verify all data of Sales order and approve/reject. (M)]
    M1-->M2[Verify stock position in warehouse and approve/reject. (M)]
    M2-->D1{Stock Approved?}
    D1-->|Yes|A3[Issues loading order in system. (A)]
    D1-->|No|M3[Discuss delivery timelines and modify/cancel order. (M)]
    M3-->A2
    A3-->M4[Arrange vehicle for dispatch. (M)]
    M4-->M5[Receive customer GRN and Invoice. (A/M)]
    M5-->End
```
