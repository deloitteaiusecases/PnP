---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

Sure! Here is the analysis based on the flowchart:

### 1. Process Name:
- **Outsourced Maintenance - Plant & Machines**

### 2. Roles (Swimlanes):
- Service Provider
- Requester
- Procurement Officer
- Procurement Manager / SC Director
- FC / HOD / CFO / CEO

### 3. Steps in Markdown Table:

| Step # | Role                             | Action                                   | Next Step/Logic          |
|--------|----------------------------------|------------------------------------------|--------------------------|
| 1      | Requester                        | Start                                    | Maintenance Request      |
| 2      | Requester                        | Maintenance Request                      | Preparation of RFQ       |
| 3      | Procurement Officer              | Preparation of RFQ                       | Quotation & Technical Doc. submission |
| 4      | Service Provider                 | Quotation & Technical Doc. submission    | Technical Evaluation     |
| 5      | Requester                        | Technical Evaluation                     | Pass: Bid Evaluation / Rejected: End |
| 6      | Procurement Officer              | Bid Evaluation                           | Approved: PR Creation in SAP |
| 7      | Procurement Manager / SC Director| Approved                                 | PR Creation in SAP       |
| 8      | Procurement Officer              | PR Creation in SAP                       | Approved: PO Creation in SAP |
| 9      | Procurement Manager / SC Director| Approved                                 | PO Creation in SAP       |
| 10     | Procurement Officer              | PO Creation in SAP                       | Approved: Transportation Services |
| 11     | Procurement Manager / SC Director| Approved                                 | Transportation Services  |
| 12     | Service Provider                 | Transportation Services                  | End                      |

### 4. Mermaid.js Code Block:

```mermaid
graph TD;
    A[Start] --> B[Maintenance Request]
    B --> C[Preparation of RFQ]
    C --> D[Quotation & Technical Doc. submission]
    D --> E{Technical Evaluation}
    E --Rejection--> X[End]
    E --Pass--> F[Bid Evaluation]
    F --> G{Approved}
    G -->|Yes| H[PR Creation in SAP]
    G -->|No| C
    H --> I{Approved}
    I -->|Yes| J[PO Creation in SAP]
    J --> K{Approved}
    K -->|Yes| L[Transportation Services]
    L --> X[End]
```

This provides a structured overview of the process, highlighting each step and decision points in the flowchart.