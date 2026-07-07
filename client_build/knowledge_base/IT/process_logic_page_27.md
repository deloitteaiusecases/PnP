---
Department: IT
Source_Document: IT.pdf
Page_Number: 27
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Restoration Procedure

2. **Roles (Swimlanes)**:
   - IT Network and System Admin
   - IT & Cybersecurity Manager

3. **Steps in Markdown Table**:

   | Step # | Role                       | Action                                                                                  | Next Step/Logic                  |
   |--------|----------------------------|-----------------------------------------------------------------------------------------|----------------------------------|
   | 1      | IT Network and System Admin| Determine which server/application/data needs restoration. Complete the Restore Form.(M) | Approved                         |
   | 2      | IT & Cybersecurity Manager | Approved                                                                                | Yes: Step 3, No: Step 7          |
   | 3      | IT Network and System Admin| After final approval, plan the restoration process.(M)                                   | Step 4                           |
   | 4      | IT Network and System Admin| Perform restoration on the test server or path provided by the user.(M)                  | Step 5                           |
   | 5      | IT Network and System Admin| Check the completeness and accuracy of restored data.(M)                                 | Step 6                           |
   | 6      | IT Network and System Admin| Email IT Manager upon successful restoration test.(M)                                    | End                              |
   | 7      | IT Network and System Admin| Initiate Incident Management Procedure, conduct root cause analysis, and re-test if fails.(M) | End                           |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> A[Determine server/application for restoration. Complete Form.(M)]
    A --> B{Approved}
    B -->|Yes| C[Plan the restoration process.(M)]
    C --> D[Perform restoration on test server or provided path.(M)]
    D --> E[Check the completeness & accuracy of restored data.(M)]
    E --> F[Email IT Manager upon successful restoration test.(M)]
    F --> End
    B -->|No| G[Initiate Incident Management Procedure, conduct root cause analysis, and re-test if fails.(M)]
    G --> End
```
