---
Department: Sales P&P
Source_Document: Sales P&P.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

Certainly! Here's the analysis of the flowchart:

### 1. Process Name
- Sales Planning and Forecast

### 2. Roles (Swimlanes)
- Senior Management
- Sales
- Finance
- CEO

### 3. Steps in a Markdown Table

| Step # | Role            | Action                                                                                      | Next Step/Logic        |
|--------|-----------------|---------------------------------------------------------------------------------------------|------------------------|
| 1      | Senior Management | Sends the Board approved strategic goals and plan to the Head of Sales. (M)               | Step 2                 |
| 2      | Sales            | Requests Head of Marketing for arranging Retail audit data. Collects market and competitors’ data. (M) | Step 3                 |
| 3      | Sales            | Sales directors prepare Sales plans and respective forecast. (M)                           | Step 4                 |
| 4      | Sales            | Discusses Plans and forecast with Head of Marketing. Submitted to CFO for review. (M)      | Step 5.1               |
| 5.1    | Finance          | Approval required?                                                                        | Yes: Step 6, No: Step 5 |
| 5      | Finance          | Reviews the Plan and Forecast and may request clarifications or revisions. (M)            | Step 3                 |
| 6      | CEO              | Final plan submitted to CEO for final sign off. (A)                                       | Step 6.1               |
| 6.1    | CEO              | Approved?                                                                                 | Yes: Step 7, No: Step 5 |
| 7      | CEO              | Plan is consolidated and submitted to Board for approval. (A/M)                           | End                    |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1[Sends the Board approved strategic goals and plan to the Head of Sales (M)]
    A1 --> A2[Requests Head of Marketing. (M)]
    A2 --> A3[Sales directors prepare Sales plans (M)]
    A3 --> A4[Discusses Plans and forecast. (M)]
    A4 --> D5.1{5.1 Approved?}
    D5.1 -- Yes --> E6[Final plan submitted to CEO for sign off (A)]
    D5.1 -- No --> B5[Reviews Plan and may request revisions (M)]
    B5 --> A3
    E6 --> F6.1{6.1 Approved?}
    F6.1 -- Yes --> G7[Plan is consolidated and submitted to Board (A/M)]
    F6.1 -- No --> B5
    G7 --> End
```

This analysis captures the flow of steps and decision points as outlined in the flowchart.