---
Department: IT
Source_Document: IT.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Emergency Incident Protocol Procedure

2. **Roles (Swimlanes)**:
   - Notifier
   - IT & Cybersecurity Manager
   - CFO
   - IT Network and Server Admin

3. **Steps in Markdown Table**

| Step # | Role                        | Action                                                                     | Next Step/Logic               |
|--------|-----------------------------|----------------------------------------------------------------------------|-------------------------------|
| 1      | Notifier                    | Immediately raise a request and document the urgency.                      | Step 2                        |
| 2      | IT & Cybersecurity Manager  | Determine the necessity for an emergency incident based on severity.       | Approval by CFO               |
| 3      | CFO                         | Approve                                                                    | Yes: Step 4 / No: End         |
| 4      | IT Network and Server Admin | Execute the incident response promptly following approval.                 | Step 5                        |
| 5      | IT Network and Server Admin | Maintain comprehensive records of the incident, including approvals and implementation details. | Step 6                        |
| 6      | IT Network and Server Admin | Evaluate the effectiveness of the emergency incident response and gather feedback. | End                           |

4. **Mermaid.js Code Block**

```mermaid
graph TD;
    Start --> A1;
    A1[Immediately raise a request and document the urgency] --> A2;
    A2[Determine the necessity for an emergency incident based on severity] --> B{Approve};
    B -- Yes --> C1[Execute the incident response promptly following approval];
    B -- No --> End;
    C1 --> C2[Maintain comprehensive records of the incident, including approvals and implementation details];
    C2 --> C3[Evaluate the effectiveness of the emergency incident response and gather feedback];
    C3 --> End;
```
