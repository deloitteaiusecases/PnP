---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 5
Last_Updated: 2026-03-16
---

1. **Process Name:**
   - Stock Replenishment Process

2. **Roles (Swimlanes):**
   - SC Material Planner
   - DC Officer / WH Section Head
   - SC Director / HQ WH Manager

3. **Steps in a Markdown Table:**

| Step # | Role                        | Action                                  | Next Step/Logic                                  |
|--------|-----------------------------|-----------------------------------------|--------------------------------------------------|
| 1      | SC Material Planner         | Start                                   | Min Stock Level (as Defined)                     |
| 2      | SC Material Planner         | Min Stock Level (as Defined)            | Auto Replenishment                               |
| 3      | SC Material Planner         | Auto Replenishment?                     | Yes: Review SAP Replenishment Report<br>No: Urgent/Manual Requirement |
| 4      | SC Material Planner         | Urgent/Manual Requirement               | Identify Replenishment Items                     |
| 5      | DC Officer / WH Section Head| Identify Replenishment Items            | Review SAP Replenishment Report                  |
| 6      | SC Material Planner         | Review SAP Replenishment Report         | Approval                                         |
| 7      | SC Director / HQ WH Manager | Approval                                | Yes: Validated Stock Replenishment Request<br>No: Feedback Report |
| 8      | SC Director / HQ WH Manager | Validated Stock Replenishment Request   | Approved                                         |
| 9      | SC Director / HQ WH Manager | Approved?                               | Yes: Issue PR<br>No: Feedback Report             |
| 10     | SC Material Planner         | Issue PR                                | End                                              |
| 11     | SC Director / HQ WH Manager | Feedback Report                         | Review SAP Replenishment Report                  |

4. **Mermaid.js Code Block:**

```mermaid
graph TD;
    A[Start] --> B[Min Stock Level (as Defined)]
    B --> C{Auto Replenishment?}
    C -- Yes --> F[Review SAP Replenishment Report]
    C -- No --> D[Urgent/Manual Requirement]
    D --> E[Identify Replenishment Items]
    E --> F
    F --> G{Approval?}
    G -- Yes --> H[Validated Stock Replenishment Request]
    G -- No --> K[Feedback Report]
    H --> I{Approved?}
    I -- Yes --> J[Issue PR]
    I -- No --> K
    J --> L[End]
    K --> F
```
