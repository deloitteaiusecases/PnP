---
Department: Financial Reporting
Source_Document: Financial Reporting.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:**
   - Planning

2. **Roles (Swimlanes):**
   - GL Manager
   - Accounting Manager
   - CFO

3. **Steps in a Markdown Table:**

   | Step # | Role             | Action                                      | Next Step/Logic                    |
   |--------|------------------|---------------------------------------------|------------------------------------|
   | 1      | GL Manager       | Start                                       | Step 2                             |
   | 2      | GL Manager       | Set-up calendar for periodical reporting (M)| Step 3                             |
   | 3      | Accounting Manager | Review the calendar (M)                    | Approve?                           |
   | 4      | CFO              | Approve                                     | Yes: Step 5, No: Step 3            |
   | 5      | GL Manager/Accounting Manager | Communicate to all department (A/M) | Step 6                             |
   | 6      | GL Manager/Accounting Manager | End                                         |                                    |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    A[Start] --> B[Set-up calendar for periodical reporting (M)]
    B --> C[Review the calendar (M)]
    C --> D{Approve}
    D -- Yes --> E[Communicate to all department (A/M)]
    D -- No --> C
    E --> F[End]
```

This provides a structured representation of the flowchart depicted in the image.