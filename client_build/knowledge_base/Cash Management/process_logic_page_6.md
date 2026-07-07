---
Department: Cash Management
Source_Document: Cash Management.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Recording of PO based and non-PO based payment.

2. **Roles (Swimlanes)**:
   - AP Accountant
   - AP Unit Head
   - Treasury Manager & Tax Manager
   - Accounting Manager

3. **Steps in Markdown Table**:

   | Step # | Role                        | Action                                              | Next Step/Logic            |
   |--------|-----------------------------|-----------------------------------------------------|----------------------------|
   | 1      | AP Unit Head                | Initiate the request for making payment over SAB bank account (A/M)    | Step 2                     |
   | 2      | AP Accountant               | Park the entry for payment to supplier (A/M)                           | Step 3                     |
   | 3      | AP Unit Head                | Review (A)                                           | Approval Decision          |
   | 4      | Treasury Manager & Tax Manager | Review (A)                                       | Approval Decision          |
   | 5      | Accounting Manager          | Decision: Approved?                                 | Yes: Step 6, No: Step 2    |
   | 6      | Accounting Manager          | Entry is posted in SAP (A)                           | End                        |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A(Start) --> B[Initiate the request for making payment over SAB bank account (A/M)]
    B --> C[Park the entry for payment to supplier (A/M)]
    C --> D[Review (A)]
    D --> E[Review (A)]
    E --> F{Approved?}
    F -- No --> C
    F -- Yes --> G[Entry is posted in SAP (A)]
    G --> H(End)
```

This flowchart captures the process for handling both PO based and non-PO based payments, involving verification and approval by different roles before the entry is finalized and posted in SAP.