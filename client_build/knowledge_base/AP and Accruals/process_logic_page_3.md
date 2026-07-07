---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name:
Issuance of debit note / receipt of credit note

#### 2. Roles (Swimlanes):
- Procurement Team
- AP Accountant
- AP Unit Head
- Accounting Manager / GL Manager

#### 3. Steps in a Markdown Table:

| Step # | Role                            | Action                                                                 | Next Step/Logic                                |
|--------|---------------------------------|------------------------------------------------------------------------|------------------------------------------------|
| 1      | AP Accountant                   | Identification of any discrepancy (M)                                  | 2                                              |
| 2      | AP Unit Head                    | Review the discrepancy (M)                                             | 3 if No; Approved Decision if Yes              |
| Decision| Accounting Manager / GL Manager | Approved?                                                              | 4 if Yes; 3 if No                              |
| 3      | AP Accountant                   | Request via email for issuance of new invoice or a credit note (M)     | 4                                              |
| 4      | Procurement Team                | Credit note or updated invoice is received from the supplier (M)       | 5                                              |
| 5      | AP Accountant                   | Record in SAP as per 'Invoice Processing Procedure' (A/M)              | End                                            |

#### 4. Logic in Mermaid.js:

```mermaid
graph TD;
    A(Start) --> B1[AP Accountant: Identification of any discrepancy (M)]
    B1 --> B2[AP Unit Head: Review the discrepancy (M)]
    B2 -->|No| C[AP Accountant: Request via email for issuance of new invoice or a credit note (M)]
    B2 -->|Yes| D(Approved?)
    D -->|Yes| E[Procurement Team: Credit note or updated invoice is received from the supplier (M)]
    D -->|No| C
    C --> E
    E --> F[AP Accountant: Record in SAP as per 'Invoice Processing Procedure' (A/M)]
    F --> G(End)
```
