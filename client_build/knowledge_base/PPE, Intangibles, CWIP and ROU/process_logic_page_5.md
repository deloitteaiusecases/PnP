---
Department: PPE, Intangibles, CWIP and ROU
Source_Document: PPE, Intangibles, CWIP and ROU.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

### 1. Process Name
- Impairment

### 2. Roles (Swimlanes)
- GL Manager
- Accounting Manager
- Consultant
- CFO

### 3. Steps in Markdown Table

| Step # | Role             | Action                                                                 | Next Step/Logic        |
|--------|------------------|------------------------------------------------------------------------|------------------------|
| 1      | GL Manager       | Shares relevant data with Consultant for impairment assessment         | Step 2                 |
| 2      | Consultant       | Performs impairment assessment as per IFRS and shares results for review (M) | Step 3                 |
| 3      | Accounting Manager | Review the working (M)                                                  | Step 4                 |
| 4      | CFO              | Approve                                                                 | Yes: Step 5 / No: Step 2 |
| 5      | CFO              | In case of any impairment, the working will be reviewed by the CEO and will be approved by the Board for impairing. Once approved, entry will be recorded in SAP (M/A) | End                    |
| 6      | CFO              | End                                                                    | -                      |

### 4. Logic in Mermaid.js

```mermaid
graph TD;
    A[Start] --> B[Shares relevant data with Consultant for impairment assessment]
    B --> C[Performs impairment assessment as per IFRS and shares results for review (M)]
    C --> D[Review the working (M)]
    D --> E{Approve}
    E -- No --> C
    E -- Yes --> F[In case of any impairment, the working will be reviewed by the CEO and will be approved by the Board for impairing. Once approved, entry will be recorded in SAP (M/A)]
    F --> G[End]
    E -- No adjustment --> G
```