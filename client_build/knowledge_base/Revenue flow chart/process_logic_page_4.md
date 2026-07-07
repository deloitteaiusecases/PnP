---
Department: Revenue flow chart
Source_Document: Revenue flow chart.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

#### 1. Process Name:
- Expected Credit Loss

#### 2. Roles (Swimlanes):
- GL Manager
- Accounting Manager
- ECL Consultant
- CFO

#### 3. Markdown Table:

| Step # | Role              | Action                                           | Next Step/Logic                 |
|--------|-------------------|--------------------------------------------------|---------------------------------|
| 1      | GL Manager        | Share data of AR Ageing, AR subledger            | Step 2                          |
| 2      | ECL Consultant    | Perform ECL working based on information shared  | Step 3                          |
| 3      | Accounting Manager| Review the working (M)                           | Approve?                        |
| 4      | Accounting Manager| Approve                                           | Yes -> Step 5, No -> Step 2     |
| 5      | Accounting Manager| Record the adjust entry in SAP (M)               | Step 6                          |
| 6      | CFO               | Review the adjustment based on approved ECL computation (A)| Approve?             |
| 7      | CFO               | Approve                                           | Yes -> End, No -> Step 2        |

#### 4. Mermaid.js Code Block:

```mermaid
graph TD
    A[Start] --> B[Share data of AR Ageing, AR subledger]
    B --> C[Perform ECL working based on information shared]
    C --> D[Review the working (M)]
    D -->|Yes| E[Record the adjust entry in SAP (M)]
    D -->|No| C
    E --> F[Review the adjustment based on approved ECL computation (A)]
    F -->|Yes| G[End]
    F -->|No| C
```

This breakdown captures the sequential flow and decision points within the process.