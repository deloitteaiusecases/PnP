---
Department: IT
Source_Document: IT.pdf
Page_Number: 26
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:**
   - SAP Servers Backup Procedure

2. **Roles (Swimlanes):**
   - IT Network and System Admin

3. **Markdown Table:**

| Step # | Role                     | Action                                                                                                         | Next Step/Logic        |
|--------|--------------------------|----------------------------------------------------------------------------------------------------------------|------------------------|
| 1      | IT Network and System Admin | Determine which SAP servers and application data need to be backed up. (M)                                       | Step 2                 |
| 2      | IT Network and System Admin | Choose between Incremental, Full, or Snapshot backups for selected SAP servers/application data. (M)            | Step 3                 |
| 3      | IT Network and System Admin | Set up backups on Fujitsu storage and Tape Library storage according to the schedule in the backup and restore form. (M) | Step 4                 |
| 4      | IT Network and System Admin | Review backup logs daily at 10:00 am for the previous day's backups. (M)                                        | Step 5                 |
| 5      | IT Network and System Admin | Analyze logs and reinitiate backup or contact Fujitsu support for resolving issues. If the same backup job fails for two consecutive schedules, inform the IT Manager, and initiate the Incident Management Procedure (M) | End                    |

4. **Mermaid.js Code Block:**

```mermaid
graph TD
    A[Start] --> B[Determine which SAP servers and application data need to be backed up. (M)]
    B --> C[Choose between Incremental, Full, or Snapshot backups for selected SAP servers/application data. (M)]
    C --> D[Set up backups on Fujitsu storage and Tape Library storage according to the schedule in the backup and restore form. (M)]
    D --> E[Review backup logs daily at 10:00 am for the previous day's backups. (M)]
    E --> F[Analyse logs and reinitiate backup or contact Fujitsu support for resolving issues.]
    F -->|If the same backup job fails for two consecutive schedules| G[Inform the IT Manager and initiate the Incident Management Procedure (M)]
    F -->|If resolved or no consecutive failures| H[End]
```
