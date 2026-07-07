---
Department: IT
Source_Document: IT.pdf
Page_Number: 32
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Antivirus Management Procedure

2. **Roles (Swimlanes)**:
   - IT Network and Server Admin

3. **Markdown Table**

```markdown
| Step # | Role                     | Action                                                                 | Next Step/Logic                                                 |
|--------|--------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------|
| 1      | IT Network and Server Admin | All server and systems will be installed with Bitdefender Antivirus. (A/M) | Step 2                                                          |
| 2      | IT Network and Server Admin | Antivirus server will push definition updates to all servers and systems daily. (A) | Step 3                                                          |
| 3      | IT Network and Server Admin | Identify servers and systems not installed with antivirus or updated with the latest definition file daily. (A/M) | Step 4                                                          |
| 4      | IT Network and Server Admin | Generate a list of servers and systems not installed with the latest antivirus software and updates monthly, sharing the report with IT Manager. (A/M) | Step 5                                                          |
| 5      | IT Network and Server Admin | Ensure uninstalling or disabling antivirus software is disabled. Antivirus will be password protected. (A/M) | Step 6                                                          |
| 6      | IT Network and Server Admin | Any changes to the antivirus server will be implemented through the change management procedure. (M) | Step 7                                                          |
| 7      | IT Network and Server Admin | Schedule automatic antivirus scans for all servers, desktops, and laptops every Wednesday. (A) | Step 8                                                          |
| 8      | IT Network and Server Admin | Check schedule scan results every Thursday and send the results to the IT Manager. (A/M) | End                                                             |
```

4. **Mermaid.js Code Block**

```mermaid
graph TD;
    A(Start) --> B[1. All server and systems will be installed with Bitdefender Antivirus. (A/M)];
    B --> C[2. Antivirus server will push definition updates to all servers and systems daily. (A)];
    C --> D[3. Identify servers and systems not installed with antivirus or updated with the latest definition file daily. (A/M)];
    D --> E[4. Generate a list of servers and systems not installed with the latest antivirus software and updates monthly, sharing the report with IT Manager. (A/M)];
    E --> F[5. Ensure uninstalling or disabling antivirus software is disabled. Antivirus will be password protected. (A/M)];
    F --> G[6. Any changes to the antivirus server will be implemented through the change management procedure. (M)];
    G --> H[7. Schedule automatic antivirus scans for all servers, desktops, and laptops every Wednesday. (A)];
    H --> I[8. Check schedule scan results every Thursday and send the results to the IT Manager. (A/M)];
    I --> J(End);
```
