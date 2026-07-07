---
Department: PPE, Intangibles, CWIP and ROU
Source_Document: PPE, Intangibles, CWIP and ROU.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

Here's the analysis of the flowchart:

### 1. Process Name
- ROU and Lease Liability

### 2. Roles (Swimlanes)
- GL Manager
- Accounting Manager
- CFO

### 3. Steps in a Markdown Table
| Step # | Role              | Action                                                                           | Next Step/Logic                            |
|--------|-------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| 1      | GL Manager        | Identifies contract on which IFRS 16 guidance will be applied.                    | Step 2                                     |
|        |                   | Prepare computation of ROU and Lease Liability & share it for review & approval.  |                                            |
| 2      | Accounting Manager| Review (M)                                                                        | Approve? Yes: Step 3, No: Step 1           |
| 3      | CFO               | Approve                                                                           | Yes: Step 4, No: Step 1                    |
| 4      | GL Manager        | Parks the entry in the system and upload the IFRS 16 working (M)                  | Step 5                                     |
| 5      | Accounting Manager| Review and approve (A)                                                            | Step 6                                     |
| 6      | Accounting Manager| Payment of lease liability as per payment process                                 | End                                        |

### 4. Logic as a Mermaid.js Code Block
```mermaid
graph TD;
    Start --> A[Identifies contract on which IFRS 16 guidance will be applied]
    A --> B[Review (M)]
    B -->|Approve?| C{Yes}
    B -->|No| A
    C --> D[Parks the entry in the system and upload the IFRS 16 working (M)]
    D --> E[Review and approve (A)]
    E --> F[Payment of lease liability as per payment process]
    F --> End
```
This setup explicates the steps and decisions involved in the ROU and Lease Liability process.