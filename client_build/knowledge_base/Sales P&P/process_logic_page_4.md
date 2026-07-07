---
Department: Sales P&P
Source_Document: Sales P&P.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

#### 1. Process Name
- Sales Returns

#### 2. Roles (Swimlanes)
- Branch Sales Manager
- Sales Director
- Finance Manager

#### 3. Extracted Steps

| Step # | Role               | Action                                                                                     | Next Step/Logic            |
|--------|--------------------|--------------------------------------------------------------------------------------------|----------------------------|
| 1      | Branch Sales Manager  | Receives a request for stock return along with reasons, pictures, and quantities details from customer. (A) | Step 2                     |
| 2      | Branch Sales Manager  | Instructs the relevant Sales Specialist to prepare a brief stock verification and root cause analysis report. (M) | Step 3                     |
| 3      | Branch Sales Manager  | Reviews report and emails it with recommendations to relevant Sales Director keeping Sales Analyst in loop for coordination. (M) | Step 4 or Step 6.1         |
| 4      | Sales Director     | Reviews report along with Sales Analyst and shares it with Finance Manager, Trade Marketing Manager, and Quality Manager for review and approval. (M) | Step 5                     |
| 5      | Sales Director     | **Approved?**                                                                               | Yes: Step 5.1 / No: Step 5.2 |
| 5.1    | Sales Director     | Issue credit note and share it with Sales Analyst which will be emailed to the customer. (A) | End                        |
| 5.2    | Finance Manager    | Inform Sales Manager and either close the process or move to step 1                            | Step 1 if not closed       |
| 6.1    | Branch Sales Manager  | Collect documentary evidence, submit it to Sales Analyst and Finance Manager in case of expired stock. (M) | End (following Step 6.2)  |
| 6.2    | Branch Sales Manager  | In case of damaged stock, if Quality Manager approved it for return and repacking, stock will be dispatched to Warehouse/Factory. (M) | End                        |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A1[Start] --> B1[1. Receives request for stock return]
    B1 --> B2[2. Instructs Sales Specialist for verification report]
    B2 --> B3[3. Reviews report and email recommendations]
    B3 --> B4[4. Review report for approval]
    B3 --> C1[6.1 Case of expired stock]
    C1 --> C2[6.2 Damaged stock - dispatch to factory]
    C2 --> D1[End]
    B4 --> D1[5. Approved?]
    D1 -->|Yes| E1[5.1 Issue credit note]
    E1 --> F1[End]
    D1 -->|No| E2[5.2 Inform Sales Manager, close or retry]
    E2 --> B1[Retry if not closed]
```
