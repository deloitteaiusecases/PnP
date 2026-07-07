---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: Physical Count Process

2. **Roles (Swimlanes)**:
   - SC Director / HQ Warehouse Manager
   - Branch WH Managers / WH Section Heads
   - Finance Dept Manager
   - Warehouse

3. **Steps Extracted into a Markdown Table:**

| Step # | Role                                | Action                              | Next Step/Logic       |
|--------|-------------------------------------|-------------------------------------|-----------------------|
| 1      | SC Director / HQ Warehouse Manager  | Start                               | Stock Count MEMO      |
| 2      | SC Director / HQ Warehouse Manager  | Stock Count MEMO                    | Define Count & Generate Tag |
| 3      | Branch WH Managers / WH Section Heads | Define Count & Generate Tag       | Perform Stock Count   |
| 4      | Branch WH Managers / WH Section Heads | Perform Stock Count               | Update Actual Counted Quantities |
| 5      | Branch WH Managers / WH Section Heads | Update Actual Counted Quantities  | Prepare Variance Report |
| 6      | Branch WH Managers / WH Section Heads | Prepare Variance Report           | Submit Variance Report |
| 7      | SC Director / HQ Warehouse Manager  | Submit Variance Report              | Approved?             |
| 8      | SC Director / HQ Warehouse Manager  | Approved (Yes)                      | Count Confirmation & Adjustment |
| 9      | Finance Dept Manager                | Variance Report                     | Approved?             |
| 10     | Finance Dept Manager                | Approved (Yes)                      | Final Count & Adjustment Report |
| 11     | Warehouse                           | Final Count & Adjustment Report     | SAP Quantities Updated |
| 12     | Warehouse                           | SAP Quantities Updated              | End                   |
| A      | Branch WH Managers / WH Section Heads | Rejected                           | Define Count & Generate Tag |

4. **Logic as a Mermaid.js Code Block:**

```mermaid
graph TD;
    A1[Start] --> A2[Stock Count MEMO]
    A2 --> B1[Define Count & Generate Tag]
    B1 --> B2[Perform Stock Count]
    B2 --> B3[Update Actual Counted Quantities]
    B3 --> B4[Prepare Variance Report]
    B4 --> A3[Submit Variance Report]
    A3 --> D1{Approved?}
    D1 -- Yes --> C1[Count Confirmation & Adjustment]
    D1 -- No --> B1
    C1 --> C2[Variance Report]
    C2 --> E1{Approved?}
    E1 -- Yes --> F1[Final Count & Adjustment Report]
    F1 --> G1[SAP Quantities Updated]
    G1 --> H1[End]
    E1 -- No --> B1
```