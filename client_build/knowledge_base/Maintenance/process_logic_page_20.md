---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 20
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name
- Root Cause Analysis

#### 2. Roles (Swimlanes)
- Maintenance
- RCA Team
- SAP PM Administrator

#### 3. Steps in a Markdown Table

| Step # | Role                | Action                                                                 | Next Step/Logic        |
|--------|---------------------|------------------------------------------------------------------------|------------------------|
| Start  | Maintenance         | Start                                                                  | 1                      |
| 1      | Maintenance         | Director establish thresholds for when RCA is mandatory.               | 2                      |
| 2      | Maintenance         | Manager design standard forms for RCA documentation.                   | 3                      |
| 3      | Maintenance         | Conduct workshops on RCA methods.                                      | 4                      |
| 4      | Maintenance         | Assign a facilitator and team when triggered.                          | 5                      |
| 5      | RCA Team            | Facilitate analysis, document findings, and identify root causes.      | 6                      |
| 6      | RCA Team            | Translate causes into actions with deadlines and owners.               | 7                      |
| 7      | Maintenance         | Supervisor track action progress.                                      | 8                      |
| 8      | Maintenance         | Director verify corrective actions after a defined period.             | 9                      |
| 9      | Maintenance         | Manager include RCA cases in KPI review meetings.                      | 10                     |
| 10     | SAP PM Administrator| Archive all RCA reports.                                               | End                    |
| End    | SAP PM Administrator| End                                                                    |                        |

#### 4. Mermaid.js Code Block

```mermaid
graph TD
    Start --> step1["1. Director establish thresholds for when RCA is mandatory."]
    step1 --> step2["2. Manager design standard forms for RCA documentation."]
    step2 --> step3["3. Conduct workshops on RCA methods."]
    step3 --> step4["4. Assign a facilitator and team when triggered."]
    step4 --> step5["5. Facilitate analysis, document findings, and identify root causes."]
    step5 --> step6["6. Translate causes into actions with deadlines and owners."]
    step6 --> step7["7. Supervisor track action progress."]
    step7 --> step8["8. Director verify corrective actions after a defined period."]
    step8 --> step9["9. Manager include RCA cases in KPI review meetings."]
    step9 --> step10["10. Archive all RCA reports."]
    step10 --> End
```