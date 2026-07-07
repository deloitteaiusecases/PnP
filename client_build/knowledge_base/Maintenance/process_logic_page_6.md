---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

```markdown
### 1. Process Name
Work Order System

### 2. Roles (Swimlanes)
- Technician
- Maintenance

### 3. Steps in Markdown Table

| Step # | Role       | Action                                                                 | Next Step/Logic |
|--------|------------|------------------------------------------------------------------------|-----------------|
| 1      | Technician | Notification is raised for any maintenance need. (A)                   | Step 2          |
| 2      | Maintenance| Reviews notification and creates work order. (M)                       | Step 3          |
| 3      | Maintenance| Schedules work order, assigns resources, checks material availability, and ensures permits. (M) | Step 4          |
| 4      | Technician | Performs task as per scope and safety requirements. (M)                | Step 5          |
| 5      | Technician | Enters technical feedback, time spent, and materials used. (A)         | Step 6          |
| 6      | Maintenance| Verifies work completion, evaluates feedback, and closes work order in SAP. (A/M) | Step 7          |
| 7      | Technician | Tracks open, overdue, and rejected work orders and reports weekly. (A) | Step 8          |
| 8      | Maintenance| Engineers and managers review work order history, breakdown causes, and trends. (M) | End             |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A[Start] --> B[Notification is raised for any maintenance need. (A)]
    B --> C[Reviews notification and creates work order. (M)]
    C --> D[Schedules work order, assigns resources, checks material availability, and ensures permits. (M)]
    D --> E[Performs task as per scope and safety requirements. (M)]
    E --> F[Enters technical feedback, time spent, and materials used. (A)]
    F --> G[Verifies work completion, evaluates feedback, and closes work order in SAP. (A/M)]
    G --> H[Tracks open, overdue, and rejected work orders and reports weekly. (A)]
    H --> I[Engineers and managers review work order history, breakdown causes, and trends. (M)]
    I --> J[End]
```
