---
Department: Cash Management
Source_Document: Cash Management.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: Issuance of LC

2. **Roles (Swimlanes)**:
   - Treasury Manager
   - GL Manager
   - Accounting Manager
   - CFO

3. **Steps in a Markdown Table**:

   | Step # | Role              | Action                                                                                      | Next Step/Logic         |
   |--------|-------------------|---------------------------------------------------------------------------------------------|-------------------------|
   | 1      | Treasury Manager  | Start                                                                                       | Step 2                  |
   | 2      | Treasury Manager  | Receive request from Procurement team for issuance of LC                                    | Step 3                  |
   | 3      | Treasury Manager  | Review the documentation (M)                                                                | Step 4                  |
   | 4      | Treasury Manager  | Submits the document for issuance of LCs (M)                                                | Step 5                  |
   | 5      | Treasury Manager  | Upon issuance of LCs by the bank, inform all stakeholders about the opening of the LC (M)   | Step 6                  |
   | 6      | GL Manager        | Records LC related expense in SAP, and update disclosures in financial statement (A/M)      | Decision (Approved?)    |
   | 7      | CFO               | Approved?                                                                                   | Yes: End; No: Step 8    |
   | 8      | Accounting Manager| Review and Approve                                                                          | Yes: End; No: Step 6    |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A[Start] --> B[Receive request from Procurement team for issuance of LC]
    B --> C[Review the documentation (M)]
    C --> D[Submits the document for issuance of LCs (M)]
    D --> E[Upon issuance of LCs by the bank, inform all stakeholders about the opening of the LC (M)]
    E --> F[Records LC related expense in SAP, and update disclosures in financial statement (A/M)]
    F --> G{Approved?}
    G -- Yes --> H[End]
    G -- No --> I[Review and Approve]
    I -- Yes --> H
    I -- No --> F
```

This structure captures the flow accurately, ensuring decisions lead back correctly to relevant steps.