---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 18
Last_Updated: 2026-03-16
---

1. **Process Name**: Maintenance KPIs

2. **Roles (Swimlanes)**:
   - Maintenance
   - SAP PM Administrator

3. **Steps in a Markdown Table**:

| Step # | Role                  | Action                                                                                     | Next Step/Logic |
|--------|-----------------------|--------------------------------------------------------------------------------------------|-----------------|
| 1      | Maintenance           | Develop and approve KPI list aligned with global best practices and plant priorities. (M)   | Step 2          |
| 2      | Maintenance           | Link each KPI to a primary and supporting role using the KPI Responsibility Matrix. (M)     | Step 3          |
| 3      | SAP PM Administrator  | Ensure required fields (e.g., failure codes, work order types) are standardized and mapped. (M) | Step 4          |
| 4      | SAP PM Administrator  | Ensure asset hierarchy, work centers, and task lists are kept current to support reliable KPI extraction. (M) | Step 5          |
| 5      | Maintenance           | Train technicians and supervisors to enter complete, timely, and structured feedback. (M)  | Step 6          |
| 6      | SAP PM Administrator  | Check accuracy of core SAP entries that feed into KPI formulas (e.g., downtime, completion codes). (M) | Step 7  |
| 7      | Maintenance           | Refine formulas, targets, and tracking methodology based on changes in plant strategy or systems. (M) | End         |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> A[Develop and approve KPI list aligned with global best practices and plant priorities. (M)]
    A --> B[Link each KPI to a primary and supporting role using the KPI Responsibility Matrix. (M)]
    B --> C[Ensure required fields (e.g., failure codes, work order types) are standardized and mapped. (M)]
    C --> D[Ensure asset hierarchy, work centers, and task lists are kept current to support reliable KPI extraction. (M)]
    D --> E[Train technicians and supervisors to enter complete, timely, and structured feedback. (M)]
    E --> F[Check accuracy of core SAP entries that feed into KPI formulas (e.g., downtime, completion codes). (M)]
    F --> G[Refine formulas, targets, and tracking methodology based on changes in plant strategy or systems. (M)]
    G --> End
```
