---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

Certainly. Here's the analysis of the flowchart:

### 1. Process Name:
- Purchase of Spare Parts for Machine & Plant

### 2. Roles (Swimlanes):
- Technical Manager
- Procurement Officer
- Procurement Manager/SC Director
- FC/HOD/CFO/CEO
- Supplier or Service Dealer

### 3. Steps in a Markdown Table:

```markdown
| Step # | Role                                      | Action               | Next Step/Logic   |
|--------|-------------------------------------------|----------------------|-------------------|
| 1      | Technical Manager                         | Start                | Spare Parts Request |
| 2      | Procurement Officer                       | Spare Parts Request  | Prepare / Send RFQ |
| 3      | Procurement Officer                       | Prepare / Send RFQ   | Price Quote       |
| 4      | Procurement Officer                       | Price Quote          | PR                |
| 5      | Procurement Manager/SC Director           | PR                   | Approved? (PR)    |
| 6      | FC/HOD/CFO/CEO                            | Approved? (PR) Yes   | RFQ               |
| 7      | FC/HOD/CFO/CEO                            | Approved? (PR) No    | End               |
| 8      | Supplier or Service Dealer                | RFQ                  | Quotation Review  |
| 9      | Procurement Officer                       | Quotation Review     | PO                |
| 10     | Procurement Officer                       | PO                   | Approved? (PO)    |
| 11     | FC/HOD/CFO/CEO                            | Approved? (PO) Yes   | PO to Supplier    |
| 12     | FC/HOD/CFO/CEO                            | Approved? (PO) No    | End               |
| 13     | Supplier or Service Dealer                | PO to Supplier       | Received Parts    |
| 14     | Technical Manager                         | Received Parts       | End               |
```

### 4. Logic in Mermaid.js Code Block:

```mermaid
graph TD
    A(Start) --> B(Spare Parts Request)
    B --> C(Prepare / Send RFQ)
    C --> D(Price Quote)
    D --> E(PR)
    E --> |Approved?| F{Approved? (PR)}
    F --> |Yes| G(RFQ)
    F --> |No| Z(End)
    G --> H(Quotation Review)
    H --> I(PO)
    I --> J{Approved? (PO)}
    J --> |Yes| K(PO to Supplier)
    J --> |No| Z
    K --> L(Received Parts)
    L --> Z
```

This analysis provides a clear representation of the flowchart into textual and code formats, along with proper logic tracing.