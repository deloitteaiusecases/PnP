---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 36
Last_Updated: 2026-03-16
---

Certainly! Here's the analysis of the flowchart:

### 1. Process Name:
- Product Shelf-Life Management

### 2. Roles (Swimlanes):
- QA Manager
- Packaging Operator
- Warehouse Manager
- SAP Coordinator

### 3. Steps Extracted into a Markdown Table:

| Step # | Role              | Action                                                                                  | Next Step/Logic                      |
|--------|-------------------|-----------------------------------------------------------------------------------------|--------------------------------------|
| 1      | QA Manager        | Define product-specific shelf life (M)                                                  | 2                                    |
| 2      | Packaging Operator| Ensures correct expiration date is printed based on production date + shelf life (M)    | Approved?                            |
| 3.1    | QA Manager        | Stop line, relabel or rework affected units                                             | 1                                    |
| 4      | SAP Coordinator   | Upon batch release, QA posts Usage Decision (UD) in SAP QM. (A/M)                       | 5                                    |
| 5      | Warehouse Manager | Stores products per storage SOP: Ambient conditions, humidity control (M)               | 6                                    |
| 6      | Warehouse Manager | Warehouse Supervisor enforces: FIFO, FEFO, and periodic stock reviews conducted (M)     | Aging stock?                         |
| 7.1    | Warehouse Manager | Flag for immediate dispatch or downgrade (M)                                            | 9                                    |
| 8      | QA Manager        | Conducts Monthly sampling for shelf life verification (M)                               | 9                                    |
| 9      | SAP Coordinator   | Expired or soon-to-expire stock is downgraded and disposed. All actions recorded in SAP (M) | 10                                   |
| 10     | QA Manager        | Shelf life adherence is reviewed monthly by QA. (M)                                     | 11                                   |
| 11     | SAP Coordinator   | Shelf life data retained in SAP for traceability and regulatory inspection (A/M)        | End                                  |

### 4. Logic as a Mermaid.js Code Block:

```mermaid
graph TD;
    Start --> A1(Define product-specific shelf life)
    A1 --> A2(Ensures correct expiration date is printed)
    A2 --> B{Approved?}
    B -- Yes --> C1(Upon batch release, QA posts Usage Decision)
    B -- No --> D1(Stop line, relabel or rework affected units)
    C1 --> E1(Stores products per storage SOP)
    E1 --> F1(Warehouse Supervisor enforces stock control)
    F1 --> G{Is there any aging stock nearing expiry?}
    G -- Yes --> H1(Flag for immediate dispatch or downgrade)
    G -- No --> I1(Conducts Monthly sampling for shelf life verification)
    H1 --> J1(Expired or soon-to-expire stock is downgraded and disposed)
    I1 --> J1
    J1 --> K1(Shelf life adherence is reviewed monthly by QA)
    K1 --> L1(Shelf life data retained in SAP for traceability)
    L1 --> End
```

This structure outlines the process flow and decision paths within the Product Shelf-Life Management process.