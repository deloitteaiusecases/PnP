---
Department: IT
Source_Document: IT.pdf
Page_Number: 23
Last_Updated: 2026-03-16
---

### Flowchart Analysis

1. **Process Name**: Media Disposal Procedure

2. **Roles (Swimlanes)**:
   - Information Owner
   - Line Manager
   - IT Network and Server Admin
   - IT & Cybersecurity Manager
   - CFO
   - Finance

3. **Steps in Markdown Table**:

| Step # | Role                       | Action                                                                 | Next Step/Logic                                 |
|--------|----------------------------|------------------------------------------------------------------------|-------------------------------------------------|
| 1      | Information Owner          | Identify information for disposal and fill Media Disposal Form if needed.| Proceed to Approval by Line Manager             |
| 2      | Line Manager               | Approved?                                                              | Yes: IT Network and Server Admin Approval; No: End |
| 3      | IT Network and Server Admin| Dispose of document/media in the presence of Information Owner.        | End                                             |
| 4      | IT Network and Server Admin| Approved?                                                              | Yes: IT & Cybersecurity Manager Approval; No: End|
| 5      | IT & Cybersecurity Manager | Approved?                                                              | Yes: CFO Approval; No: End                      |
| 6      | CFO                        | Approved?                                                              | Yes: Update Asset Inventory; No: End            |
| 7      | Finance                    | Update the asset inventory for backup media.                           | End                                             |
| 8      | Finance                    | Maintain Disposal Media form for 3 years.                              | End                                             |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> A1[Info Owner: Fill Media Disposal Form]
    A1 --> B1{Line Manager: Approved?}
    B1 -- Yes --> C1{IT Network/Admin: Approved?}
    C1 -- Yes --> D1{IT & Cybersecurity Manager: Approved?}
    D1 -- Yes --> E1{CFO: Approved?}
    E1 -- Yes --> F1[Finance: Update Asset Inventory]
    F1 --> G[End]
    C1 -- No --> G
    D1 -- No --> G
    E1 -- No --> G
    B1 -- No --> G
    C1 -- Yes --> C2[Dispose of document/media]
    C2 --> H[Finance: Maintain Disposal Media form for 3 years]
    H --> G
```

This provides a structured overview of the process with decision points explicitly traced back to the relevant steps.