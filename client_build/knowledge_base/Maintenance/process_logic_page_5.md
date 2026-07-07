---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

#### 1. Process Name
- **Maintenance Scheduling**

#### 2. Roles (Swimlanes)
- SAP PM Administrator
- Maintenance

#### 3. Steps in a Markdown Table

| Step # | Role               | Action                                                                                    | Next Step/Logic          |
|--------|--------------------|-------------------------------------------------------------------------------------------|--------------------------|
| 1      | SAP PM Administrator | Trigger scheduling process (M)                                                           | Step 2                   |
| 2      | Maintenance        | Extract list of open PM and CM work orders from SAP and validate for scope, parts, and permits (A) | Step 3                   |
| 3      | Maintenance        | Classify work orders by priority (P1–P5), duration, and resource requirement (M)          | Step 4                   |
| 4      | Maintenance        | Confirm equipment availability windows and integrate with production schedule (M)         | Step 5                   |
| 5      | Maintenance        | Create a comprehensive monthly schedule in SAP, with work orders (M)                      | Step 6                   |
| 6      | Maintenance        | Break down the monthly plan into weekly and daily task lists (A/M)                        | Step 7                   |
| 7      | Maintenance        | Reschedule deferred work and insert urgent/emergency jobs (M)                             | Step 8                   |
| 8      | Maintenance        | Share finalized monthly schedule with maintenance, production, and stores teams (A/M)     | Step 9                   |
| 9      | Maintenance        | Track completion status in SAP and record delays, early completions, or task deferrals (M)| Step 10                  |
| 10     | Maintenance        | Review KPIs and initiate improvement actions (M)                                          | End                      |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1[Trigger scheduling process (M)];
    A1 --> A2[Extract list of open PM and CM work orders from SAP and validate for scope, parts, and permits (A)];
    A2 --> A3[Classify work orders by priority (P1–P5), duration, and resource requirement (M)];
    A3 --> A4[Confirm equipment availability windows and integrate with production schedule (M)];
    A4 --> A5[Create a comprehensive monthly schedule in SAP, with work orders (M)];
    A5 --> A6[Break down the monthly plan into weekly and daily task lists (A/M)];
    A6 --> A7[Reschedule deferred work and insert urgent/emergency jobs (M)];
    A7 --> A8[Share finalized monthly schedule with maintenance, production, and stores teams (A/M)];
    A8 --> A9[Track completion status in SAP and record delays, early completions, or task deferrals (M)];
    A9 --> A10[Review KPIs and initiate improvement actions (M)];
    A10 --> End;
```

This setup provides a structured overview of the maintenance scheduling process, articulating each step and the responsible roles involved.