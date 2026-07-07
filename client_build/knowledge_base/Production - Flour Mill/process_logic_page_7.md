---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

1. **Process Name:**
   - Raw Wheat Receipt into Silos

2. **Roles (Swimlanes):**
   - Silo Operator
   - QA Analyst

3. **Steps in Markdown Table:**

   | Step # | Role         | Action                                      | Next Step/Logic                                      |
   |--------|--------------|---------------------------------------------|------------------------------------------------------|
   | 1      | Silo Operator| Start                                       | Step 2                                               |
   | 2      | Silo Operator| Plan and Schedule Circulation               | Step 3                                               |
   | 3      | Silo Operator| Pre-Transfer Inspection                     | Step 4                                               |
   | 4      | Silo Operator| Validate Readiness?                         | Yes: Step 5<br>No: Step 6                            |
   | 5      | Silo Operator| Execute Circulation                         | Step 7                                               |
   | 6      | Silo Operator| Halt circulation                            | Step 3                                               |
   | 7      | QA Analyst   | Monitor Temperature & Moisture              | Step 8                                               |
   | 8      | QA Analyst   | Visual Inspection During Circulation        | Step 9                                               |
   | 9      | Silo Operator| Document Circulation Parameters in SAP      | Step 10                                              |
   | 10     | Silo Operator| End                                         | -                                                    |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    Start --> Step2
    Step2["Plan and Schedule Circulation"] --> Step3
    Step3["Pre-Transfer Inspection"] --> Step4
    Step4{"Validate Readiness?"} --> |Yes| Step5
    Step4 --> |No| Step6
    Step5["Execute Circulation"] --> Step7
    Step6["Halt circulation"] --> Step3
    Step7["Monitor Temperature & Moisture"] --> Step8
    Step8["Visual Inspection During Circulation"] --> Step9
    Step9["Document Circulation Parameters in SAP"] --> End
```