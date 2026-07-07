---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### 1. Process Name
Emergency Response Procedure

### 2. Roles (Swimlanes)
- Technician
- Maintenance

### 3. Flowchart Steps

| Step # | Role        | Action                                                                                               | Next Step/Logic |
|--------|-------------|------------------------------------------------------------------------------------------------------|-----------------|
| 1      | Technician  | Any equipment failure or critical abnormality is immediately reported.                               | 2               |
| 2      | Maintenance | Evaluates the situation for safety and operational impact, then alerts concerned departments.         | 3               |
| 3      | Maintenance | Authorizes the technician to proceed, subject to safety clearance and risk checks.                   | 4               |
| 4      | Maintenance | Implement temporary isolation, tagging, or containment actions to stabilize the situation.           | 5               |
| 5      | Maintenance | Carry out necessary repair or workaround under supervisor oversight, ensuring safety protocols.      | 6               |
| 6      | Maintenance | After stabilizing, create a SAP work order for documentation and closure tracking.                  | 7               |
| 7      | Maintenance | Enters detailed feedback on actions taken, materials used, time, and observations.                   | 8               |
| 8      | Maintenance | Supervisor verifies completion, accuracy of feedback, and closes the emergency work order in SAP.    | 9               |
| 9      | Maintenance | Significant failures reviewed for root causes and potential preventive actions.                      | 10              |
| 10     | Maintenance | Adjust PM plans, inspection frequencies, or training needs based on learnings.                       | End             |

### 4. Mermaid.js Code Block

```mermaid
graph TD
    A(Start) --> B["1. Report failure/abnormality"]
    B --> C["2. Evaluate situation & alert departments"]
    C --> D["3. Authorize technician to proceed"]
    D --> E["4. Implement stabilization actions"]
    E --> F["5. Perform repair/workaround with oversight"]
    F --> G["6. Create SAP work order"]
    G --> H["7. Enter detailed feedback"]
    H --> I["8. Verify completion & close work order"]
    I --> J["9. Review significant failures"]
    J --> K["10. Adjust PM plans & training"]
    K --> L(End)
```
