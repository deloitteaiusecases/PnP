---
Department: PPE, Intangibles, CWIP and ROU
Source_Document: PPE, Intangibles, CWIP and ROU.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

### Flowchart Analysis

1. **Process Name**: FA Capital work-in-progress
2. **Roles (Swimlanes)**:
   - User
   - GL Manager
   - Accounting Manager
   - Supply Chain P&P
   - Maintenance P&P

3. **Steps in Markdown Table**:

| Step # | Role              | Action                                                                 | Next Step/Logic                      |
|--------|-------------------|------------------------------------------------------------------------|--------------------------------------|
| 1      | User              | Initiate request duly approved by Department head for Asset under Construction (M) | Review and approve                  |
| 2      | GL Manager        | Review and approve                                                     | Yes: Initiate the request to create a unique FA ID in SAP (M/A)<br>No: Back to start |
| 3      | GL Manager        | Initiate the request to create a unique FA ID in SAP (M/A)             | Capitalization of expense on monthly basis to CWIP/AUC (A) |
| 4      | GL Manager        | Capitalization of expense on monthly basis to CWIP/AUC (A)             | CWIP Transfer to FA (A)              |
| 5      | GL Manager        | CWIP Transfer to FA (A)                                                | Yes: End<br>No: Approve             |
| 6      | GL Manager        | Approve                                                                | Yes: End<br>No: Review and approve  |
| 7      | Supply Chain P&P  | Generation of PO                                                       | Receipt of goods/service and recording of system generated entry for GR/IR |
| 8      | Supply Chain P&P  | Receipt of goods/service and recording of system generated entry for GR/IR | Arrange for completion certificate |
| 9      | Maintenance P&P   | Arrange for completion certificate and relevant documentation including approval from maintenance team (N) | CWIP Transfer to FA (A)              |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A(Start) --> B[Initiate request duly approved by Department head for Asset under Construction (M)];
    B --> C{Review and approve};
    C -- Yes --> D[Initiate the request to create a unique FA ID in SAP (M/A)];
    C -- No --> A;
    D --> E[Capitalization of expense on monthly basis to CWIP/AUC (A)];
    E --> F[CWIP Transfer to FA (A)];
    F -->|Yes| G(End);
    F -->|No| H{Approve};
    H -->|Yes| G;
    H -->|No| C;
    I[Generation of PO] --> J[Receipt of goods/service and recording of system generated entry for GR/IR];
    J --> K[Arrange for completion certificate and relevant documentation including approval from maintenance team (N)];
    K --> F;
```

This provides a clear, structured analysis of the flowchart, along with the Mermaid.js code to visualize it programmatically.