---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

Here’s the analysis of the flowchart:

### 1. Process Name
- Assets & CAPEX

### 2. Roles (Swimlanes)
- Service Provider
- Requester
- Local Buyer/Procurement Officer
- Procurement Manager/S Director
- FC/HOD
- CEO/CFO

### 3. Markdown Table of Steps

| Step # | Role                                | Action                | Next Step/Logic          |
|--------|-------------------------------------|-----------------------|--------------------------|
| 1      | Requester                           | Start                 | Assets Request           |
| 2      | Local Buyer/Procurement Officer     | Assets Request        | Approved?                |
| 3      | Procurement Manager/S Director      | Approved?             | Yes: Preparation of RFQ / No: End |
| 4      | Local Buyer/Procurement Officer     | Preparation of RFQ    | Comparison Summary       |
| 5      | Local Buyer/Procurement Officer     | Comparison Summary    | Approved?                |
| 6      | Procurement Manager/S Director      | Approved?             | Yes: Bid Evaluation / No: End     |
| 7      | Local Buyer/Procurement Officer     | Bid Evaluation        | Approved?                |
| 8      | Procurement Manager/S Director      | Approved?             | Yes: PR Creation in SAP / No: End |
| 9      | Local Buyer/Procurement Officer     | PR Creation in SAP    | Approved?                |
| 10     | FC/HOD                              | Approved?             | Yes: PO Creation in SAP / No: End |
| 11     | Local Buyer/Procurement Officer     | PO Creation in SAP    | Approved?                |
| 12     | CEO/CFO                             | Approved?             | Yes: PO / No: End        |
| 13     | Service Provider                    | PO                    | Assets Delivery          |
| 14     | Service Provider                    | Assets Delivery       | End                      |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1(Assets Request);
    A1 --> |Approved?| A2{Approved?};
    A2 --> |Yes| A3(Preparation of RFQ);
    A2 --> |No| End;
    A3 --> B1(Comparison Summary);
    B1 --> |Approved?| B2{Approved?};
    B2 --> |Yes| B3(Bid Evaluation);
    B2 --> |No| End;
    B3 --> |Approved?| B4{Approved?};
    B4 --> |Yes| B5(PR Creation in SAP);
    B4 --> |No| End;
    B5 --> |Approved?| C1{Approved?};
    C1 --> |Yes| C2(PO Creation in SAP);
    C1 --> |No| End;
    C2 --> |Approved?| C3{Approved?};
    C3 --> |Yes| C4(PO);
    C3 --> |No| End;
    C4 --> D1(Assets Delivery);
    D1 --> End;
```

This structure follows the decision flow and makes clear distinctions where approvals are required.