---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

1. **Process Name**: Purchasing Departmental & Administration Items

2. **Roles (Swimlanes)**:
   - Item Requester
   - Procurement Officer
   - Procurement Manager/SC Director
   - FC/HOD/CF/G/CEO
   - Supplier or Service Dealer

3. **Markdown Table**:

| Step # | Role                          | Action                                | Next Step/Logic           |
|--------|-------------------------------|---------------------------------------|---------------------------|
| 1      | Item Requester                | Start                                 | 2                         |
| 2      | Procurement Officer           | Item Request                          | 3                         |
| 3      | Procurement Manager/SC Director | Approved?                           | Yes: 6, No: 2             |
| 4      | Procurement Officer           | Preparation of RFQ                    | 5                         |
| 5      | Supplier or Service Dealer    | RFQ                                   | 4                         |
| 6      | procurement Officer           | Comparison Sheet                      | 7                         |
| 7      | Procurement Officer           | PR Creation in SAP                    | 8                         |
| 8      | FC/HOD/CF/G/CEO               | Approved?                             | Yes: 10, No: 9            |
| 9      | Procurement Officer           | PO                                    | 8                         |
| 10     | Procurement Officer           | PO                                    | 11                        |
| 11     | FC/HOD/CF/G/CEO               | PO, PR Comparison Sheet & Evaluation Form | 12                  |
| 12     | Procurement Officer           | Received Item                         | 13                        |
| 13     | Item Requester                | End                                   | -                         |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    A1(Start) --> A2(Item_Request)
    A2 -- No --> A4(Preparation_of_RFQ)
    A4 --> A5(RFQ)
    A5 --> A4
    A4 --> A2
    A2 --> B1(Approved?)
    B1 -- Yes --> C1(Comparison_Sheet)
    C1 --> C2(PR_Creation_in_SAP)
    C2 --> D1(Approved?)
    D1 -- No --> D2(PO)
    D2 --> D1
    D1 -- Yes --> E1(Item_Received)
    E1 --> A3(End)
    E1 --> E2(PO_PR_Comparison_Sheet_and_Evaluation_Form)
    E2 --> E1
```