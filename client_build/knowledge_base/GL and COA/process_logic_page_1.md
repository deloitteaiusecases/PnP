---
Department: GL and COA
Source_Document: GL and COA.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

1. **Process Name**: Opening of GL Accounts

2. **Roles (Swimlanes)**:
   - User from Accounting and Finance team
   - GL Manager
   - Accounting Manager

3. **Steps in Markdown Table**:

   | Step # | Role                           | Action                                                                                               | Next Step/Logic    |
   |--------|--------------------------------|------------------------------------------------------------------------------------------------------|--------------------|
   | 1      | User from Accounting and Finance team | Raise a request via email to open a new GL account as per 'GL opening template' (M)                   | Step 2             |
   | 2      | GL Manager                     | Review the request and provide feedback for approval or rejection to the Accounting Manager, including the reason for the decision. (M) | Approved?         |
   | 3      | GL Manager                     | The GL Manager to create a GL account in SAP, specifying the GL details, and share the final details with the Accounting Manager for review. (A/M) | Step 4            |
   | 4      | GL Manager                     | GL Manager to notify user via email, keep FP&A Manager informed (M)                                   | End                |
   | -      | Accounting Manager             | Approved?                                                                                            | Yes: Step 3 / No: End |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> A[Raise a request via email to open a new GL account as per 'GL opening template' (M)]
    A --> B[Review the request and provide feedback for approval or rejection to the Accounting Manager, including the reason for the decision. (M)]
    B --> C{Approved?}
    C -- Yes --> D[The GL Manager to create a GL account in SAP, specifying the GL details, and share the final details with the Accounting Manager for review. (A/M)]
    D --> E{Approved?}
    E -- Yes --> F[GL Manager to notify user via email, keep FP&A Manager informed (M)]
    E -- No --> End
    F --> End
    C -- No --> End
```
