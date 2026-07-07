---
Department: Cash Management
Source_Document: Cash Management.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: Recording of Petty Cash

2. **Roles (Swimlanes)**:
   - User
   - Petty Cash Custodian
   - AP Accountant
   - AP Unit Head & Tax Manager
   - Accounting Manager

3. **Markdown Table of Steps**:

| Step # | Role                          | Action                                                           | Next Step/Logic                      |
|--------|-------------------------------|------------------------------------------------------------------|--------------------------------------|
| 1      | User                          | Start                                                            | 2                                    |
| 2      | User                          | Initiate request duly approved by Department head and Procurement team (M) | 3 (if Yes), 2 (if No)               |
| 3      | User                          | Submits invoice and necessary documents (M)                      | 4                                    |
| 4      | Petty Cash Custodian          | Review and approve                                               | 5 (if Yes), 2 (if No)               |
| 5      | Petty Cash Custodian          | Payment to supplier for petty expense (M)                        | 6                                    |
| 6      | Petty Cash Custodian          | Validate the documents (M)                                       | 7                                    |
| 7      | AP Accountant                 | Records entry for pre-payment (M/A)                              | 9                                    |
| 8      | AP Accountant                 | Records entry for expense booking (A)                            | 9                                    |
| 9      | AP Unit Head & Tax Manager    | Review (A)                                                       | 10                                   |
| 10     | AP Unit Head & Tax Manager    | Approve?                                                         | 11 (if Yes), 9 (if No)              |
| 11     | Accounting Manager            | End                                                              | -                                    |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A1[Start] --> A2[Initiate request approved (M)]
    A2 -->|Yes| A3[Submits invoice (M)]
    A2 -->|No| A2
    A3 --> B1[Review and approve]
    B1 -->|Yes| B2[Payment to supplier (M)]
    B1 -->|No| A2
    B2 --> B3[Validate documents (M)]
    B3 --> C1[Records entry for pre-payment (M/A)]
    C1 --> C2[Records entry for expense booking (A)]
    C2 --> D1[Review (A)]
    D1 --> D2{Approve?}
    D2 -->|Yes| E1[End]
    D2 -->|No| D1
```

This analysis extracts the key components of the flowchart for better understanding and implementation in AI or automated processes.