---
Department: Financial Reporting
Source_Document: Financial Reporting.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### Flowchart Analysis

#### 1. Process Name
External audit or review and final approval of financial statements

#### 2. Roles (Swimlanes)
- GL Manager
- Accounting Manager
- CFO
- Auditors
- Board

#### 3. Steps in Markdown Table

| Step # | Role             | Action                                                        | Next Step/Logic                   |
|--------|------------------|---------------------------------------------------------------|-----------------------------------|
| 1      | GL Manager       | Coordinate with the auditor to provide necessary information and access to records | 2                                 |
| 2      | GL Manager       | Provide FS and all supporting document to external auditor for review/audit | 3                                 |
| 3      | Auditors         | Conduct audit/review, and communicate audit findings and/or adjustments | 4                                 |
| 4      | Accounting Manager | Review and evaluate findings/adjustment and prepare response | 5                                 |
| 5      | CFO              | Approve?                                                      | Yes: 6 / No: 3                    |
| 6      | Accounting Manager | Reshare updated FS post approval from CFO                   | 7                                 |
| 7      | Auditors         | Review and share draft audit report                          | 8                                 |
| 8      | Board            | Review and provide approval                                  | End                               |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1[The GL Manager, Accounting Manager and CFO will coordinate with the auditor to provide necessary information and access to records]
    A1 --> A2[Provide FS and all supporting document to external auditor for review/audit]
    A2 --> A3[Conduct audit/review, and communicate audit findings and/or adjustments]
    A3 --> A4[Review and evaluate findings/adjustment and prepare response]
    A4 --> A5{Approve?}
    A5 --> |Yes| A6[Reshare updated FS post approval from CFO]
    A5 --> |No| A3
    A6 --> A7[Review and share draft audit report]
    A7 --> A8[Review and provide approval]
    A8 --> End
```
