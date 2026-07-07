---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 12
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: HANDLING WOODEN & PLASTIC PALLETS (Receiving)

2. **Roles (Swimlanes)**:
   - Procurement
   - DC Officer
   - Quality Control

3. **Steps Table**

| Step # | Role         | Action                                                                 | Next Step/Logic                                           |
|--------|--------------|------------------------------------------------------------------------|-----------------------------------------------------------|
| 1      | Procurement  | Start                                                                  | Step 2                                                    |
| 2      | Procurement  | Raise Purchase Order (PO) for pallets                                  | Step 3                                                    |
| 3      | DC Officer   | Receive pallets, verify quantity, and notify QC for inspection.        | Step 4                                                    |
| 4      | Quality Control | Inspect for quality, damage, and compliance. Segregate rejected pallets. | If cleared, go to Step 5; if rejected, go back to Step 3 |
| 5      | DC Officer   | Accept cleared pallets and stack by type.                              | Step 6                                                    |
| 6      | DC Officer   | Record pallet data (type, quantity, PO, QC status) in SAP.             | End                                                       |
| End    |              | End                                                                    |                                                           |

4. **Mermaid.js Code Block**

```mermaid
graph TD;
    A(Start) --> B(Raise Purchase Order (PO) for pallets)
    B --> C(Receive pallets, verify quantity, and notify QC for inspection)
    C --> D{Inspect for quality, damage, and compliance}
    D -->|Cleared| E(Accept cleared pallets and stack by type)
    E --> F(Record pallet data (type, quantity, PO, QC status) in SAP)
    F --> G(End)
    D -->|Rejected| C
```
