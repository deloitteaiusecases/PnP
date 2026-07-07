---
Department: General
Section: Policies & Procedure for Purchasing Transportation Services
Section_Kind: core
Section_Priority: normal
Source: SCM_Procurement Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Policies & Procedure for Purchasing Transportation Services

Policies
The following policies define the rules and expectations for procuring transportation services at Arabian Mills These ensure consistency, compliance, and proper vendor management across all external transportation engagements.
Transportation Services Requisition
 Procurement of transportation services is initiated on a need basis—especially when no internal vehicles are available to fulfill the request. The requisition must be received formally via email from the requester.
Minimum Number of Service Providers
 A minimum of two (2) transportation service providers must be considered for every service requirement.
Request for Quotation
 All transportation services must be procured through an RFQ process. The RFQ shall be sent to at least two (2) pre-qualified service providers listed in the approved vendor list.
Approved Vendors List
 The Procurement Department must maintain an approved vendor list, developed through a defined supplier selection and qualification process. This list must be used when issuing RFQs.
Payment to Service Providers
 Payments to service providers may be made in cash or on credit depending on the case. The Supply Chain Department holds full responsibility for determining the appropriate payment terms, which must align with the agreement made with the service provider.
Payment Currency
 All payments will be made in Saudi Riyals (SR).
Service Compliance
 The quality of the procured transportation service must meet Arabian Mills’ service level requirements and comply with all predefined terms outlined by the requesting department.
Procedure
This procedure outlines the process for procuring transportation services at Arabian Mills, including route planning, vendor selection, quotation comparison, and PO issuance. It ensures all transport arrangements are handled through approved service providers and formal documentation to support operational efficiency and compliance.

| S. No. | Responsibility | Procedure Description | Output / Report |
| --- | --- | --- | --- |
|  | Logistics Coordinator | Send transportation request to the Procurement Officer via email, including all required transportation details. This applies when internal vehicles are unavailable. | Transportation Request |
|  | Procurement Officer | Forward the transportation request to the Supply Chain Director for review and approval. | Approved Transportation Request |
|  | Procurement Officer | Send the RFQ by email to at least two (2) transportation service providers listed in the qualified supplier list. RFQ must include service details and terms. | RFQ Sent |
|  | Service Provider | Submit price quotations including service specifications, delivery timelines, and commercial terms to the Procurement Officer. | Price Quotation |
|  | Procurement Officer | Compile and review quotations. Prepare a comparison sheet and send it to the Supply Chain Director. | Quotations Comparison Sheet |
|  | Procurement Officer | Negotiate prices and service terms with service providers. If price gaps exist, escalate the matter to the Supply Chain Director and requester for resolution with justification. | Negotiation Notes |
|  | Procurement Officer | Prepare a Bid Evaluation Report. Obtain signatures from Procurement Manager and Supply Chain Director. | Bid Evaluation Form |
|  | Logistics Coordinator | Prepare the Purchase Request (PR) in the SAP system with service terms and specifications. | PR on SAP |
|  | Procurement Officer | Receive the PR. Add prices, supplier details, and payment terms. | Updated PR |
|  | Procurement Officer | Submit the PR for approval to the Plant Manager and Supply Chain Director. | Approved PR |
|  | Procurement Officer | Upon PR approval, convert the PR into a Purchase Order (PO) in SAP. | PO Generated |
|  | Procurement Officer | Print the PO and submit the complete document pack (Comparison Sheet, Bid Evaluation, PR) to Procurement Manager for review and signature. | PO and Supporting Documents |
|  | Procurement Manager | Review and sign the PO. Return it to the Procurement Officer for communication with the service provider. | Signed PO |
|  | Procurement Officer | If advance payment is required, prepare and send document copies to the Finance Department prior to service delivery. | Document Copies to Finance |
|  | Procurement Officer | If payment is on credit, send original invoices and documents to the Finance Department after the transportation service is rendered. | Invoice |
|  | Procurement Officer | Follow up with service provider and requester to ensure timely and accurate implementation of the transportation service. | Follow-up Email / Call Record |
|  | Procurement Officer | Archive the completed PO and all related documentation after successful service delivery. | Archived Documentation |

Flowchart

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Logistics Service  
(Top title bar text, right side: **Procurement**)

**Roles / Swimlanes (top to bottom):**
- Service Provider
- Requester
- User Dept / Project / Cost Center
- Procurement Manager/SC Officer
- FC/HOD
- CEO/CFO

---

### Steps

| Step # | Role | Action (as labelled in diagram) | Decision / Next Step (including Yes/No branches) |
|--------|------|----------------------------------|--------------------------------------------------|
| 1 | Requester | **Start** | Proceeds to Step 2. |
| 2 | User Dept / Project / Cost Center | **Transportation Request** | Flows to approval Step 3. |
| 3 | Procurement Manager/SC Officer | **Approved** (decision on Transportation Request) | **Yes** → Step 4. **No** (labelled “NO” in red to left of diamond) → returns back toward Step 2 Transportation Request. |
| 4 | User Dept / Project / Cost Center | **Preparation of RFQ** | After preparation, RFQ goes to Service Provider (Step 5). |
| 5 | Service Provider | **RFQ** | Process continues with internal evaluation steps (Step 6). |
| 6 | User Dept / Project / Cost Center | **Comparison Summary** | Goes to approval Step 7. |
| 7 | Procurement Manager/SC Officer | **Approved** (decision related to Comparison Summary) | **Yes** (labelled “Yes” in green) → Step 8 Bid Evaluation. (No branch not explicitly shown in diagram.) |
| 8 | User Dept / Project / Cost Center | **Bid Evaluation** | Output leads to Step 9 PR. |
| 9 | Requester | **PR** | Sent for approval in Step 10. |
| 10 | Procurement Manager/SC Officer | **Approved** (decision related to PR) | **Yes** (green “Yes”) → Step 11 PR Creation in SAP. (No branch not explicitly shown; presumed return to PR.) |
| 11 | User Dept / Project / Cost Center | **PR Creation in SAP** | Leads into subsequent approval steps and PO creation (Steps 12–14). |
| 12 | FC/HOD | **Approved** (decision) | **Yes** (green “Yes”) → passes to CEO/CFO approval Step 13 and onward to PO activities (Step 14). (No branch not explicitly shown.) |
| 13 | CEO/CFO | **Approved** (decision) | **Yes** (green “Yes”) → Step 14 PO Creation in SAP. (No branch not explicitly shown.) |
| 14 | User Dept / Project / Cost Center | **PO Creation in SAP** | Results in issuing a PO to Service Provider (Step 15). |
| 15 | Service Provider | **PO** | Leads to provision of **Transportation Services** (Step 16). |
| 16 | Service Provider | **Transportation Services** | Upon completion, flow proceeds to Step 17 End. |
| 17 | Service Provider | **End** | Process terminates. |

(Every diamond in the diagram is labelled “Approved”; text “Yes” appears in green on the accepted branches, and one “NO” in red appears on the rejection branch from the first approval.)

---

### Mermaid.js Flow

```mermaid
graph TD

%% Nodes
S1([Start]):::start
A2[Transportation Request]
D3{Approved}:::decision
A4[Preparation of RFQ]
B5[RFQ]
A6[Comparison Summary]
D7{Approved}:::decision
A8[Bid Evaluation]
A9[PR]
D10{Approved}:::decision
A11[PR Creation in SAP]
D12{Approved}:::decision
D13{Approved}:::decision
A14[PO Creation in SAP]
B15[PO]
B16[Transportation Services]
E17([End]):::end

%% Main flow
S1 --> A2
A2 --> D3
D3 -- Yes --> A4
D3 -- NO --> A2

A4 --> B5
B5 --> A6
A6 --> D7
D7 -- Yes --> A8

A8 --> A9
A9 --> D10
D10 -- Yes --> A11

A11 --> D12
D12 -- Yes --> D13
D13 -- Yes --> A14

A14 --> B15
B15 --> B16
B16 --> E17

%% Styles
classDef decision fill=#f8f8f8,stroke=#333,stroke-width:1px;
classDef start fill=#c6efce,stroke=#333,stroke-width:1px;
classDef end fill=#f4b084,stroke=#333,stroke-width:1px;
```