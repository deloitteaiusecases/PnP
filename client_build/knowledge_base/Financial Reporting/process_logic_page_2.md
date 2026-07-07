---
Department: Financial Reporting
Source_Document: Financial Reporting.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

1. **Process Name**: GL period closure

2. **Roles (Swimlanes)**:
   - Accounting Manager
   - Relevant Stakeholders

3. **Steps in Markdown Table**:

   | Step # | Role                | Action                                            | Next Step/Logic                    |
   |--------|---------------------|---------------------------------------------------|-----------------------------------|
   | 1      | Accounting Manager  | Start                                             | 2                                 |
   | 2      | Accounting Manager  | Communicate to all departments for closure checklist and module closing | 3, 4                             |
   | 3      | Accounting Manager  | Closure of GL Module and GL Period                | 5                                 |
   | 4      | Relevant Stakeholders | Closure of Module                                | 3                                 |
   | 5      | Accounting Manager  | End                                               | -                                 |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A1(Start) --> A2(Communicate to all departments for closure checklist and module closing);
    A2 --> A3(Closure of GL Module and GL Period);
    A2 --> R1(Closure of Module);
    R1 --> A3;
    A3 --> A4(End);
```
