---
Department: PPE, Intangibles, CWIP and ROU
Source_Document: PPE, Intangibles, CWIP and ROU.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name
- FA Unique ID, Procurement and Tracking

#### 2. Roles (Swimlanes)
- User
- FA Manager
- Accounting Manager
- Supply Chain P&P
- Maintenance P&P

#### 3. Steps in Markdown Table

| Step # | Role              | Action                                                                                     | Next Step/Logic                   |
|--------|-------------------|--------------------------------------------------------------------------------------------|-----------------------------------|
| 1      | User              | Initiate request duly approved by Department head for purchase the FA (M)                   | Decision: FA Manager Review       |
| 2      | FA Manager        | Review and approve                                                                         | Yes: Initiate in SAP \| No: Start |
| 3      | FA Manager        | Initiate the request to create a unique FA ID in SAP (M/A)                                | Accounting Manager PO Generation  |
| 4      | Accounting Manager| Generation of PO                                                                            | Supply Chain P&P Receipt of FA    |
| 5      | Supply Chain P&P  | Receipt of FA                                                                               | Maintenance P&P FA Tagging        |
| 6      | Maintenance P&P   | FA Tagging, FA Movement                                                                     | FA Manager Updates                |
| 7      | FA Manager        | Updates the FA movement and maintained the FAR, and shares with GL Manager for review (A/M) | Decision: Approve                 |
| 8      | FA Manager        | Approve                                                                                     | Yes: End \| No: Update Movement   |

#### 4. Logic in Mermaid.js

```mermaid
graph TD
    A[Start] --> B{Initiate request duly approved by Department head for purchase the FA (M)}
    B -->|No| A
    B -->|Yes| C[Review and approve]
    C -->|No| A
    C -->|Yes| D[Initiate the request to create a unique FA ID in SAP (M/A)]
    D --> E[Generation of PO]
    E --> F[Receipt of FA]
    F --> G[FA Tagging, FA Movement]
    G --> H[Updates the FA movement and maintained the FAR, and shares with GL Manager for review (A/M)]
    H --> I{Approve}
    I -->|Yes| J[End]
    I -->|No| G
```