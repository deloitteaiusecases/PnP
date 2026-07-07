---
Department: Revenue flow chart
Source_Document: Revenue flow chart.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

Certainly! Let's break down the flowchart.

### 1. Process Name
- **Recording of payment collection & revenue recognition (Credit Sale)**

### 2. Roles (Swimlanes)
- Sales & Collection Staff
- AR Team
- Warehouse Department (SCM P&P)
- GL and Accounting Manager

### 3. Steps in a Markdown Table

| Step # | Role                              | Action                                                          | Next Step/Logic                              |
|--------|-----------------------------------|-----------------------------------------------------------------|----------------------------------------------|
| 1      | Sales & Collection Staff          | Start                                                           | Step 2                                       |
| 2      | Warehouse Department (SCM P&P)    | After completion of weighing scale, auto-issuance of invoice and revenue recognition (A) | Step 3                                       |
| 3      | GL and Accounting Manager         | Review (M)                                                      | Step 4                                       |
| 4      | GL and Accounting Manager         | Approve                                                         | Yes: Step 5, No: Step 6                      |
| 5      | AR Team                           | Post approval, shares with Sales team for follow-up             | Step 8                                       |
| 6      | AR Team                           | Prepare listing of customers for follow-up purpose (M)          | Step 5                                       |
| 7      | Sales & Collection Staff          | Validate payment received and update in SAP for amount collected (M) | Step 8                                       |
| 8      | Sales & Collection Staff          | Auto generated entry for amount collection in SAP (A)           | Step 9                                       |
| 9      | AR Team                           | Review amount incorporated in SAP against the collection (M)    | End                                          |

### 4. Logic in Mermaid.js

```mermaid
graph TD;
    Start --> Step2;
    Step2[After completion of weighing scale, auto-issuance of invoice and revenue recognition (A)] --> Step3;
    Step3[Review (M)] --> Step4[Approve];
    Step4 -->|Yes| Step5[Post approval, shares with Sales team for follow-up];
    Step4 -->|No| Step6[Prepare listing of customers for follow-up purpose (M)];
    Step6 --> Step5;
    Step5 --> Step7[Validate payment received and update in SAP for amount collected (M)];
    Step7 --> Step8[Auto generated entry for amount collection in SAP (A)];
    Step8 --> Step9[Review amount incorporated in SAP against the collection (M)];
    Step9 --> End;
```

This representation will help visualize the process flow logically for further analysis.