---
Department: IT
Source_Document: IT.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: Notification Procedure

2. **Roles (Swimlanes)**:
   - Notifier
   - DR Plan Coordinator
   - Damage Assessment Team
   - CFO
   - Recovery Team

3. **Steps and Actions**:

| Step # | Role                   | Action                                                                 | Next Step/Logic       |
|--------|------------------------|------------------------------------------------------------------------|-----------------------|
| 1      | Notifier               | Inform DR Plan Coordinator about the disaster event (M)                | Step 2                |
| 2      | DR Plan Coordinator    | Assess whether the event/disaster is temporary or permanent (M)        | Step 3                |
| 3      | DR Plan Coordinator    | Inform Damage Assessment Team (DAT)                                    | Step 4                |
| 4      | Damage Assessment Team | DAT to follow Damage Assessment procedure (M)                          | Step 5                |
| 5      | Damage Assessment Team | Inform damage assessment details to DR Plan Coordinator (M)            | Step 6                |
| 6      | DR Plan Coordinator    | Inform CFO about DR Plan activation (M)                                | Step 7                |
| 7      | CFO                    | Inform CEO about DR Plan activation (M)                                | Step 8                |
| 8      | DR Plan Coordinator    | Inform Recovery Team to activate IT DR Plan (M)                       | Step 9                |
| 9      | Recovery Team          | Communicate the Recovery Status to DR Plan Coordinator every 1 hour (M)| Step 10               |
| 10     | Recovery Team          | Communicate to DR Plan Coordinator about the Recovery process completion and service/process is back online (M) | Step 11 |
| 11     | DR Plan Coordinator    | Inform CFO about recovery completion (M)                               | Step 12               |
| 12     | CFO                    | Inform CEO about recovery completion (M)                               | End                   |

4. **Mermaid.js Code (graph TD)**:
```mermaid
graph TD;
    Start --> A1[Inform DR Plan Coordinator about the disaster event (M)]
    A1 --> A2[Assess whether the event/disaster is temporary or permanent (M)]
    A2 --> A3[Inform Damage Assessment Team (DAT)]
    A3 --> A4[DAT to follow Damage Assessment procedure (M)]
    A4 --> A5[Inform damage assessment details to DR Plan Coordinator (M)]
    A5 --> A6[Inform CFO about DR Plan activation (M)]
    A6 --> C1[Inform CEO about DR Plan activation (M)]
    A6 --> A8[Inform Recovery Team to activate IT DR Plan (M)]
    C1 --> A8
    A8 --> R1[Communicate the Recovery Status to DR Plan Coordinator every 1 hour (M)]
    R1 --> R2[Communicate to DR Plan Coordinator about the Recovery process completion and service/process is back online (M)]
    R2 --> A11[Inform CFO about recovery completion (M)]
    A11 --> C2[Inform CEO about recovery completion (M)]
    C2 --> End
```