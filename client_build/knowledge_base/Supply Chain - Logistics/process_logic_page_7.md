---
Department: Supply Chain - Logistics
Source_Document: Supply Chain - Logistics.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

Sure, here is the analysis of the flowchart:

### 1. Process Name
Freight Invoice Process

### 2. Roles (Swimlanes)
- Transportation
- Dispatch Supervisor
- Logistics Manager
- Finance Coordinator

### 3. Steps in Markdown Table

| Step # | Role              | Action                                     | Next Step/Logic                   |
|--------|-------------------|--------------------------------------------|-----------------------------------|
| 1      | Transportation    | Start                                      | Physical Invoice & Document Set   |
| 2      | Transportation    | Physical Invoice & Document Set            | Freight Discrepancy Log           |
| 3      | Transportation    | Freight Discrepancy Log                    | Invoice Approval Summary          |
| 4      | Transportation    | Invoice Approval Summary                   | Approved -> Approved Freight Invoice Batch \n Not Approved -> Trip Validation Checklist |
| 5      | Dispatch Supervisor | Trip Validation Checklist                | Freight Discrepancy Log           |
| 6      | Logistics Manager | Approved Freight Invoice Batch             | SAP FI Posting & Payment Schedule Report |
| 7      | Finance Coordinator | SAP FI Posting & Payment Schedule Report | End                               |

### 4. Logic in Mermaid.js Code Block

```mermaid
graph TD;
    A(Start) --> B(Physical Invoice & Document Set)
    B --> C(Freight Discrepancy Log)
    C --> D{Invoice Approval Summary}
    D -- Approved --> E(Approved Freight Invoice Batch)
    D -- Not Approved --> F(Trip Validation Checklist)
    F --> C
    E --> G(SAP FI Posting & Payment Schedule Report)
    G --> H(End)
```

This represents the flow of the Freight Invoice Process with explicit decision paths based on the invoice approval status.