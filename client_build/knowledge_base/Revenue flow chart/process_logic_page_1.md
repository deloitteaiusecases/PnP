---
Department: Revenue flow chart
Source_Document: Revenue flow chart.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

Sure, here’s the analysis:

### 1. Process Name:
Recording of payment collection & revenue recognition (Advance and Cash Sale)

### 2. Roles (Swimlanes):
- Sales & Collection Staff
- AR Team
- Warehouse Personnel (SCM PR)
- GL and Accounting Manager

### 3. Steps in Markdown Table:

| Step # | Role                          | Action                                                                                  | Next Step/Logic                                   |
|--------|-------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------|
| 1      | Sales & Collection Staff      | Validate payment received and update in SAP for amount collected (M)                    | Auto generated entry for amount collection in SAP (A) |
| 2      | AR Team                       | Review amount incorporated in SAP against the collection (M)                            | After completion of weighing scale, auto-issuance of invoice and revenue recognition entry (A) |
| 3      | Warehouse Personnel (SCM PR)  | After completion of weighing scale, auto-issuance of invoice and revenue recognition entry (A) | Review by GL and Accounting Manager (M)        |
| 4      | GL and Accounting Manager     | Review (M)                                                                              | End if Yes                                         |

### 4. Logic in Mermaid.js Code Block:

```mermaid
graph TD;
    Start --> A1[Sales & Collection Staff<br>Validate payment received and update in SAP for amount collected (M)];
    A1 --> B1[Auto generated entry for amount collection in SAP (A)];
    B1 --> C1[AR Team<br>Review amount incorporated in SAP against the collection (M)];
    C1 --> D1[Warehouse Personnel (SCM PR)<br>After completion of weighing scale, auto-issuance of invoice and revenue recognition entry (A)];
    D1 --> E1[GL and Accounting Manager<br>Review (M)];
    E1 -->|Yes| End;
```

This logic flow provides a clear structure for understanding the process and its dependencies among different roles.