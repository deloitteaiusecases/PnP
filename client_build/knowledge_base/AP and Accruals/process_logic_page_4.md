---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Creditors Ageing

2. **Roles (Swimlanes)**:
   - SAP
   - AP Accountant
   - AP Unit Head/Accounting Manager
   - CFO

3. **Steps Table**:

| Step # | Role                            | Action                                                                       | Next Step/Logic              |
|--------|---------------------------------|------------------------------------------------------------------------------|------------------------------|
| 1      | AP Accountant                   | Extract the AP ageing report, which consists of supplier-wise and invoice-wise ageing (A) | Step 2                       |
| 2      | AP Unit Head/Accounting Manager | Review the report. (M)                                                       | Step 3                       |
| 3      | CFO                             | Discuss the Payment decision if due date is exceeded one month (M)            | End                          |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> Step1["Extract the AP ageing report, which consists of supplier-wise and invoice-wise ageing (A)"]
    Step1 --> Step2["Review the report. (M)"]
    Step2 --> Step3["Discuss the Payment decision if due date is exceeded one month (M)"]
    Step3 --> End
```
