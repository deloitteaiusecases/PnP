---
Department: Marketing P&P
Source_Document: Marketing P&P.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

1. **Process Name:** 
   - E-Commerce Customer Sales Order Procedure

2. **Roles (Swimlanes):** 
   - E Commerce Specialist
   - Finance Manager
   - Supply Chain
   - Logistics Manager

3. **Markdown Table:**

   | Step # | Role                | Action                                                                                               | Next Step/Logic                                      |
   |--------|---------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------|
   | 1      | E Commerce Specialist | Receives Purchase order via email from the customer. (M)                                            | 2                                                    |
   | 2      | E Commerce Specialist | Specialist generates Sales Order in the SAP system on the same day of receiving PO. (A/M)          | 3                                                    |
   | 3      | Finance Manager       | Verifies all data of Sales order, and approves or rejects (M)                                       | 3.1 (if approved), End (if rejected)                 |
   | 3.1    | Supply Chain          | Verifies stock position in the warehouse according to Sales order and approves or rejects (M)       | 4 (if approved), End (if rejected)                   |
   | 4      | Supply Chain          | Issues loading order in the system immediately after approval of SO. (M)                            | 5                                                    |
   | 5      | Logistics Manager     | Arranges vehicle for dispatch and loads it with required stock. (M)                                 | 6                                                    |
   | 6      | Logistics Manager     | Receives customer Goods receiving note (GRN) along with Invoice receiving copy by the driver. (A/M) | End                                                  |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    A(Start) --> B[Receives Purchase order via email from the customer. (M)];
    B --> C[Specialist generates Sales Order in the SAP system on the same day of receiving PO. (A/M)];
    C --> D[Verifies all data of Sales order, and approves or rejects (M)];
    D -->|Approves| E[Verifies stock position in the warehouse and approves or rejects (M)];
    D -->|Rejects| F(End);
    E -->|Approves| G[Issues loading order in the system immediately after approval of SO. (M)];
    E -->|Rejects| F;
    G --> H[Arranges vehicle for dispatch and loads it with required stock. (M)];
    H --> I[Receives customer GRN along with Invoice receiving copy by the driver. (A/M)];
    I --> F;
```