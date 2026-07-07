---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

1. **Process Name:** Raw Wheat Receipt into Silos - Quarantine & Rejection Handling

2. **Roles (Swimlanes):**
   - QA Analyst
   - QA Specialist
   - Department Manager
   - Data Entry Operator

3. **Steps in Markdown Table:**

| Step # | Role                | Action                                                    | Next Step/Logic                                              |
|--------|---------------------|-----------------------------------------------------------|--------------------------------------------------------------|
| 1      | QA Analyst          | Start                                                     | Quarantine batch if any test fails                           |
| 2      | QA Analyst          | Quarantine batch if any test fails                        | Perform secondary testing                                    |
| 3      | QA Specialist       | Perform secondary testing                                 | Root cause investigation                                     |
| 4      | QA Specialist       | Root cause investigation                                  | Decision?                                                    |
| 5      | Department Manager  | Decision?                                                 | If failure originates from vendor -> Return; If safe -> Reprocess; If toxic -> Dispose |
| 6      | Department Manager  | If failure originates from vendor then Return             | Document all actions in SAP                                  |
| 7      | Department Manager  | If safe and contamination can be removed then Reprocess   | Document all actions in SAP                                  |
| 8      | Department Manager  | If contamination is toxic or non-recoverable then dispose | Document all actions in SAP                                  |
| 9      | Data Entry Operator | Document all actions in SAP                               | End                                                          |

4. **Mermaid.js Code Block:**

```mermaid
graph TD
    A(Start) --> B{Quarantine batch if any test fails}
    B --> C(Perform secondary testing)
    C --> D(Root cause investigation)
    D --> E{Decision?}
    E --> F1[If failure originates from vendor then Return]
    E --> F2[If safe and contamination can be removed then Reprocess]
    E --> F3[If contamination is toxic or non-recoverable then dispose]
    F1 --> G(Document all actions in SAP)
    F2 --> G
    F3 --> G
    G --> H(End)
```
