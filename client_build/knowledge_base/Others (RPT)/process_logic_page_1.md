---
Department: Others (RPT)
Source_Document: Others (RPT).pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:** Related Party

2. **Roles (Swimlanes):**
   - Accounting Manager
   - CFO
   - AR Manager

3. **Steps in Markdown Table:**

   | Step # | Role               | Action                                                    | Next Step/Logic       |
   |--------|--------------------|-----------------------------------------------------------|-----------------------|
   | 1      | Accounting Manager | Obtains list of related parties from legal department (M) | Step 2                |
   | 2      | Accounting Manager | Validates the listing as per IAS 24 (M)                   | Step 3                |
   | 3      | CFO                | Approve                                                   | Yes: Step 4, No: Step 2 |
   | 4      | AR Manager         | Documents transactions and disclosure of related party (M) | Step 5                |
   | 5      | CFO                | Review the transactions and disclosures (M)               | End                   |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    A(Start) --> B[Obtains list of related parties from legal department (M)]
    B --> C[Validates the listing as per IAS 24 (M)]
    C --> D{Approve}
    D -- Yes --> E[Documents transactions and disclosure of related party (M)]
    E --> F[Review the transactions and disclosures (M)]
    D -- No --> C
    F --> G(End)
```

This code represents the flowchart logic and explicitly shows the decision paths between steps.