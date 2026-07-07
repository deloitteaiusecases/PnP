---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 10
Last_Updated: 2026-03-16
---

## Analysis

1. **Process Name**: Handling Wooden & Plastic Pallets (Issuance Plastic Pallet)

2. **Roles (Swimlanes)**:
   - FG WH Section Head/DC
   - Packaging Warehouse
   - Production Department
   - Sales Department
   - Logistics
   - Finance
   - IT Team

3. **Steps Table**:

| Step # | Role                       | Action                                                 | Next Step/Logic                         |
|--------|----------------------------|--------------------------------------------------------|-----------------------------------------|
| 1      | FG WH Section Head/DC      | Start                                                  | Step 2                                  |
| 2      | FG WH Section Head/DC      | Create SAP Reservation Document.                       | Step 3                                  |
| 3      | FG WH Section Head/DC      | Physically receive and document pallets                | Step 4                                  |
| 4      | FG WH Section Head/DC      | Issue pallets to packing area.                         | Step 6                                  |
| 5      | Packaging Warehouse        | Real-Time Tracking Report                              | Step 2                                  |
| 6      | Packaging Warehouse        | SAP Transfer Posting                                   | Step 7                                  |
| 7      | Production Department      | Raise pallet request as per shift/load dispatch.       | Step 9                                  |
| 8      | Sales Department           | Include pallet details on invoice.                     | Step 7                                  |
| 9      | Sales Department           | Define pallet type and quantity per sales order.       | Step 10                                 |
| 10     | Logistics                  | Dispatch plastic pallets with FG.                      | Step 11                                 |
| 11     | Finance                    | Record customer guarantee money (no VAT).              | Step 12                                 |
| 12     | IT Team                    | Pallet Reconciliation Report                           | End                                     |
| 13     | IT Team                    | End                                                    |                                         |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A1[Start] --> A2[Create SAP Reservation Document.]
    A2 --> A3[Physically receive and document pallets]
    A3 --> A4[Issue pallets to packing area.]
    A5[Real-Time Tracking Report] --> A2
    A4 --> A6[SAP Transfer Posting]
    A6 --> A7[Raise pallet request as per shift/load dispatch.]
    A8[Include pallet details on invoice.] --> A6
    A7 --> A9[Define pallet type and quantity per sales order.]
    A9 --> A10[Dispatch plastic pallets with FG.]
    A10 --> A11[Record customer guarantee money (no VAT).]
    A11 --> A12[Pallet Reconciliation Report]
    A12 --> A13[End]
```