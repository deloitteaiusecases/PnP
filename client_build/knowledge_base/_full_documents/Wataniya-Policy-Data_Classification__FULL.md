---
Department: FULL_DOCUMENT
Section: FULL_DOCUMENT
Section_Kind: full_document
Section_Priority: high
Source: Wataniya-Policy-Data Classification.docx
Document_Title: Wataniya-Policy-Data Classification
Document_Class: full_document
Document_View: full
Is_Full_Document: true
---

| GAP ANALYSIS DOCUMENT Policy & Procedure Document |
| --- |

| Document Number | Wataniya-Policy-Data Classification |
| --- | --- |
| Version | 1.0 |
| Effective Date | 09 June 2026 |
| Department | — |
| Document Owner | Policy Owner |
| Approved By | Compliance Head |
| Classification | Confidential – Internal Use Only |
| Next Review Date | 12 months from effective date |
Gap Analysis Report
Date: 2026-06-09 | Prepared by: Policy Intelligence System
---
1. Executive Summary
The client has a relatively mature set of information security and data-handling procedures (classification, media disposal, incident management) and has recently introduced a more advanced, NDMO-aligned Data Classification Policy (Wataniya) with clear roles and methodology. However, this new practice is only partially reflected in the existing Information Security / Data Management & Compliance manual (Arabian Mills), resulting in fragmented governance, inconsistent terminology, and weak linkage between classification levels and technical controls (e.g., masking, access control).
Most gaps are governance and documentation related and rated 🟡 MEDIUM, as they can undermine compliance with Saudi data protection and cybersecurity regulations if not addressed. The primary risk is inconsistent treatment of highly sensitive and personal data across systems and entities, potentially leading to misclassification, mishandling and weak evidencing of compliance. The single most urgent action is to issue and approve a unified, enterprise-wide Data Classification Standard that reconciles the two schemes, embeds NDMO/PDPL requirements, and is integrated into the existing Information Security Procedure.
---
2. Current Practice vs. Policy Comparison

| # | Area | Current Practice (Wataniya – Data Classification Policy) | Policy Requirement (Existing InfoSec / Data Management & Compliance) | Status |
| --- | --- | --- | --- | --- |
| 1 | Data classification levels & scheme | Uses NDMO‑aligned levels (Top Secret, Secret, Confidential‑Internal, Confidential‑External, Public) with impact-based mapping. | Uses four levels (Strictly Confidential, Confidential, Internal, Public) with basic examples; no explicit NDMO mapping or split between internal/external confidential data. | 🟡 Partial |
| 2 | Governance & roles for classification | Formal roles defined: DMSC, DPO, Data Governance Officer, Business Data Executive, Business Data Steward, Data Custodians, Information Security Department, Data Users. | Classification section assigns responsibility mainly to Cybersecurity/IT & Cybersecurity Manager and “asset owners”; no DPO/DGO/Data Steward/Custodian roles or RACI defined. | 🔴 Gap |
| 3 | Classification methodology & impact assessment | Three‑phase method (Data Identification, Impact Assessment, Classification); detailed impact categories (national interest, entity activities, individuals, environment) and scoring based on SDAIA model. | Requires classification “in terms of value, legal requirements, sensitivity, and criticality” but does not define a structured, standardised impact assessment method or scoring. | 🟡 Partial |
| 4 | Default handling of unclassified data | Any data without explicit classification is treated as “Internal” until classified; explicit rule. | No explicit default classification rule in the classification section. | 🟢 Aligned (practice exceeds policy) |
| 5 | Linkage of classification to technical controls (masking, pseudonymisation, access control) | Explicitly requires masking/pseudonymisation of restricted data before analytics/sharing and classification‑driven access/storage/transfer decisions. | InfoSec classification and media disposal procedures do not explicitly require masking/pseudonymisation or map classification levels to specific security controls beyond general confidentiality. | 🔴 Gap |
| 6 | Integration with media disposal & data sanitisation | Uses NDMO‑aligned categories; does not yet explicitly cross‑reference the existing Media Disposal / Data Sanitisation procedures. | Media Disposal procedure and Data Sanitisation procedure are in place and refer to “Strictly Confidential/Confidential” information, with approvals and retention of forms, but not to the new Top Secret/Secret/Confidential‑Internal/External scheme. | 🟡 Partial |
| 7 | Training, awareness & KPIs for classification | Requires regular training, awareness and KPI monitoring by DMSC, DPO, DGO and Cyber Security Team on data classification; explicit objective to build a “culture of responsible data management”. | Incident training and awareness are defined; the classification section itself has no explicit training, KPI or audit requirements linked specifically to data classification. | 🟡 Partial |
| 8 | Coverage of internal vs. external stakeholders | Policy explicitly applies to “all internal and external stakeholders” interacting with Wataniya data (including auditors, risk functions, etc.). | InfoSec manual states recipients must handle information per classification, but is written primarily for internal staff; third‑party alignment is not clearly spelled out within the classification section. | 🟢 Low misalignment (largely covered elsewhere – supplier/IT contracts not seen) |
Legend: ✅ Aligned / 🟡 Partial / 🔴 Gap / ⬜ No Policy
---
3. Detailed Gap Analysis
#### 3.1 Critical Gaps 🔴 HIGH
Based on the documents provided, no direct HIGH (regulatory-critical) gaps can be confirmed solely from the data classification perspective. Most issues are governance and integration gaps that pose medium operational and regulatory risk if left unresolved.
#### 3.2 Significant Gaps 🟡 MEDIUM
Gap 1: Fragmented Data Classification Governance and Roles
Current state:
Wataniya’s Data Classification Policy defines an extensive governance structure (DMSC, DPO, DGO, Business Data Executives/Stewards, Data Custodians, Information Security Department, Data Users) with clear accountability for classification, labelling, approvals and monitoring.
The existing Arabian Mills Information Security / Data Management & Compliance manual assigns responsibility mainly to the Cybersecurity/IT & Cybersecurity Manager and generic “asset owners”, without reflecting the DMSC/DPO/DGO/Steward/Custodian roles or a RACI.
Required state:
A single, consolidated governance model for data classification that:
Formally recognises DMSC, DPO, DGO, Data Executives/Stewards and Data Custodians.
Is embedded in the Information Security Procedure and related manuals.
Provides a clear RACI for classification, labelling, access approvals, monitoring, declassification and exception handling.
Risk:
Overlapping and unclear responsibilities across policies can lead to inconsistent classification and handling of highly sensitive and personal data, weak lines of defence, and difficulty evidencing regulatory compliance in audits or investigations.
Regulatory basis: see Regulatory References – G1, G2.
Immediate action:
Within 30 days, IT & Cybersecurity Manager and DMSC to jointly draft and approve a unified Data Classification Governance Charter that reconciles roles in both documents and includes a RACI; use this as the basis for updating the Information Security / Data Management & Compliance manual.
---
Gap 2: Incomplete Mapping of Classification Levels to Security Controls (Masking, Pseudonymisation, Access, Storage and Transfer)
Current state:
Wataniya’s policy explicitly states that restricted data shall be protected before sharing for analytics and other purposes using techniques such as data masking and pseudonymisation, and that classification should drive access, storage and transfer decisions.
The existing Information Security manual’s classification and media disposal sections define levels and basic handling (e.g., labels, disposal approvals) but do not:
Map each level (Strictly Confidential/Confidential/Internal/Public or Top Secret/Secret/Confidential‑Internal/External/Public) to concrete technical controls (encryption standards, DLP rules, masking, anonymisation, access restrictions, logging requirements).
Address classification-driven masking/pseudonymisation for analytics and data sharing.
Required state:
A formal Data Protection Control Matrix that links each classification level to specific mandatory controls (e.g., encryption in transit/at rest, masking requirements, access control patterns, logging, secure transfer and storage requirements), aligned with Wataniya’s NDMO-based scheme and applied consistently in the Information Security Procedure.
Risk:
High-value and personal data classified as Top Secret/Secret/Confidential could be stored, shared or analysed without appropriate masking, encryption or access controls, increasing the likelihood and impact of data breaches, unlawful disclosures or misuse of personal data.
Regulatory basis: see Regulatory References – G1, G2.
Immediate action:
Within 60 days, Information Security Department and Data Custodians to develop and approve a classification-to-control matrix and incorporate it into the Information Security Procedure and technical standards (e.g., DLP, encryption, access control configurations).
---
Gap 3: Lack of a Standardised, Documented Impact Assessment Method in the Core InfoSec Manual
Current state:
Wataniya’s Data Classification Policy includes a detailed three-phase methodology (Data Identification, Data Impact Assessment, Data Classification), and a questionnaire-based impact model aligned to SDAIA categories (national interest, entity activities, individuals, environment) with scoring (High/Medium/Low/None).
The existing Information Security / Data Management & Compliance manual only states that information must be classified “in terms of its value, legal requirements, sensitivity and criticality” without a detailed, standard process, scoring method, or reference to the SDAIA/NDMO impact categories.
Required state:
A single, documented impact assessment method, referenced in the Information Security manual, that is aligned to the NDMO/SDAIA impact framework and is mandatory for Business Data Executives/Stewards when assigning or revising classification levels.
Risk:
Different teams may apply inconsistent criteria, resulting in under‑classification of data with high national, regulatory or personal risk or over‑classification that impedes business use; this undermines risk-based protection and may weaken regulatory compliance evidence.
Regulatory basis: see Regulatory References – G2, G3.
Immediate action:
Within 45 days, Data Governance Officer and DPO to embed the Wataniya impact assessment questionnaire and scoring model as an annex to the Information Security / Data Management & Compliance manual and roll out a mandatory procedure for its use in all new and revised classifications.
---
#### 3.3 Improvement Opportunities 🟢 LOW
**Terminology harmonisation between schemes**
Issue: Existing InfoSec manual uses “Strictly Confidential/Confidential/Internal/Public”, while Wataniya uses “Top Secret/Secret/Confidential‑Internal/Confidential‑External/Public”.
Recommendation: Map and harmonise terminology (e.g., Strictly Confidential ↔ Top Secret; Confidential ↔ Secret/Confidential‑Internal) in a single reference table and update forms, labels and training accordingly.
**Explicit default classification rule in core manual**
Issue: Wataniya practice assumes unclassified data is “Internal”; this is not explicitly captured in the Information Security manual.
Recommendation: Add a one‑line rule in the classification section that any unclassified information is to be treated as Internal by default until formally classified.
**Third-party alignment statement**
Issue: Classification obligations for external processors and partners are clear in Wataniya policy but not explicitly reiterated in the classification section of the InfoSec manual.
Recommendation: Add a short clause that all third parties accessing data must comply with the organisation’s classification and handling rules, to be reflected in contracts and NDAs.
**Cross-reference between classification and Incident Management**
Issue: Incident Management procedure is strong but does not explicitly reference classification levels when prioritising or handling data breaches.
Recommendation: Update incident triage guidance so that incidents involving Top Secret/Secret/Confidential‑External data are automatically treated at higher severity levels (e.g., S4–S5).
---
4. Compliance Risk Register

| # | Issue | Severity | Regulatory Basis* | Consequence | Recommended Action |
| --- | --- | --- | --- | --- | --- |
| 1 | Fragmented data classification governance and unclear roles (DMSC/DPO/DGO vs Cybersecurity Manager/asset owners) | 🟡 MEDIUM | See Regulatory References – G1, G2 | Inconsistent application of classification rules, weak accountability, difficulty evidencing compliance in audits or investigations. | Approve unified Data Classification Governance Charter and RACI; update Information Security manual to reflect roles. |
| 2 | No formal mapping from classification levels to concrete technical controls (masking, encryption, access control, logging) | 🟡 MEDIUM | See Regulatory References – G1, G2 | Inadequate protection of highly sensitive and personal data; increased likelihood/impact of data breaches and regulatory sanctions. | Develop and approve classification-to-control matrix; embed in Information Security Procedure and technical standards. |
| 3 | Impact-based classification method not embedded in core InfoSec manual | 🟡 MEDIUM | See Regulatory References – G2, G3 | Non-uniform classification across domains; risk of under‑protecting critical data; weak justification for classification decisions. | Incorporate impact assessment model and questionnaire into the Information Security manual and make it mandatory. |
| 4 | Terminology misalignment between existing and new classification schemes | 🟢 LOW | – | User confusion; mislabelling; training complexity; minor risk of mis‑handled data. | Publish mapping between levels; standardise terminology in policies, forms and training. |
| 5 | Default classification and third‑party obligations not explicitly codified in core manual | 🟢 LOW | – | Minor ambiguity on handling of unlabelled data and third‑party compliance. | Add concise clauses to Information Security manual for default “Internal” handling and third‑party adherence to classification rules. |
\*Regulations and article numbers are listed in full in the Regulatory References section.
---
5. Recommended Actions

| Priority | Action | Policy/Control Impacted | Owner | Timeline | Success Metric |
| --- | --- | --- | --- | --- | --- |
| 1 | Develop and approve a unified Data Classification Governance Charter (covering DMSC, DPO, DGO, Business Data Executives/Stewards, Data Custodians, InfoSec, Data Users) and corresponding RACI. | Data Management & Compliance section; Data Classification Policy | Data Management Steering Committee (DMSC) with IT & Cybersecurity Manager | 0–30 days | Charter approved; RACI published; 100% of key roles formally nominated. |
| 2 | Update the Information Security / Data Management & Compliance manual to harmonise classification levels with the Wataniya scheme and explicitly reference the unified governance structure. | Information Security Procedure – Data Management & Compliance | IT & Cybersecurity Manager | 30–60 days | Revised manual approved; obsolete terminology removed; all related procedures cross‑referenced. |
| 3 | Create a Data Classification-to-Control Matrix (per level: required masking/pseudonymisation, encryption, access control, logging, transfer/storage rules) and integrate it into technical standards (DLP, IAM, backup). | Technical Security Standards; Data Classification Policy | Information Security Department & Data Custodians | 30–90 days | Matrix approved; at least 80% of critical systems configured according to it; no unprotected Top Secret/Secret datasets in initial review. |
| 4 | Embed the SDAIA/NDMO-aligned impact assessment method and questionnaire into the Information Security / Data Management & Compliance manual and mandate its use for all new/revised data classifications. | Data Classification Procedure | Data Governance Officer & DPO | 30–60 days | Procedure approved; 100% of new classification decisions documented with completed impact assessment. |
| 5 | Roll out targeted training and awareness for Data Executives, Stewards, Custodians and users covering the unified classification scheme, governance roles, and new control matrix. | Training & Awareness Programme | DPO & IT & Cybersecurity Manager | 60–90 days | ≥95% of identified stakeholders trained; post‑training assessment average score ≥80%; reduction in classification errors reported in first 6 months. |
| 6 | Update Incident Management and Media Disposal/Data Sanitisation procedures to reference the harmonised classification levels and treat incidents involving higher levels as higher severity. | Incident Management; Media Disposal; Data Sanitisation | IT & Cybersecurity Manager | 60–90 days | Updated procedures approved; severity mapping documented; first incident simulation reflects new prioritisation. |
---
6. Implementation Roadmap
Immediate (0–30 days)
Finalise and approve the unified Data Classification Governance Charter and RACI (Action 1).
Communicate interim guidance that, until manuals are updated, the Wataniya classification levels and governance model take precedence where more stringent.
Short-term (30–90 days)
Revise the Information Security / Data Management & Compliance manual to:
Harmonise terminology and levels with the Wataniya policy.
Reference DMSC, DPO, DGO, Business Data Executives/Stewards, Data Custodians.
Embed the SDAIA/NDMO impact assessment model and default “Internal” rule.
Develop and implement the classification-to-control matrix across key systems (DLP, IAM, storage, backup).
Update Incident Management and Media Disposal/Data Sanitisation procedures to align with the harmonised levels.
Deliver targeted training for all classification stakeholders.
Ongoing (90+ days)
Run periodic (at least annual) audits on correct application of classification levels and controls, led by Cyber Security / DPO.
Use KPIs and dashboards (e.g., number of misclassified assets, incidents by classification level, percentage of analytics datasets masked) to monitor maturity and drive continuous improvement.
Reassess data classifications annually and after major business or regulatory changes, as required by the Wataniya policy.
---
Regulatory References
G1 – Personal Data Protection Law (PDPL), promulgated by Royal Decree No. M/19 dated 09/02/1443H (corresponding to 16/09/2021), Article 19: obliges data controllers to take necessary organisational and technical measures to ensure the preservation, confidentiality and security of personal data, including protection against unauthorised access, disclosure, alteration or destruction.
G2 – National Data Governance Interim Regulations issued by the National Data Management Office (NDMO), Article 9 (Data Classification and Handling): requires entities to classify data according to sensitivity and criticality, assign clear responsibilities for data management and apply commensurate protection measures, including for sharing and reuse.
G3 – National Data Management and Personal Data Protection Standards (NDMO), Section 3.2 – Data Classification and Impact Assessment (treated as Article 3.2 for the purposes of this analysis): sets out requirements for risk‑based impact assessment (national interest, entity activities, individuals, environment) and for mapping impact levels (High/Medium/Low/None) to data classification levels and protection controls.
These regulations collectively underpin the need for unified governance, risk‑based data classification, and classification‑driven security controls across the organisation.
1  REVISION HISTORY

| Version | Date | Description | Prepared By | Approved By |
| --- | --- | --- | --- | --- |
| 1.0 | 09 June 2026 | Initial release | Policy Owner | — |
2  APPROVAL & AUTHORIZATION

| Role | Name | Signature | Date |
| --- | --- | --- | --- |
| Prepared By | Policy Owner |  |  |
| Reviewed By | — |  |  |
| Approved By | Compliance Head |  |  |
DISCLAIMER: Generated by AI-assisted policy tool. Must be reviewed and approved by authorized personnel before official use.
3  SOURCES REFERENCED
Production Feed Flour Policy and Procedure.docx
Marketing Policies and procedures.docx
Information Security Procedure.docx
SCM_Procurement Policy and Procedures.docx
Production Flour Policy and Procedures.docx
Accounting Principles and procedures.docx
7_Document_and_Content_Data_Management__12_.docx
5_Data_Quality_.docx