---
Department: Supply Chain - Logistics
Source_Document: Supply Chain - Logistics.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Finished Goods Transportation - Key Account & Distributor

2. **Roles (Swimlanes)**:
   - Sales
   - Weigh-in Scale
   - Transportation
   - Truck Driver
   - FG Warehouse

3. **Steps in Markdown Table**:

| Step # | Role            | Action                        | Next Step/Logic                 |
|--------|-----------------|-------------------------------|---------------------------------|
| 1      | Sales           | Start                         | Truck Scale                     |
| 2      | Weigh-in Scale  | Truck Scale                   | Delivery Note & Scale Ticket    |
| 3      | Weigh-in Scale  | Delivery Note & Scale Ticket  | SAP Loading Doc.                |
| 4      | Transportation  | SAP Loading Doc.              | Vehicle Driver Allotment        |
| 5      | Transportation  | Vehicle Driver Allotment      | Check                           |
| 6      | Truck Driver    | Check                         | Yes: Loading Truck Issue Order  |
| 7      | FG Warehouse    | Loading Truck Issue Order     | Report                          |
| 8      | Transportation  | Report                        | Final Scale Ticket & Invoice    |
| 9      | Sales           | Final Scale Ticket & Invoice  | End                             |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A(Start) --> B(Truck Scale);
    B --> C(Delivery Note & Scale Ticket);
    C --> D(SAP Loading Doc.);
    D --> E(Vehicle Driver Allotment);
    E --> F{Check};
    F -- Yes --> G(Loading Truck Issue Order);
    G --> H(Report);
    H --> I(Final Scale Ticket & Invoice);
    I --> J(End);
```
