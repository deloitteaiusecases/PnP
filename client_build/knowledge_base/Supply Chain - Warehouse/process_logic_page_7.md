---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name:**
   - Warehouse Inspection

2. **Roles (Swimlanes):**
   - WH Section Heads
   - Inspection Team
   - SC Director / HQ WH Manager

3. **Steps in Markdown Table:**

| Step # | Role                  | Action                                             | Next Step/Logic                                  |
|--------|-----------------------|----------------------------------------------------|--------------------------------------------------|
| 1      | WH Section Heads      | Start                                              | 2                                                |
| 2      | WH Section Heads      | Prepare & Circulate Inspection Memo & Checklist    | 3                                                |
| 3      | Inspection Team       | Check all Records and Readiness                    | 4 (Yes) / 5 (No)                                 |
| 4      | Inspection Team       | Briefing Meeting                                   | 6                                                |
| 5      | Inspection Team       | Log all fact & Photos                              | 3                                                |
| 6      | Inspection Team       | Perform Complete Inspection                        | 7                                                |
| 7      | Inspection Team       | Any non-conformities?                              | 5 (Yes) / 8 (No)                                 |
| 8      | SC Director / HQ WH Manager | Submit Final Report (within 3 working days)   | 9                                                |
| 9      | SC Director / HQ WH Manager | Approved                                       | 10 (Yes) / 6 (No)                                |
| 10     | SC Director / HQ WH Manager | Final Report                                  | 11                                               |
| 11     | SC Director / HQ WH Manager | End                                            | -                                                |

4. **Logic in Mermaid.js Code Block:**

```mermaid
graph TD;
    A1(Start) --> A2(Prepare & Circulate Inspection Memo & Checklist)
    A2 --> A3(Check all Records and Readiness)
    A3 -- Yes --> A4(Briefing Meeting)
    A3 -- No --> B5(Log all fact & Photos)
    B5 --> A3
    A4 --> A6(Perform Complete Inspection)
    A6 --> A7(Any non-conformities?)
    A7 -- Yes --> B5
    A7 -- No --> A8(Submit Final Report (within 3 working days))
    A8 --> A9(Approved)
    A9 -- Yes --> A10(Final Report)
    A9 -- No --> A6
    A10 --> A11(End)
```
