---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 10
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name:**
   - Lubrication Management

2. **Roles (Swimlanes):**
   - Maintenance
   - Technician
   - Storekeeper

3. **Steps in a Markdown Table:**

| Step # | Role        | Action                                                                                     | Next Step/Logic |
|--------|-------------|--------------------------------------------------------------------------------------------|-----------------|
| 1      | Maintenance | Ensure lubrication points, frequency, and lubricant specifications are aligned with OEM and internal best practices. | 2               |
| 2      | Maintenance | Planner links pre-approved lubrication task lists and checklists to preventive maintenance schedules in SAP PM. | 3               |
| 3      | Technician  | Work orders are automatically generated from SAP PM schedules and assigned to certified technicians. | 4               |
| 4      | Technician  | Technicians carry out lubrication tasks using standard methods and safety protocols, referring to SAP checklists. | 5               |
| 5      | Technician  | Technicians document completed tasks, lubricant quantities used, and any abnormalities observed. | 6               |
| 6      | Maintenance | Supervisors verify task completion, quality of feedback, and raise work notifications if defects are found. | 8               |
| 7      | Storekeeper | Lubricant usage and stock levels are tracked digitally, with automated alerts for reorder thresholds. | 8               |
| 8      | Maintenance | Lubrication effectiveness is reviewed using SAP-generated KPIs and failure trend analysis.       | End             |

4. **Mermaid.js Logic Diagram:**

```mermaid
graph TD;
    A[Start] --> B1[1. Ensure lubrication points, frequency, and lubricant specifications aligned with best practices. (M)]
    B1 --> B2[2. Planner links pre-approved lubrication task lists to SAP PM schedules. (M)]
    B2 --> C1[3. Work orders generated and assigned to technicians. (A)]
    C1 --> C2[4. Technicians carry out lubrication tasks. (A)]
    C2 --> C3[5. Technicians document tasks and observations. (A/M)]
    C3 --> D1[6. Supervisors verify task completion and raise notifications. (M)]
    D1 --> E[8. Lubrication effectiveness reviewed using KPIs. (M)]
    D2[7. Track lubricant usage and stock levels. (M)] --> E
    E --> F[End]
```

This representation captures the logic and flow of the lubrication management process, ensuring clarity and traceability of each step in the procedure.