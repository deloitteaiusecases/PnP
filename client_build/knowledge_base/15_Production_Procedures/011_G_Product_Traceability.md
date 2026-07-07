---
Department: 1.5 Production Procedures
Section: G. Product Traceability:
Section_Kind: core
Section_Priority: normal
Source: Production Flour Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## G. Product Traceability:

8.1 Purpose:
The purpose of this procedure is to ensure that all flour products manufactured at Arabian Mills are fully traceable — from raw material intake through processing, packaging, storage, and distribution enabling rapid identification, location, and control of any batch at any point in the supply chain.
This system supports:
i. The ability to isolate and manage non-conforming products.
ii. Effective and timely execution of product recalls (where required)
iii. Compliance with SFDA, ISO 22000, and customer traceability requirements
iv. Maintenance of brand reputation and consumer trust
This procedure also enables root cause investigations for any food safety, quality, or regulatory incident through accurate product history and movement records — maintained and verified through the SAP system.
8.2 Policy Statement:
Arabian Mills maintains a fully integrated and verifiable traceability system designed to ensure that every batch of wheat, raw materials, in-process products, packaging, and finished goods can be tracked from receipt through processing, packaging, storage, dispatch, and distribution.
The system shall provide clear visibility of material flow across all processing stages to facilitate:
i. Rapid identification and isolation of affected product batches in the event of any quality or safety concern.
ii. Full compliance with SFDA, GFSI (FSSC 22000 or BRC), and Codex requirements.
iii. Support for transparent communication with regulators, customers, and supply chain partners.
iv. Maintenance of consumer trust through effective risk management.
Traceability data shall be managed primarily through SAP MM, QM, and WM modules, with seamless integration between procurement, production, QA, and dispatch processes. All records will be maintained in an audit-ready state to ensure swift retrieval during regulatory inspections or internal verifications.
8.3 Scope:
This procedure applies to all materials including wheat, additives, processing aids, packaging materials, and finished flour products, processed and distributed by Arabian Mills. It covers:
i. Raw material intake and silo storage.
ii. Processing, milling, conditioning, and packaging operations.
iii. Finished goods warehousing and distribution.
iv. Inter-company transfers and third-party logistics.
It applies to all personnel in:
i. Procurement
ii. Production & Milling
iii. QA/QC
iv. Warehouse & Dispatch
v. IT (supporting SAP system integrity).
8.4 Applicable Standards & References:
i. SFDA Technical Regulations on Food Traceability
ii. GFSI Benchmarking Requirements (FSSC 22000 / BRC)
iii. Codex Alimentarius CAC/GL 60-2006 (Principles for Traceability)
iv. ISO 22005:2007 Food Chain Traceability
v. Company Quality Manual & QMS procedures
8.5 Policies - Product Traceability:
i. Each finished product must be linked to a unique batch number that captures full backward (raw materials, rework, packaging) and forward (customers, distributors) traceability.
ii. All traceability information must be system-managed and retrievable within 2 hours of a request (internal, regulatory, or customer).
iii. Daily traceability checks must be conducted and documented to verify linkage between input materials and output batches.
iv. Lot tracking must extend to all packing and labelling materials, with issuance and usage reconciled in system transactions.
v. Periodic traceability drills (mock recalls) must be conducted to validate traceability system integrity and responsiveness.
8.6 Procedures - Product Traceability:

| Sr. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1. | **Supplier Lot Recording**<br>• Procurement team shall ensure that all incoming materials (wheat, additives, packaging) are linked to a unique supplier lot number and purchase order in SAP at Goods Receipt Note (GRN) posting. Supplier Certificate of Analysis (COA) and batch number are attached digitally in SAP. ✔ Acceptance: Complete lot number and COA recorded. ✖ Rejection: Missing COA or lot number. Actions on Rejection:<br>• I) Procurement Officer to hold the material immediately in SAP system; notify QA Analyst for evaluation; contact supplier to urgently provide missing COA or lot documentation.<br>• ii) Do not release material for use until all records are complete and verified. | Procurement Officer , QA Analyst (for respective actions) | Per delivery |
| 2. | **Raw Wheat Traceability in Silo Transfers**<br>• Silo Operator shall perform stock transfers in SAP MM to link raw wheat lots to specific silo bins, recording transfer date, lot, and QA clearance. QA Analyst to verify batch-silo linkage weekly. ✔ Acceptance: Transfer correctly posted with lot linked to silo. ✖ Rejection: Unlinked or incorrect lot posting. Actions on Rejection:<br>• i) Block usage of the affected lot; correct SAP posting; perform re-verification of batch-silo linkage<br>• ii) QA to confirm accuracy before allowing lot use. | Silo Operator , QA Analyst (for respective actions) | Daily posting, weekly verification |
| 3. | **In-Process Batch Linking**<br>• Milling Operator must ensure that each processing lot is linked to raw wheat lot ID in SAP batch master. Usage Decision (UD) posting must confirm QA clearance for batch progression. ✔ Acceptance: Complete batch linking to raw wheat lot. ✖ Rejection: Incomplete batch record in SAP. Actions on Rejection:<br>• Hold the lot in SAP; perform correction of traceability records; notify QA Manager.<br>• ii) Verify correction and obtain QA approval prior to batch progression. | Milling Operator , QA Manager (for respective actions) | Per lot |
| 4. | **Packaging Material Traceability**<br>• Packaging Supervisor must ensure packaging material batch numbers are posted against finished product batches in SAP. QA to cross-check during production and after packaging. ✔ Acceptance: Accurate linkage of packaging batch to product lot. ✖ Rejection: Missing packaging batch linkage. Actions on Rejection:<br>• i) Quarantine the affected finished product; update packaging traceability records in SAP; re-verify packaging linkage<br>• ii) Obtain QA approval before release of affected stock. | Packaging Supervisor , QA Packaging Specialist (for respective actions) | Per batch |
| 5. | **Finished Product Lot Traceability**<br>• QA Specialist shall ensure that each finished product lot is fully linked in SAP to raw wheat lot, packaging materials, production date, and QA release (UD). ✔ Acceptance: Traceability complete and accurate. ✖ Rejection: Traceability incomplete. Actions on Rejection:<br>• i) Block lot in SAP from dispatch; correct lot linkage in system; re-verify linkage for completeness<br>• ii) Obtain QA sign-off prior to product release. | QA Specialist | Per Lot |
| 6. | **Dispatch Traceability**<br>• Dispatch Officer shall ensure that each delivery note in SAP SD module is correctly linked to the corresponding finished product lots, maintaining forward traceability. ✔ Acceptance: Full linkage from delivery note to lot. ✖ Rejection: Incomplete or incorrect linkage. Actions on Rejection:<br>• i) Block dispatch in SAP; correct delivery lot linkage; perform re-verification with QA.<br>• ii) Obtain QA release approval before proceeding with dispatch. | Dispatch Office , QA Packaging Specialist (for respective actions) | Per shipment |
| 7. | **Traceability Verification Exercises**<br>• QA Manager shall conduct mock traceability tests quarterly (both backward and forward) to verify the completeness and accuracy of lot traceability in SAP. Target retrieval time <2 hours. ✔ Acceptance: Complete traceability demonstrated. ✖ Rejection: Gaps found in lot linkage. Actions on Rejection:<br>• i) Issue NCR immediately; perform correction of identified gaps; conduct staff retraining where needed.<br>• ii) Document corrective action; retest traceability to confirm system integrity. | QA Manager | Quarterly |
| 8. | **Traceability Record Retention**<br>• IT team, together with QA, shall ensure that traceability records (lot linkage, COAs, UD, GRN) are retained in SAP for at least 5 years. ✔ Acceptance: Records archived per retention policy. ✖ Rejection: Missing or incomplete archived records. Actions on Rejection:<br>• Initiate CAPA process; conduct full audit of archive records; update any incomplete records; QA Manager to confirm audit readiness. | IT Specialist , QA Manager (for respective actions) | Annual audit |

Flowchart:

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Product Traceability  

**Roles / Swimlanes:**
- Procurement Officer  
- Silo Operator  
- Milling Operator  
- Packaging Supervisor  
- QA  
- Dispatch Officer  

### Steps

| Step # | Role               | Action | Decision/Next Step |
|--------|--------------------|--------|--------------------|
| Start  | Procurement Officer | Start | Next step: 1 |
| 1 | Procurement Officer | Ensures Each delivery has a unique Supplier Lot No. (M) | Next step: 2 |
| 2 | Silo Operator | Performs transfers wheat to silo. Links lot to specific bin in SAP. (M) | Next step: 3 |
| 3 | Milling Operator | Links production batch to raw wheat lot in SAP. Ensures UD from QA is posted in SAP QM. (M) | Next step: 4 |
| 4 | Packaging Supervisor | Issues packaging materials via SAP (MM). Links packaging lot to product batch in SAP (M) | Next step: 5 |
| 5 | QA | QA posts UD in SAP QM to release finished product. (M) | From here the flow proceeds in parallel: to step 6 (Dispatch) and to step 7 (QA traceability drills). |
| 6 | Dispatch Officer | Ensures Only SAP QReleased batches are dispatched. Each delivery note links to corresponding product batch in SAP SD. (A) | Process for dispatching finished product completes after this step; overall process continues with QA steps 7–9. |
| 7 | QA | Conducts quarterly traceability drills from product to wheat/ packaging and from raw material to customer (M) | Next step: 8 |
| 8 | QA | Ensures all traceability records retained in SAP for up  years (A/M) | Next step: 9 |
| 9 | QA | If linkage is missing or incomplete*: QA initiates NCR. Blocks batch in SAP. Corrective action logged (M) | If linkage is missing or incomplete → QA initiates NCR, blocks batch in SAP, corrective action logged, then End. If linkage is not missing or incomplete → End. |
| End | QA | End | — |

\*The asterisk appears after the word “incomplete*” in the step text.

---

```mermaid
graph TD

    A0[Start\n(Procurement Officer)] --> A1
    A1[1. Ensures Each delivery has a unique Supplier Lot No. (M)\n(Procurement Officer)] --> B2
    B2[2. Performs transfers wheat to silo. Links lot to specific bin in SAP. (M)\n(Silo Operator)] --> C3
    C3[3. Links production batch to raw wheat lot in SAP. Ensures UD from QA is posted in SAP QM. (M)\n(Milling Operator)] --> D4
    D4[4. Issues packaging materials via SAP (MM). Links packaging lot to product batch in SAP (M)\n(Packaging Supervisor)] --> E5
    E5[5. QA posts UD in SAP QM to release finished product. (M)\n(QA)] --> F6
    E5 --> G7

    F6[6. Ensures Only SAP QReleased batches are dispatched. Each delivery note links to corresponding product batch in SAP SD. (A)\n(Dispatch Officer)] --> HEnd[End]

    G7[7. Conducts quarterly traceability drills from product to wheat/ packaging and from raw material to customer (M)\n(QA)] --> H8
    H8[8. Ensures all traceability records retained in SAP for up  years (A/M)\n(QA)] --> I9
    I9[9. If linkage is missing or incomplete*: QA initiates NCR. Blocks batch in SAP. Corrective action logged (M)\n(QA)] --> JDec

    JDec{Linkage missing or incomplete?} -->|Yes| KEndNCR[End\n(after NCR, batch blocked, corrective action logged)]
    JDec -->|No| HEnd
```