---
Department: 1.5 Production Procedures
Section: F. Finished Products:
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: F. Finished Products:
Source: Production Flour Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 2
---

## F. Finished Products:

7.1 Purpose:
The purpose of this procedure is to ensure that all finished flour products meet defined quality, food safety, and customer specifications prior to release. This section defines the systematic approach to monitoring, verification, and control of product attributes including physical, chemical, microbiological, packaging, and labelling quality. It ensures finished products are compliant with regulatory requirements (e.g., SFDA, Codex), market expectations, and internal standards. By implementing robust monitoring and traceability via SAP QM/MM modules, the process safeguards brand integrity, supports continuous improvement, and minimizes the risk of product recalls or non-conformance.
7.2 Policy Statement:
Arabian Mills is committed to delivering finished products that consistently meet internal, regulatory, and customer standards for safety, quality, and legal compliance. All finished products must undergo complete testing, verification, and traceability confirmation prior to release. No product shall be dispatched unless:
i. It has been approved by QA in SAP QM
ii. It is correctly labelled and packaged per the relevant SKU master data.
iii. It is free from known defects or hazards.
iv. It meets all regulatory and shelf-life requirements.
Any deviations will be managed through formal non-conformance procedures and subject to continuous improvement reviews.
7.3 Scope:
This procedure applies to all finished flour products produced and packaged at the mill, including:
i. Consumer retail packs
ii. Bulk industrial bags
iii. B2B shipments (food industry, bakery channels)
It covers:
i. Finished product testing (physical, chemical, microbiological)
ii. Packaging quality assurance
iii. Labelling verification
iv. Shelf life and storage controls
v. Release procedures via SAP QM
vi. Non-conformance handling and product disposition
Applicable to all operational teams:
i. QA
ii. Production
iii. Packaging
iv. Warehouse & Distribution
v. Document Control & Regulatory Affairs
7.4 Applicable Standards & References:
i. ISO 22000 — Food Safety Management Systems
ii. ISO 9001 — Quality Management Systems
iii. SFDA Regulations — Saudi Food and Drug Authority Standards
iv. Codex Alimentarius — International Food Standards (relevant to flour)
v. GMP (Good Manufacturing Practices)
vi. GHP (Good Hygiene Practices)
vii. Customer-specific standards (if applicable)
7.5 Policies - Finished Products:
i. All finished products must comply with pre-approved product specifications for physical, chemical, and microbiological parameters (e.g., ash content, moisture, granulation, foreign matter).
ii. Finished product testing must be conducted per defined sampling plans, with results recorded against production batch numbers.
iii. Products not meeting the release criteria must be quarantined in the system and physically isolated until a disposition decision is taken by QA.
iv. Final product conformity must be verified through system-generated Certificates of Analysis (CoA), where applicable.
v. Any product quality deviations must be investigated, documented, and subject to corrective and preventive actions (CAPA).
7.6 Procedures - Finished Products:

| Sr. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1. | **Finished Product Sampling**<br>• The QA Analyst must systematically collect finished flour samples from each production line immediately after packaging and before the product is released to storage or shipment. Sampling must strictly follow the approved Sampling Plan and Matrix, which considers batch size, product type, and historical risk profile. Each sample must be traceable to the SAP Batch ID and logged in SAP QM. Sampling must be conducted in a manner that ensures representativeness (e.g., collecting at different times during the run and from different packing points). ✔ Acceptance: Samples collected correctly, recorded in SAP, traceable to batch. ✖ Rejection: Missed sampling, incomplete traceability. Actions on Rejection:<br>• QA Analyst to immediately initiate NCR; repeat sample collection as per Sampling Plan; record deviation in SAP QM and inform QA Manager for follow-up review. | QA Analyst | Per line |
| 2. | **Laboratory Analysis of Product Attributes**<br>• The QA Analyst must perform detailed laboratory analysis on each finished flour sample. Tests shall include Moisture (14.0–14.5%), Ash Content (as per spec), Protein %, Granulation Profile (target particle size), Colour (Hunter Lab or equivalent), Gluten Strength, and Full Microbiological Panel (Total Viable Count, Yeast & Mould , Coliforms, Pathogens as per SFDA requirements). All results must be recorded in SAP QM Inspection Lot. The laboratory must follow accredited methods (ISO, AACC, AOAC), and equipment must be properly calibrated. ✔ Acceptance: All parameters fall within product specifications. ✖ Rejection: Any parameter fails specification. Actions on Rejection:<br>• i) Block the affected batch in SAP; initiate NCR; perform root cause investigation; define corrective action plan and document in SAP QM<br>• ii) Escalate to QA Manager if needed. | QA Analyst | Per line |
| 3. | **Metal Detection**<br>• The Packaging Line Operator must verify the correct functioning of metal detectors at the start of shift, hourly, and after any stoppage or changeover. Challenge tests using ferrous, non-ferrous, and stainless-steel test sticks must be performed and logged. The metal detector must remain continuously active during packing. All reject bins must be checked for proper operation. If any actual contamination is detected, or a test failure occurs, the entire affected lot must be isolated, and full re-screening and investigation must be performed. ✔ Acceptance: No metal detected; all challenge tests passed. ✖ Rejection: Detector failure or contamination event. Actions on Rejection:<br>• i) Stop the packaging line immediately; isolate the affected batch.<br>• ii) QA Analyst to conduct full investigation and testing; raise NCR in SAP; arrange full re-screening of product if appropriate<br>• iii) Only release after QA Manager’s approval. | Packaging Line Operator, QA Analyst, QA Manager (for respective actions) | Start of shift, Hourly, per changeover |
| 4. | **Packaging Material Verification**<br>• The QA Analyst must verify that all packaging materials (bags, bulk sacks, FIBCs) meet approved specifications for strength, print quality, seal integrity, and regulatory compliance. Labels must be verified for content, accuracy (batch code, expiry date), legibility, and alignment with the approved label master. QA must also check sealing strength by performing manual seal tests and observing packaging quality during operations. Any discrepancies must be immediately reported, and the affected packaging batch quarantined if necessary. ✔ Acceptance: Packaging material fully compliant, labelling correct and legible. ✖ Rejection: Label errors, poor print, weak seals. Actions on Rejection:<br>• Immediately hold affected packs and segregate defective packaging materials; initiate necessary rework to correct packaging; document action and NCR in SAP; verify corrections prior to further production or release. | QA Analyst | Per line |
| 5. | **Final Release Decision (SAP Usage Decision)**<br>• The QA Manager must review all laboratory results, in-process control checks, metal detection logs, packaging verification outcomes, and micro results before final release of each batch/lot. If all requirements are satisfied, the QA Manager shall approve the Usage Decision in SAP QM and update batch status to “Released”. If any result is pending, failed, or unresolved, the batch must remain blocked in SAP. ✔ Acceptance: All release criteria met; batch marked “Released” in SAP QM. ✖ Rejection: Failed tests or incomplete release record. Actions on Rejection:<br>• i) Block batch in SAP; document NCR and investigation findings in SAP QM<br>• ii) Escalate to Production Manager for further review and resolution.<br>• iii) QA Manager to initiate the investigation and document all corrective and preventive actions (CAPA) | QA Manager , Production Manager (for respective actions) | Per lot |
| 6. | **Finished Goods Storage & Shelf Life Monitoring**<br>• The Warehouse S ection Head must ensure that all released products are stored under appropriate conditions; controlled temperature and humidity to maintain product quality and shelf life. FIFO (First-In, First-Out) stock rotation must be enforced. Environmental parameters must be logged, and deviations must trigger investigation. QA will conduct shelf-life verification sampling monthly to confirm compliance with declared shelf life. ✔ Acceptance: FIFO maintained, storage conditions within spec. ✖ Rejection: Storage deviations, aged stock present. Actions on Rejection:<br>• i) Quarantine the affected stock immediately; inform QA Manager and Production Manager<br>• ii) Conduct root cause investigation; determine stock disposition (rework, downgrade, or disposal)<br>• iii) Document corrective action in SAP and stock records.<br>• Please refer ‘Warehouse section’ of Supply Chain Management Manual for finished goods GR and storage process. | Warehouse S ection Head , QA Analyst, QA & Production Manager’s (for respective actions) | Weekly & Monthly |
| 7. | **Dispatch Release Verification**<br>• Prior to shipping, the Warehouse Section He ad must verify that only SAP “Released” batches are dispatched. The correct labels, batch documents, and customer-specific instructions must match the SAP data and delivery note. The Shipping Coordinator must ensure traceability by maintaining shipment logs linked to SAP. ✔ Acceptance: Batch “Released”, documents accurate, traceability maintained. ✖ Rejection: Unreleased stock or document mismatch. Actions on Rejection:<br>• Place an immediate hold on dispatch; correct documentation or batch status discrepancy; QA verification and sign-off required prior to releasing the product for shipment.<br>• Please refer ‘Warehouse section’ of Supply Chain Management Manual for finished goods GR and storage process. | Warehouse Section Head , QA Analyst (for respective actions) | Each Lot |

7.7 Packaging Quality (Finished Product):
7.7.1 Purpose:
The purpose of this procedure is to define a structured and systematic approach for ensuring the quality, safety, and compliance of all packaged flour products. It establishes the controls required to verify that packaging materials, processes, and finished product presentation meet regulatory, customer, and internal specifications. This procedure ensures packaging integrity, accurate labelling, traceability, and protection of product quality during storage and distribution. It also aims to minimize packaging defects, prevent mislabelling, and safeguard consumer confidence through clear accountability and process validation across all packaging operations.
7.7.2 Policy Statement:
All packaged flour products must be produced under controlled and validated packaging processes that ensure the accuracy, integrity, and compliance of the final product. Packaging operations shall meet all applicable food safety, quality, and regulatory standards, including SFDA, GSO, Codex, and customer-specific requirements. Only pre-approved packaging materials that comply with migration and suitability standards shall be used. All printed materials and labels shall undergo verification prior to use, with packaging line controls ensuring correct label application and legibility. Packaging integrity (seal strength, pack weight, contamination control) shall be verified per defined sampling plans. Packaging traceability shall be maintained through SAP batch control from packaging to warehouse dispatch. No product shall be released for storage or distribution unless the packaging has been verified and the batch approved in SAP QM.
7.7.3 Scope:
This procedure applies to all flour packaging operations conducted at the facility, covering the handling, inspection, and control of packaging materials; operation of packaging equipment for both retail and bulk pack formats; application of product labelling; verification of sealing integrity; and all quality assurance checks required prior to release for storage or dispatch. It encompasses all personnel involved in packaging, including operators, quality assurance staff, and warehouse personnel, and is applicable to all finished flour products produced under the facility’s scope of certification and licensing (SFDA, GSO, Codex). The scope also includes integration with SAP systems for traceability and batch release.
7.7.4 Applicable Standards & References:
The following standards and regulatory requirements apply to this Finished Product Packaging Quality Procedure:
i. SFDA (Saudi Food and Drug Authority) Food Packaging & Labelling Regulations
ii. Codex Alimentarius (CODEX STAN 1-1985) General Standard for the Labelling of Prepackaged Foods
iii. GCC Standardization Organization (GSO) Standards for Food Packaging Materials and Labelling
iv. ISO 22000 Food Safety Management System
v. ISO 9001 Quality Management System – Packaging Quality
vi. ISO 11607 Packaging for Terminally Sterilized Medical Devices – relevant clauses for seal integrity testing
vii. EN 868 Packaging Materials — applicable sections for transportation durability
viii. Saudi Standards, Metrology and Quality Organization (SASO) applicable for packaging materials used in food industry.
ix. Internal Customer Specifications & Export Market Requirements (for specialized or export SKU’s)
7.7.5 Policies - Packaging Quality (Finished Product):
i. Only QA-approved packaging materials (bags, liners, sacks) shall be used, as defined in the bill of materials and stored in ERP material master.
ii. Packaging materials must undergo incoming quality checks for seal integrity, tensile strength, print clarity, contamination, and compliance with food contact safety.
iii. Final packaging integrity of finished product must be checked visually and functionally (e.g., weight tolerance, seal strength, tamper-proofing) at defined intervals during packing.
iv. Rejected packaging materials must be blocked in the system and physically labelled as “Not for Use”.
v. Packaging performance issues during production must be logged and escalated for supplier or material review.
7.7.6 Procedures – Packaging Quality (Finished Product):

| Sr. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1. | **Packaging Material Selection & Verification**<br>• Packaging Supervisor to ensure only approved packaging materials are used (bags, liners, labels, sacks). Verify material specs (thickness, GSM, barrier properties, print quality, seal integrity, tensile strength, food safety compliance etc.) against procurement specs. ✔ Acceptance: Materials meet all internal and external standards. ✖ Rejection: Off-spec materials detected. Actions on Rejection:<br>• Quarantine the rejected materials immediately; notify QA and Procurement for supplier follow-up; update SAP MM records to reflect rejection; initiate replacement material request if required. | Packaging Supervisor , QA Analyst (for respective actions) | Per delivery and lot issue |
| 2. | **Pre-Use Material Inspection**<br>• QA Analyst to conduct pre-use inspection for defects (e.g., print clarity, seal ability ). ✔ Acceptance: No defects, clear printing, correct SKU and batch label. ✖ Rejection: Visual defects or mismatch to job order. Actions on Rejection:<br>• i) Isolate the defective batch of packaging material.<br>• ii) Escalate issue to QA Manager; log non-conformance in SAP; arrange replacement material as needed before production can continue. | QA Analyst , QA Manager (for respective actions) | Per lot received |
| 3. | **Bag Printing & Label Verification**<br>• Packaging Operator to validate on-line printer (or pre-printed bag) for SKU, batch code, expiry, regulatory text. Conduct start-up check, hourly check, and change-over check. ✔ Acceptance: Print clear, legible, correct per spec. ✖ Rejection: Print defects, missing info. Actions on Rejection:<br>• Immediately isolate affected bags; conduct rework or replacement of defective items as per SOP; update corrective action and results in SAP QM; verify correct printing before resuming line operation. | Packaging Operato r, QA Analyst (for respective actions) | At start-up, hourly, change-over |
| 4. | **Product Filling & Weight Check**<br>• Operator to verify filler calibration and fill weight (± tolerance). Inline checkweigher must be used if available. ✔ Acceptance: Fill weight within spec (as per packaging). ✖ Rejection: Under/overfilled. Actions on Rejection:<br>• Adjust filler calibration immediately; isolate non-conforming bags; document corrective action and affected quantities in SAP; verify correction before resuming packing. | Packaging Operator | Continuous; hourly QC verification |
| 5. | **Bag Sealing Integrity Check**<br>• QA Analyst to verify seal strength using standard pull/peel test. Random sample bags pulled every hour. ✔ Acceptance: Strong seal, no leaks, no delamination. ✖ Rejection: Weak seal, peel failures. Actions on Rejection:<br>• Stop packaging line; recalibrate sealing system; inspect last one hour’s production output; quarantine non-conforming product; resume line only after successful verification by QA. | QA Analyst | Hourly |
| 6. | **Visual Inspection (Final)**<br>• QA to perform visual QC at end-of-line conveyor: bag print, seal, product appearance. ✔ Acceptance: Clean, well-sealed bags, correct label. ✖ Rejection: Dirty, damaged, or misprinted bags. Actions on Rejection:<br>• i) Immediately remove non-conforming product from conveyor, log defect rate trends.<br>• ii) If repeat issues are observed, escalate to Packaging Supervisor and QA Manager for corrective actions and possible line adjustment. | QA Analyst | Continuous + hourly samples |
| 7. | **Metal Detection**<br>• All packed flour must pass through calibrated metal detector. ✔ Acceptance: Metal detector pass, no alarms. ✖ Rejection: Alarm triggered. Actions on Rejection:<br>• i) Stop conveyor immediately; isolate suspect product; conduct full re-screening of the batch.<br>• ii) Perform root cause analysis; update SAP QM batch records; accordingly, resume line after QA verification and approval. | QA Analyst | Continuous with hourly verification |
| 8. | **Palletization & Label Check**<br>• Packaging Operator to verify correct stacking, pallet labelling and wrapping. Pallet label must match job order and SAP batch. ✔ Acceptance: Label correct, pallet stable, no damage. ✖ Rejection: Incorrect label, unstable stack. Actions on Rejection:<br>• Rework pallet to correct stacking or labelling ; update corrected label information in SAP MM/WM; verify pallet integrity before release for warehouse storage. | Packaging Operator | Per pallet |
| 9. | **SAP Posting & Traceability Linkage**<br>• Data Entry Operator to post finished goods in SAP (MM/WM). Ensure correct batch, pallet, and label linkage for traceability. ✔ Acceptance: Complete and accurate SAP posting. ✖ Rejection: Incomplete/mismatched entry. Actions on Rejection:<br>• Correct SAP entry immediately; notify QA for verification and approval of corrected record; confirm traceability data is complete and audit-ready before moving product.<br>• Please refer ‘Warehouse section’ of Supply Chain Management Manual for finished goods GR and storage process. | Data Entry Operator, QA Manager (for respective actions) | Per lot |

Flowchart:

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Packaging Quality  

**Roles / Swimlanes:**
- Packaging Supervisor
- QA
- Packaging Operator
- Data Entry Operator  

---

### Steps and Decisions

| Step # | Role | Action | Decision / Next Step |
|--------|------|--------|----------------------|
| Start | Packaging Supervisor | Start | Next Step: 1. Ensure only approved packaging materials are used. (M) |
| 1 | Packaging Supervisor | Ensure only approved packaging materials are used. (M) | Next Step: 2. Checks Visual defects. Correct SKU and label match. Defective material is quarantined. (M) |
| 2 | QA | Checks Visual defects. Correct SKU and label match. Defective material is quarantined. (M) | Next Step: 3. Performs Start-up validation of batch code, expiry date, product label. (M) |
| 3 | Packaging Operator | Performs Start-up validation of batch code, expiry date, product label. (M) | Next Step: 4. Print and label correct? |
| 4 | Packaging Operator | Print and label correct? | If **Yes** → 5. Verify filler calibration and fill weight (M). If **No** → 4.1 Halt and Correct (M). |
| 4.1 | Packaging Operator | Halt and Correct (M) | Next Step: Loop back to 3. Performs Start-up validation of batch code, expiry date, product label. (M) |
| 5 | QA | Verify filler calibration and fill weight (M) | Next Step: 6. Conducts seal integrity testing. Peel/pull strength tests every hour. Visual inspection for leaks (M). |
| 6 | QA | Conducts seal integrity testing. Peel/pull strength tests every hour. Visual inspection for leaks (M) | Next Step: 7. Checks bags on conveyor. (M) |
| 7 | QA | Checks bags on conveyor. (M) | Next Step: 8. All finished packs pass through a calibrated metal detector (A). |
| 8 | QA | All finished packs pass through a calibrated metal detector (A) | Next Step: Decision “Approved?”. |
| Approved? | QA | Approved? | If **Yes** → 10. Ensures stable pallet stacking, correct pallet label, proper shrink wrapping (M). If **No** → 9.1 Stop line, isolate affected output (M). |
| 9.1 | QA | Stop line, isolate affected output (M) | Next Step: 12. Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M). |
| 10 | Packaging Operator | Ensures stable pallet stacking, correct pallet label, proper shrink wrapping (M) | Next Step: 11. Posts batch data into SAP MM/WM. (M) |
| 11 | Data Entry Operator | Posts batch data into SAP MM/WM. (M) | Next Step: 12. Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M). |
| 12 | QA | Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M) | Next Step: End |
| End | QA | End | — |

---

```mermaid
graph TD

    start((Start))
    s1[1. Ensure only approved packaging materials are used. (M)]
    s2[2. Checks Visual defects. Correct SKU and label match. Defective material is quarantined. (M)]
    s3[3. Performs Start-up validation of batch code, expiry date, product label. (M)]
    d4{4. Print and label correct?}
    s41[4.1 Halt and Correct (M)]
    s5[5. Verify filler calibration and fill weight (M)]
    s6[6. Conducts seal integrity testing. Peel/pull strength tests every hour. Visual inspection for leaks (M)]
    s7[7. Checks bags on conveyor. (M)]
    s8[8. All finished packs pass through a calibrated metal detector (A)]
    dAppr{Approved?}
    s91[9.1 Stop line, isolate affected output (M)]
    s10[10. Ensures stable pallet stacking, correct pallet label, proper shrink wrapping (M)]
    s11[11. Posts batch data into SAP MM/WM. (M)]
    s12[12. Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M)]
    end((End))

    start --> s1 --> s2 --> s3 --> d4
    d4 -- Yes --> s5
    d4 -- No --> s41 --> s3
    s5 --> s6 --> s7 --> s8 --> dAppr
    dAppr -- Yes --> s10 --> s11 --> s12 --> end
    dAppr -- No --> s91 --> s12
```

7.8 Product Labelling:
7.8.1 Purpose:
The purpose of this section is to ensure that all finished flour products are labelled accurately, legibly, and in full compliance with regulatory, customer, and internal requirements. The labelling process supports legal traceability, product identity, and consumer protection. Accurate labelling is critical to meeting SFDA and GSO standards, facilitating recalls if necessary, preventing food fraud, and safeguarding consumer health by ensuring transparency regarding ingredients, allergens, shelf life, and batch traceability.
7.8.2 Policy Statement:
Arabian Mills is fully committed to ensuring that all finished flour products are labelled accurately and consistently in compliance with regulatory standards, customer expectations, and internal quality requirements. Product labelling is treated as a critical control point in the supply chain, supporting legal compliance, consumer protection, and traceability.
All products must be clearly and legibly labelled with complete information prior to release from the facility. Labels shall reflect validated product specifications, shelf life, batch identity, allergen declarations, and all legally mandated information.
Only QA-approved and validated label templates may be used for production. No product may be dispatched unless it has passed label verification and is formally approved by the QA Manager or his nominee for release in SAP. Any errors or deviations in labelling, including but not limited to incorrect content, misalignment, missing codes, or illegibility will trigger immediate product hold, investigation, and corrective action. Label non-conformances are treated as a priority food safety risk and will be managed through the company's corrective action program.
All labelling operations must be fully traceable within the SAP system, including label material usage and batch reconciliation. Label equipment must be maintained and calibrated to ensure consistent print quality and performance. All personnel involved in labelling must be trained and qualified for their respective roles.
7.8.3 Scope:
This procedure applies to all flour products manufactured and packaged at Arabian Mills — including but not limited to:
i. Consumer retail packs,
ii. Bulk sacks (25–50 kg),
iii. Industrial and commercial SKUs.
It covers all stages of labelling from design approval through application, verification, and post-release traceability:
i. Label design and regulatory approval processes.
ii. Generation of artwork and master label templates.
iii. Label printing or verification of pre-printed packaging.
iv. Label application on packaging lines.
v. In-process and post-process label verification.
vi. Control of labelling materials inventory.
vii. Documentation of label lot usage in SAP.
viii. Non-conformance management and corrective actions.
This policy is applicable to personnel across:
i. Packaging operations,
ii. Quality Assurance (QA),
iii. Warehouse & Logistics,
iv. Document Control,
v. Regulatory Affairs & Compliance.
7.8.4 Applicable Standards & References:
i. Saudi Food and Drug Authority (SFDA) Food Labelling Requirements
ii. GSO 9/2013 (GCC Standardization Organization) — Labelling of Prepackaged Foods
iii. Codex Alimentarius — General Standard for the Labelling of Prepackaged Foods (Codex Stan 1-1985)
iv. ISO 22000 — Food Safety Management Systems
v. GFSI Benchmarking Requirements — Label Management Controls
vi. Internal Company Specifications — Product Label Templates, Brand Guidelines
vii. SAP QM / WM / MM Modules — for traceability and inventory management of labelling materials
7.8.5 Policies – Product Labelling:
i. Product labels must display mandatory information: product name, net weight, ingredient list, nutrition facts (if applicable), batch number, date of packing, shelf life, storage instructions, manufacturer details, and regulatory declarations.
ii. All label content must be pre-approved by QA and Regulatory Affairs and stored as version-controlled templates.
iii. Label data must be system-generated based on actual production batch characteristics to avoid manual entry errors.
iv. Label print quality, alignment, and correctness must be inspected at start-up, during batch changeover, and periodically during production.
v. Mislabelling incidents must be treated as critical non-conformances, requiring batch hold and formal incident reporting.
7.8.6 Procedures — Product Labelling:

| Sr. No. | Procedure Step | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1. | **Label Design & Approval**<br>• Regulatory Affairs Specialist, in coordination with QA Manager and Marketing, prepares and approves master artwork and label content. All label templates must be approved per SFDA, Codex, and applicable Saudi and GCC regulations, with formal document control versioning. ✔ Acceptance: Label template approved, master file archived in Document Control, version control maintained. ✖ Rejection: Missing approvals, outdated template. Actions on Rejection:<br>• i) Immediately stop use of unapproved labels, initiate artwork revision through Regulatory & QA<br>• ii) Obtain necessary approvals prior to release; document action in Document Control register and SAP Document Module. | Regulatory Affairs Specialist , QA Manager , Marketing Manager (for respective actions) | Upon new product or label revision |
| 2. | **Label Generation**<br>• QA Specialist to verify the latest approved template is used prior to printing. Printer settings (resolution, alignment, ink quality) must be checked and verified before batch start. ✔ Acceptance: Correct version loaded; printer setup validated. ✖ Rejection: Incorrect version or poor print quality. Actions on Rejection:<br>• i) Immediately halt printing process; reload correct label template; recalibrate printer settings.<br>• ii) QA to perform verification check and approve resumption of printing. | QA Specialist | Before batch printing |
| 3. | **Label Printing**<br>• Packaging Operator to print labels or operate label applicator with pre-printed materials. QA to verify first-off label sample and sign-off on batch label start sheet. ✔ Acceptance: Print quality meets specification, batch details accurate. ✖ Rejection: Illegible, smudged, misaligned or missing information. Actions on Rejection:<br>• i) Stop the production line immediately; isolate and segregate any affected printed materials; correct print settings or replace faulty label stock<br>• ii) QA Analyst to verify corrections and approve restart. | Packaging Operator , QA Analyst (for respective actions) | At start of each production line |
| 4. | **Label Application**<br>• Packaging Operator to monitor label application — ensuring correct positioning and adhesion on packaging. Line checks every 30 minutes to verify consistency. ✔ Acceptance: Label applied correctly, no skew or detachment. ✖ Rejection: Misaligned, detached, or missing label. Actions on Rejection:<br>• i) Hold and segregate all affected packaged product; adjust label applicator equipment as required; perform verification check on corrective adjustment<br>• ii) QA Analyst to approve before restarting production. | Packaging Operator , QA Analyst (for respective actions) | 30 min interval during shift |
| 5. | **Label Verification (In-Process)**<br>• QA Analyst conducts hourly line inspections to verify: - product name.<br>• - net weight<br>• - ingredient list<br>• - shelf life<br>• - Storage instructions<br>• - manufacturer details<br>• - Legibility - Correct product information - Date code/lot code clarity - Regulatory declarations ✔ Acceptance: Fully compliant labelling . ✖ Rejection: Labelling error identified. Actions on Rejection:<br>• QA Analyst to immediately stop line operation; quarantine affected batch for further inspection.<br>• ii) Issue Non-Conformance Report (NCR); perform 100% label inspection if required and update records in SAP QM<br>• iii) Initiate corrective and preventive actions where necessary. | QA Analyst | Hourly during shift |
| 6. | **Post-Packaging Label Verification**<br>• QA Supervisor performs random verification of finished product in the warehouse pre-dispatch: - Correct SKU - Label match - No mix-up or stock contamination. ✔ Acceptance: Matches batch record, traceable. ✖ Rejection: Label mismatch or non-conformance. Actions on Rejection:<br>• i) Immediately quarantine affected stock, initiate root cause analysis with relevant departments.<br>• ii) Document corrective action plan; ensure proper updates are logged in SAP.<br>• iii) Release product only after QA Manager’s confirmation. | QA Supervisor , QA Manager (for respective actions) | Per line, pre-dispatch |
| 7. | **Label Material Control**<br>• Warehouse Section Head to ensure label rolls / sheets are issued per batch and reconciled post-production. Leftover labels returned and controlled. ✔ Acceptance: Label inventory reconciled and logged in SAP. ✖ Rejection: Label stock not reconciled. Actions on Rejection:<br>• i) Conduct full physical inventory count of label materials; investigate discrepancies between issued and returned labels.<br>• ii) Notify QA and Procurement of variance; implement corrective measures. | Warehouse Section Head , QA & Procurement Manager’s (for respective actions) | Per batch issue |
| 8. | **Non-Conformance Handling**<br>• QA Manager to manage any labelling deviation: - Raise NCR - Conduct root cause analysis (RCA) - Implement corrective/preventive actions (CAPA). ✔ Acceptance: Non-conformance closed with documented CAPA. ✖ Rejection: Repeated labelling deviations. Actions on Rejection:<br>• i) Escalate issue to Production Manager and cross-functional team for systemic review; initiate detailed review of processes and staff competency; revise SOP or provide targeted retraining as required; document preventive measures. | QA Manager | As needed (non-conformance) |
| 9. | **SAP Interface**<br>• - All label version approvals tracked in SAP Document Module. - Label material batch usage recorded in SAP MM. - Label verification (in-process / post-process) logged in SAP QM. - Non-conformance, NCR and CAPA entered in SAP QM. ✔ Acceptance: SAP fully updated; audit ready . ✖ Rejection: Missing SAP records or incomplete data. Actions on Rejection:<br>• Data Entry Operator to immediately update missing SAP entries; verify all related SAP data accuracy with QA Supervisor; confirm readiness for audit review. | Data Entry Operator , QA Supervisor (for respective actions) | Per batch closure |

Flowchart:

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Product Labelling  

**Roles / Swimlanes:**
- Regulatory Affairs Specialist  
- QA  
- Packaging Operator  
- Warehouse Supervisor  

---

### Steps

| Step # | Role                       | Action                                                                                                                                      | Decision/Next Step                                                                                                  |
|--------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Start  | Regulatory Affairs Specialist | Start                                                                                                                                       | Next: Step 1                                                                                                        |
| 1      | Regulatory Affairs Specialist | Prepares master artwork and Label content. Obtain Approvals from QA and Document Control and archive. (A/M)                               | Next: Step 2                                                                                                        |
| 2      | QA                         | Verify the latest approved template is used and Printer settings (M)                                                                       | Next: Step 3                                                                                                        |
| 3      | QA                         | **Decision:** Correct template version available?                                                                                           | If **Yes**: go to Step 4. If **No**: go to Step 3.1                                                                 |
| 3.1    | QA                         | Halt printing, load correct version                                                                                                         | After loading correct version, return to Step 3                                                                     |
| 4      | Packaging Operator         | print labels or operate label applicator with pre-printed materials. (M)                                                                   | Next: Step 4.1                                                                                                      |
| 4.1    | QA                         | Check first-off sample: Legibility, Accuracy, log start of batch printing in SAP (M)                                                       | Next: Step 5                                                                                                        |
| 5      | QA                         | Performs hourly line inspection (M)                                                                                                        | Next: Step 6                                                                                                        |
| 6      | QA                         | **Decision:** Correct template version available?                                                                                           | If **Yes**: go to Step 7. If **No**: go to Step 6.1                                                                 |
| 6.1    | QA                         | Stop line, isolate affected units, issue NCR                                                                                                | Next: Step 9                                                                                                        |
| 7      | Packaging Operator         | Ensure correct label placement and adhesion. (M)                                                                                            | Next: Step 8                                                                                                        |
| 8      | QA                         | Verifies Label match with SKU, Correct batch linkage, No stock mix-up, Sample pulled from warehouse before dispatch (M)                    | Next: Step 10                                                                                                       |
| 9      | QA                         | Any labeling deviation: Raised as NCR/CA + CAPA conducted. QA to document in SAP QM (A/M)                                                  | Next: Step 10                                                                                                       |
| 10     | Warehouse Supervisor       | Reconciles label rolls issued vs. used. Returns leftovers to store. (M)                                                                    | Next: Step 11                                                                                                       |
| 11     | Warehouse Supervisor       | Label version, batch usage, inspections, and non-conformance logs are updated (M)                                                          | Next: End                                                                                                           |
| End    | Warehouse Supervisor       | End                                                                                                                                         | —                                                                                                                   |

---

### Explicit Yes/No Branches

- **Step 3 – Correct template version available?**  
  - **Yes →** Step 4 (print labels or operate label applicator).  
  - **No →** Step 3.1 (Halt printing, load correct version, then return to Step 3).

- **Step 6 – Correct template version available?**  
  - **Yes →** Step 7 (Ensure correct label placement and adhesion).  
  - **No →** Step 6.1 (Stop line, isolate affected units, issue NCR → Step 9).

---

### Mermaid.js Flow

```mermaid
graph TD

    Start([Start]) --> S1[1. Prepares master artwork and Label content. Obtain Approvals from QA and Document Control and archive. (A/M)]
    S1 --> S2[2. Verify the latest approved template is used and Printer settings (M)]
    
    D3{3. Correct template version available?}
    S2 --> D3
    D3 -- Yes --> S4[4. print labels or operate label applicator with pre-printed materials. (M)]
    D3 -- No --> S3_1[3.1 Halt printing, load correct version]
    S3_1 --> D3

    S4 --> S4_1[4.1 Check first-off sample: Legibility, Accuracy, log start of batch printing in SAP (M)]
    S4_1 --> S5[5. Performs hourly line inspection (M)]

    D6{6. Correct template version available?}
    S5 --> D6
    D6 -- Yes --> S7[7. Ensure correct label placement and adhesion. (M)]
    D6 -- No --> S6_1[6.1 Stop line, isolate affected units, issue NCR]

    S7 --> S8[8. Verifies Label match with SKU, Correct batch linkage, No stock mix-up, Sample pulled from warehouse before dispatch (M)]
    S6_1 --> S9[9. Any labeling deviation: Raised as NCR/CA + CAPA conducted. QA to document in SAP QM (A/M)]

    S8 --> S10[10. Reconciles label rolls issued vs. used. Returns leftovers to store. (M)]
    S9 --> S10

    S10 --> S11[11. Label version, batch usage, inspections, and non-conformance logs are updated (M)]
    S11 --> End([End])
```