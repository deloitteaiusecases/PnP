---
Department: Financial Reporting
Source_Document: Financial Reporting.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

#### 1. Process Name:
- Trial-balance closure and preparation of financial statement

#### 2. Roles (Swimlanes):
- GL Manager
- Accounting Manager
- AP Accountant
- AP Unit Head Treasury & Tax Manager
- Accounting Manager (Duplicate)

#### 3. Steps in a Markdown Table:

| Step # | Role                | Action                                                                                       | Next Step/Logic                  |
|--------|---------------------|----------------------------------------------------------------------------------------------|----------------------------------|
| 1      | GL Manager          | Extract TB, perform pre-closure checklist, and prepare financial statement (A/M)             | Step 2                           |
| 2      | GL Manager          | Updated FS, prepare detailed schedule and perform variance analysis (M)                      | Step 3                           |
| 3      | Accounting Manager  | Review and provide feedback (M)                                                              | Step 4                           |
| 4      | Accounting Manager  | Review and share with senior management (M)                                                  | End                              |

#### 4. Logic as Mermaid.js Code Block:

```mermaid
graph TD;
    Start --> A[Extract TB, perform pre-closure checklist, and prepare financial statement (A/M)]
    A --> B[Updated FS, prepare detailed schedule and perform variance analysis (M)]
    B --> C[Review and provide feedback (M)]
    C --> D[Review and share with senior management (M)]
    D --> End
```