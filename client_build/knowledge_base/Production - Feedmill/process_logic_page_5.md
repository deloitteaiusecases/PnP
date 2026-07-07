---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

Here's the analysis of the flowchart:

### Process Name:
- Grinding Process

### Roles (Swimlanes):
1. Shift Operator Milling / QA Analyst
2. Shift Operator / Mechanic
3. QA Specialist / Data Entry Operator

### Steps in a Markdown Table:

| Step # | Role                              | Action                                                               | Next Step/Logic                      |
|--------|-----------------------------------|----------------------------------------------------------------------|--------------------------------------|
| 1      | Shift Operator Milling / QA Analyst | Is equipment clean and functional?                                   | Yes: Step 2, No: Step 1.1            |
| 1.1    | Shift Operator Milling / QA Analyst | Clean/Repair, log deviation, then recheck (M)                        | Back to Step 1                       |
| 2      | Shift Operator Milling / QA Analyst | Is approved material issued and free from visible defects?           | Yes: Step 3, No: Step 2.1            |
| 2.1    | Shift Operator Milling / QA Analyst | Quarantine batch, notify QA/SCM (M)                                  | Back to Step 2                       |
| 3      | Shift Operator Milling / QA Analyst | Configure hammer speed, feed rate, screen size as per formula. Authorize settings by Supervisor (M) | Step 4                               |
| 4      | Shift Operator Milling / QA Analyst | Monitor for flow consistency, temperature, and abnormal noise (M)    | Step 5                               |
| 5      | Shift Operator Milling / QA Analyst | Is particle size within target (±10%)?                               | Yes: Step 5.1, No: Step 6            |
| 5.1    | Shift Operator Milling / QA Analyst | Continue grinding (A)                                                | End                                  |
| 6      | Shift Operator Milling / QA Analyst | Adjust feed rate, screen, or speed to correct deviation. Notify QA if deviation persists (M) | Back to Step 4                       |
| 7      | Shift Operator Milling / QA Analyst | Are weighing and monitoring instruments within calibration tolerance? | Yes: Step 8, No: Step 7.1            |
| 7.1    | Shift Operator Milling / QA Analyst | Isolate equipment and inform Maintenance (M)                         | Back to Step 4                       |
| 8      | Shift Operator / Mechanic           | Record any abnormal vibration, noise, temperature (M)                | Step 9                               |
| 9      | Shift Operator / Mechanic           | Stop mill, clean area, inspect screens/hammers (M)                   | Step 10                              |
| 10     | QA Specialist / Data Entry Operator | Any Deviation Noted?                                                 | Yes: Step 10.1, No: End              |
| 10.1   | QA Specialist / Data Entry Operator | Log deviation in SAP/QMS, conduct RCA and CAPA (M)                   | Back to Step 9                       |

### Mermaid.js Code Block:

```mermaid
graph TD;
    A[Start]
    A --> B{Is equipment clean and functional?}
    B -->|No| B1[Clean/Repair, log deviation, then recheck (M)]
    B1 --> B
    B -->|Yes| C{Is approved material issued and free from visible defects?}
    C -->|No| C1[Quarantine batch, notify QA/SCM (M)]
    C1 --> C
    C -->|Yes| D[Configure hammer speed, feed rate, screen size as per formula. Authorize settings by Supervisor (M)]
    D --> E[Monitor for flow consistency, temperature, and abnormal noise (M)]
    E --> F{Is particle size within target (±10%)?}
    F -->|Yes| F1[Continue grinding (A)]
    F1 --> Z[End]
    F -->|No| G[Adjust feed rate, screen, or speed to correct deviation. Notify QA if deviation persists (M)]
    G --> E
    E --> H{Are weighing and monitoring instruments within calibration tolerance?}
    H -->|No| H1[Isolate equipment and inform Maintenance (M)]
    H1 --> E
    H -->|Yes| I[Record any abnormal vibration, noise, temperature (M)]
    I --> J[Stop mill, clean area, inspect screens/hammers (M)]
    J --> K{Any Deviation Noted?}
    K -->|Yes| L[Log deviation in SAP/QMS, conduct RCA and CAPA (M)]
    L --> J
    K -->|No| Z
```
