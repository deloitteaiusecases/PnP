---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:**
   - Product Recalls / Customer Damage / Near Expiry FG Return

2. **Roles (Swimlanes):**
   - Sales Representative
   - DC Officer / WH Section Head
   - Recall / Return Committee

3. **Steps in Markdown Table:**

   | Step # | Role                         | Action                                             | Next Step/Logic                  |
   |--------|------------------------------|----------------------------------------------------|----------------------------------|
   | 1      | Sales Representative         | Start                                              | Step 2                           |
   | 2      | Sales Representative         | Return Report                                      | Step 3                           |
   | 3      | DC Officer / WH Section Head | Return Items List                                  | Step 4                           |
   | 4      | DC Officer / WH Section Head | Weighing Scale Ticket                               | Step 5                           |
   | 5      | DC Officer / WH Section Head | Verify & Classify Returns in coordination with QC team | If approved, Step 6; If rejected, Step 3 |
   | 6      | Recall / Return Committee    | Approved?                                          | If Yes, Step 7; If No, Step 3    |
   | 7      | Recall / Return Committee    | Signed Return Voucher                              | Step 8                           |
   | 8      | Recall / Return Committee    | Dispose                                            | Step 9                           |
   | 9      | Recall / Return Committee    | End                                                | -                                |

4. **Mermaid.js Code Block:**

   ```mermaid
   graph TD;
     A(Start) --> B(Return Report)
     B --> C(Return Items List)
     C --> D(Weighing Scale Ticket)
     D --> E(Verify & Classify Returns in coordination with QC team)
     E -->|Approved| F{Approved?}
     E -->|Rejected| C
     F -->|Yes| G(Signed Return Voucher)
     F -->|No| C
     G --> H(Dispose)
     H --> I(End)
   ```
