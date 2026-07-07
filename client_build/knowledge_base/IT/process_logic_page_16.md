---
Department: IT
Source_Document: IT.pdf
Page_Number: 16
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

#### 1. Process Name:
- Access Right Review - Server and Application Procedure

#### 2. Roles (Swimlanes):
- IT Network and Server Admin
- Application/Server User

#### 3. Steps in a Markdown Table:

| Step # | Role                           | Action                                                                                  | Next Step/Logic      |
|--------|--------------------------------|-----------------------------------------------------------------------------------------|----------------------|
| 1      | IT Network and Server Admin    | Generate list of users having access to servers/applications. (A/M)                      | Step 2               |
| 2      | IT Network and Server Admin    | Share the user access list with the concerned owners of the server/application for review (M) | Step 3               |
| 3      | Application/Server User        | Review the user access on the servers/applications and inform the updates/modifications to the server/application administrator. (M) | Step 4               |
| 4      | IT Network and Server Admin    | Update the user access list and send the final revised list for final review and approval. (M) | Decision: Approved?  |
| 5      | Decision                       | Approved                                          | Yes: Step 6 / No: Step 4      |
| 6      | IT Network and Server Admin    | Repeat the review process every six months for any access change, resigned employees, and elevated privileges. (M) | Step 7               |
| 7      | IT Network and Server Admin    | Maintain and update the user access review list as a digital record and retain the documents for 3 years. (M) | Step 8               |
| 8      | IT Network and Server Admin    | Shred any physical documents using a shredder after 3 years. (M)                          | End                  |

#### 4. Logic as a Mermaid.js Code Block:

```mermaid
graph TD;
    A[Start] --> B[1. Generate list of users having access to servers/applications. (A/M)]
    B --> C[2. Share the user access list with the concerned owners of the server/application for review. (M)]
    C --> D[3. Review the user access on the servers/applications and inform the updates/modifications to the server/application administrator. (M)]
    D --> E[4. Update the user access list and send the final revised user access list for final review and approval. (M)]
    E --> F{Approved?}
    F -->|No| E
    F -->|Yes| G[6. Repeat the review process every six months for any access change, resigned employees, and elevated privileges. (M)]
    G --> H[7. Maintain and update the user access review list as a digital record and retain the documents for 3 years. (M)]
    H --> I[8. Shred any physical documents using a shredder after 3 years. (M)]
    I --> J[End]
```
