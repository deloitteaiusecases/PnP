---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 18
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:** Processing / Milling Operation
2. **Roles (Swimlanes):**
   - Mill Operator
   - QA Analyst
   - QA Specialist

3. **Steps in Markdown Table:**

| Step # | Role          | Action                                                                                                   | Next Step / Logic                                                                                                                         |
|--------|---------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Mill Operator | Identifies flour material unsuitable for immediate packaging                                             | Step 2                                                                                                                                   |
| 2      | QA Analyst    | Samples and tests rework for safety                                                                      | Step 3A: "Classifies approved rework" OR Step 3B: "Monitors product quality"                                                             |
| 3A     | QA Specialist | Classifies approved rework as: "Approved for Rework" / "Reject for Disposal". Updates SAP MM and QM records | If "Approved for Rework", then Step 4; If "Reject for Disposal", process ends                                                            |
| 3B     | QA Analyst    | Monitors product quality after rework addition (moisture, granulation, contamination)                    | Step 4                                                                                                                                   |
| 4      | QA Specialist | Rework tagging, approval, batch linkage, update final product batch traceability in SAP MM/QM             | End                                                                                                                                      |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    Start([Start]) --> |Identifies flour material unsuitable for immediate packaging| Step1[Mill Operator];
    Step1 --> |Samples and tests rework for safety| Step2[QA Analyst];
    Step2 --> |Classifies approved rework| Step3A[QA Specialist];
    Step2 --> |Monitors product quality| Step3B[QA Analyst];
    Step3A --> |Approved for Rework| Step4[QA Specialist];
    Step3A --> |Reject for Disposal| End([End]);
    Step3B --> Step4;
    Step4 --> |Rework tagging, approval, batch linkage, update traceability| End;
```

This outlines the logical flow and roles for the "Processing / Milling Operation" process.