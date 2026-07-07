---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

Sure, let's analyze the flowchart:

### 1. Process Name:
Preventive Maintenance

### 2. Roles (Swimlanes):
- Maintenance
- Planner
- Technician

### 3. Extracted Steps into Markdown Table:

```markdown
| Step # | Role       | Action                                                                                                 | Next Step/Logic                  |
|--------|------------|--------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Maintenance| Develop PM strategies, task lists, frequencies, and parts required for each asset class in SAP. (M)    | Step 2                           |
| 2      | Planner    | Run SAP-based forecast of due preventive tasks for the upcoming month. (M)                             | Step 3                           |
| 3      | Planner    | Review resource availability and production constraints; propose the detailed PM schedule (M)           | Step 4                           |
| 4      | Planner    | Present the proposed PM schedule in the monthly S&OP meeting for alignment and approval. (M)           | Step 5                           |
| 5      | Planner    | Ensure the schedule is formally approved; any changes/deferrals authorized and recorded in SAP (M)     | Step 6                           |
| 6      | Planner    | Release work orders for all approved tasks through the SAP PM module. (M)                              | Step 7                           |
| 7      | Technician | Carry out maintenance work as per work order details, task lists, and checklists. (M)                  | Step 8                           |
| 8      | Technician | Enter findings, time confirmations, spares used, and any anomalies into SAP (A/M)                      | Step 9                           |
| 9      | Maintenance| Track completion % of PM tasks, identify deferrals, and analyze root causes. (M)                       | Step 10                          |
| 10     | Maintenance| Report key metrics in monthly management reviews. (M)                                                  | End                              |
```

### 4. Logic as a Mermaid.js Code Block:

```mermaid
graph TD;
    A(Start) --> B[1. Develop PM strategies, task lists, frequencies, and parts in SAP. (M)]
    B --> C[2. Run SAP-based forecast of due preventive tasks for the upcoming month. (M)]
    C --> D[3. Review resource availability and propose the PM schedule (M)]
    D --> E[4. Present proposed PM schedule for alignment and approval (M)]
    E --> F[5. Ensure the schedule is approved, changes are authorized, and recorded in SAP (M)]
    F --> G[6. Release work orders for all approved tasks through SAP PM module. (M)]
    G --> H[7. Carry out maintenance work as per work order details (M)]
    H --> I[8. Enter findings, time confirmations, spares used, and anomalies into SAP (A/M)]
    I --> J[9. Track completion %, identify deferrals, analyze root causes (M)]
    J --> K[10. Report key metrics in monthly management reviews. (M)]
    K --> L(End)
```

This analysis breaks down the flowchart into a structured format, detailing each step, the responsible role, and the subsequent actions flow.