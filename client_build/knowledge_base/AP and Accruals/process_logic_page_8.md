---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 8
Last_Updated: 2026-03-16
---

Sure, here's the analysis of the flowchart:

### 1. Process Name
- Accrual Management – non-PO based approvals

### 2. Roles (Swimlanes)
- GL Manager
- Accounting Manager

### 3. Steps in Markdown Table

| Step # | Role             | Action                                                                                      | Next Step/Logic          |
|--------|------------------|---------------------------------------------------------------------------------------------|--------------------------|
| Start  | GL Manager       | Start                                                                                       | Step 1                   |
| 1      | GL Manager       | Gather essential data for calculating accrual provisions (M)                                | Step 2                   |
| 2      | GL Manager       | Calculate accrual and upload the working on SAP and parks the accrual entry in the system (M) | Step 3                   |
| 3      | Accounting Manager | Review and Approve (A)                                                                      | Step 4                   |
| 4      | GL Manager       | Reverse the accrual and upload the working on SAP and parks the accrual entry in the system (M) | Step 5                   |
| 5      | Accounting Manager | Review and Approve (M)                                                                      | End                      |
| End    |                  | End                                                                                         |                          |

### 4. Logic in Mermaid.js Code Block

```mermaid
graph TD
    A[Start] --> B[Gather essential data for calculating accrual provisions (M)]
    B --> C[Calculate accrual and upload the working on SAP and parks the accrual entry in the system (M)]
    C --> D[Review and Approve (A)]
    D --> E[Reverse the accrual and upload the working on SAP and parks the accrual entry in the system (M)]
    E --> F[Review and Approve (M)]
    F --> G[End]
```

This diagram represents the steps and roles involved in the accrual management process for non-purchase order-based approvals.