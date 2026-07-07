---
Department: General
Section: Policies & Procedure for Purchasing Spare Parts, Consumables for Machines & Plants
Section_Kind: core
Section_Priority: normal
Source: SCM_Procurement Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Policies & Procedure for Purchasing Spare Parts, Consumables for Machines & Plants

Policies
This section outlines the procurement policies applicable to spare parts and consumables required for the repair, maintenance, and operation of machinery and plant equipment at Arabian Mills These policies ensure that items are sourced reliably, in compliance with specifications, and within warranty conditions.
Minimum Number of Suppliers
 Every spare part must be sourced from a minimum of three (3) suppliers to ensure competitive pricing and quality assurance.
 This requirement may be waived if a machine agent or authorized dealer is the exclusive provider of the required spare part.
Request for Quotation
 All spare parts and consumables must be procured through a structured RFQ process.
 The RFQ must be issued to a minimum of three (3)   pre-qualified suppliers for each purchase.
Approved Vendors List
 An official approved vendor list must be maintained by the Supply Chain Department.
 This list must be created using a defined selection and qualification procedure and must be referred to for all procurement activities.
Payment to Suppliers
 Payments to suppliers may be made in cash or on credit, based on the nature and urgency of the procurement.
 All payments must follow the terms and conditions specified in the supplier agreement.
Payment Currency
 The default currency for procurement is Saudi Riyals (SAR).
 Payments in USD or EUR are permitted for international purchases as stated in the supplier agreement.
Spare Part / Consumables Compliance
 All spare parts and consumables must comply with pre-defined specifications shared with the supplier at the RFQ stage.
 Non-compliant deliveries must be rejected and returned according to the company’s quality assurance protocol.
Parts Provider Selection
 If a genuine part is available from an authorized machine agent, it must be purchased directly.
 If unavailable, the part should be procured from other approved suppliers following the standard RFQ process.
Machine Warranty
 Prior to procurement, the machine warranty must be reviewed.
 If the issue is covered by warranty, the supplier or agent must be contacted, and the warranty claim procedure followed.
Spare Part Installation
 If applicable, the installation of spare parts may be carried out by the parts provider to ensure proper fitment and validation.
Spare Part Warranty
 Procured spare parts may carry a supplier-issued warranty that guarantees their operational performance for a specified period.
 The warranty terms must be verified and documented at the time of procurement.
Procedure
This procedure defines the systematic steps to be followed for procuring spare parts and consumables used in machinery and plant operations at Arabian Mills It ensures supplier qualification, quotation review, warranty compliance, and SAP-based transaction tracking.

| S. No | Responsibility | Procedure Description | Output / Report |
| --- | --- | --- | --- |
|  | Department Coordinator | Send a Spare Part Request to the Procurement Officer by email. The request must include the part name and serial number to ensure accurate sourcing. | Spare Part Request |
|  | Procurement Officer | Check if the required spare part is exclusive to an authorized dealer . If so, send the RFQ directly to that dealer. If not, issue RFQ to a minimum of three (3) qualified suppliers. | RFQ |
|  | Procurement Officer | In all cases, review the existing agreement with the supplier. If using an authorized dealer, ensure any pre-agreed discounts or pricing terms are included in the quotation. | Email |
|  | Procurement Officer | Once quotations are received, forward them to the Technical Manager for evaluation and clarification. | Quotations |
|  | Head of Maintenance | Review the quotations. If technical queries arise, send them to the Procurement Officer for supplier clarification. | Quotations |
|  | Procurement Officer | Forward the technical queries to the relevant suppliers and follow up for detailed responses. | Email |
|  | Head of Maintenance | After resolving technical queries, classify the suppliers based on price, quality, and lead time. Create and submit a Purchase Requisition (PR) in the SAP system. | PR on SAP |
|  | Procurement Officer | If the spare part is new or not in the system, initiate a New Item Registration Form . Send it to the Finance Department for SAP entry after approval from the Supply Chain Director . | Item Registration Form |
|  | Procurement Officer | Upon PR generation, if there is only one source, issue the PO directly to the selected supplier. If multiple suppliers are evaluated, prepare a Bid Evaluation Form , then create a PO in SAP and submit for approval. | PO or Bid Evaluation + PO |
|  | Procurement Officer | Send a copy of the PO to the Supplier and the Warehouse . Also print all supporting documents ( PR, Comparison Sheet, and Bid Evaluation Form ) and submit to Finance in case of cash deal or where advance payment is required. | PO and Supporting Documents |
|  | Procurement Officer | If the purchase is on credit , send the PO, all supporting documents , and the Goods Received Note (GRN) to the Finance Department after material delivery . | GRN |

Flowchart

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Purchase Of Spare Parts for Machine & Plant  

**Roles / Swimlanes:**

1. Technical Manager  
2. Procurement Officer  
3. Procurement Manager / SCM Director  
4. F/COO/CEO (exact text partially unclear; transcribed as visible)  
5. Supplier Or Service Dealer  

---

### Process Steps

| Step # | Role                                | Action / Decision Label | Decision / Next Step |
|--------|-------------------------------------|-------------------------|----------------------|
| 1      | Technical Manager                  | Start                   | Proceeds to Step 2: “Spare Parts Request”. |
| 2      | Procurement Officer                | Spare Parts Request     | Proceeds to Step 3: “Prepare / Send RFQ”. |
| 3      | Procurement Officer                | Prepare / Send RFQ      | Proceeds to Step 4: “RFQ” (Supplier Or Service Dealer). |
| 4      | Supplier Or Service Dealer         | RFQ                     | Proceeds to Step 5: “Price Quote” (back to Procurement Officer). |
| 5      | Procurement Officer                | Price Quote             | Proceeds to Step 6: “Quotation Review” (Technical Manager). |
| 6      | Technical Manager                  | Quotation Review        | Proceeds to Step 7: “PR”. |
| 7      | Procurement Officer                | PR                      | Proceeds to Step 8: Decision “Approved?” (Procurement Manager / SCM Director). |
| 8      | Procurement Manager / SCM Director | Approved?               | Yes → Step 9: Decision “Approved?” (F/COO/CEO). No path is not shown in the diagram. |
| 9      | F/COO/CEO                          | Approved?               | Yes → Step 10: “PO” (Procurement Officer). No path is not shown in the diagram. |
| 10     | Procurement Officer                | PO                      | Proceeds to Step 11: “PO” (Supplier Or Service Dealer). |
| 11     | Supplier Or Service Dealer         | PO                      | Proceeds to Step 12: “Received Parts” (Technical Manager). |
| 12     | Technical Manager                  | Received Parts          | Proceeds to Step 13: “End”. |
| 13     | Technical Manager                  | End                     | Process terminates. |

Yes/No branches explicitly:

- Step 8 “Approved?” (Procurement Manager / SCM Director)  
  - Yes → Step 9 “Approved?” (F/COO/CEO)  
  - No → Not indicated in the diagram (no return or alternate flow shown).

- Step 9 “Approved?” (F/COO/CEO)  
  - Yes → Step 10 “PO” (Procurement Officer)  
  - No → Not indicated in the diagram (no return or alternate flow shown).

---

### Mermaid Diagram

```mermaid
graph TD

%% Roles noted in comments for clarity
    A1[Start\n(Technical Manager)] --> A2[Spare Parts Request\n(Procurement Officer)]
    A2 --> A3[Prepare / Send RFQ\n(Procurement Officer)]
    A3 --> B1[RFQ\n(Supplier Or Service Dealer)]
    B1 --> A4[Price Quote\n(Procurement Officer)]
    A4 --> A5[Quotation Review\n(Technical Manager)]
    A5 --> A6[PR\n(Procurement Officer)]
    A6 --> D1{Approved?\n(Procurement Manager / SCM Director)}
    D1 -->|Yes| D2{Approved?\n(F/COO/CEO)}
    D1 -->|No (not shown)| D1_No[(No path specified\nin source diagram)]
    D2 -->|Yes| A7[PO\n(Procurement Officer)]
    D2 -->|No (not shown)| D2_No[(No path specified\nin source diagram)]
    A7 --> B2[PO\n(Supplier Or Service Dealer)]
    B2 --> A8[Received Parts\n(Technical Manager)]
    A8 --> A9[End\n(Technical Manager)]
```