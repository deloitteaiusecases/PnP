---
Department: Zakat, VAT and WHT
Source_Document: ZAKAT, VAT and WHT.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

Sure, let's analyze the flowchart:

### 1. Process Name
- **Withholding Tax**

### 2. Roles (Swimlanes)
- AP Accountant
- AP Unit Head
- Tax Manager

### 3. Steps in Markdown Table

| Step # | Role           | Action                                                   | Next Step/Logic                        |
|--------|----------------|----------------------------------------------------------|----------------------------------------|
| 1      | AP Accountant  | Start                                                    | Step 2                                 |
| 2      | AP Accountant  | Identifies list of parties where WHT is required (M/A)   | Step 3                                 |
| 3      | AP Unit Head   | Review (M)                                               | Step 4                                 |
| 4      | AP Accountant  | Deduct WHT and record as liability (M)                   | Step 5                                 |
| 5      | AP Unit Head   | Review (M)                                               | Step 6                                 |
| 6      | Tax Manager    | Payment as per payment process                           | End                                    |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A[Start] --> B[Identifies list of parties where WHT is required (M/A)]
    B --> C[Review by AP Unit Head (M)]
    C --> D[Deduct WHT and record as liability (M)]
    D --> E[Review by AP Unit Head (M)]
    E --> F[Payment as per payment process]
    F --> G[End]
```

This representation covers all the roles, actions, and logic explicitly, connecting each step in the process flow.