---
Department: ANNEXURES
Section: ANNEXURE XVII – Product Recall / Return
Section_Kind: appendix
Section_Priority: low
Source: Production Flour Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## ANNEXURE XVII – Product Recall / Return

              a. Product Recall / Return - Escalation Protocol:

| Situation | Escalate To | Timeline |
| --- | --- | --- |
| Delay in recall decision or risk classification (> 2 hrs) | QA Manager → COO Manager | Immediate |
| Delay in notification to SFDA or customers (> 24 hrs) | QA Manager → COO → Legal/Government Relations Specialist | Immediate |
| Failure in traceability identification (batch cannot be found in SAP) | QA Manager → SAP Specialist → Branch Manager  Production Director  COO | Immediate |
| Incomplete product recovery (< 95% target recovery) | QA Manager → Recall Committee → Production Director  COO | Within 24 hrs of issue detection |
| Any deviation in disposal or records | QA Manager → Production Director | Immediate |
| Repeated recall or systemic issue | QA Manager → Production Director → Board Representative | Within 48 hrs |

              b. Product Recall / Return - Records & Documentation:

| Record Name | Purpose | Location | Retention Period |
| --- | --- | --- | --- |
| Recall / Return Decision Form | To document official decision to initiate recall | QA Department Files / SAP QM | Minimum 3 years |
| Risk Assessment Reports | To assess risk and classify recall severity | QA Department Files / SAP QM | Minimum 3 years |
| Recall / Return Notification Records | Record of notifications sent to SFDA, customers, other authorities | QA Department Files / SAP QM | Minimum 3 years |
| Traceability Reports (SAP) | Full traceability for affected batch(es) | SAP Traceability Module | Minimum 3 years |
| Product Recovery Logs | Detailed log of recovered product quantities and locations | QA Department Files / SAP QM | Minimum 3 years |
| Disposal Records | Document controlled disposal of affected product | QA Department Files / SAP QM | Minimum 3 years |
| Recall / Return Effectiveness Reports | Summary of recovery % and recall outcome | QA Department Files / SAP QM | Minimum 3 years |
| Mock Recall Reports | Evidence of periodic testing of recall system | QA Department Files / SAP QM | Minimum 3 years |
| Corrective Action Reports (Post-recall) | Document corrective and preventive actions after recall | QA Department Files / SAP QM | Minimum 3 years |

              c. Product Recall / Return - Verification & Review:

| Verification Activity | Responsibility | Frequency | Output / Record |
| --- | --- | --- | --- |
| Conduct Mock Recall (full test of traceability and recovery) | QA Manager | Annually (minimum) | Mock Recall Report |
| Review and update Recall Plan and Team roles | QA Manager | Annually | Revised Recall Plan Document |
| Report effectiveness of mock recalls in Management Review | QA Manager | Annually (part of Management Review) | Management Review Minutes |
| Implement continuous improvement based on test results and real recall learnings | QA Manager + Recall Team | After each recall or mock recall | Updated Recall Procedure / Corrective Action Report |

              d. Flowchart:

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Product Recall Escalation  

**Roles / Swimlanes:**
- QA  
- Regulatory Affairs  

---

### Steps

| Step # | Role / Swimlane | Action / Decision | Decision / Next Step |
|--------|------------------|-------------------|----------------------|
| Start | QA | Start | Proceed to Step 1. |
| 1 | QA | Identifies a potential issue. Logs incident in SAP QM and initiates internal investigation (M). | Proceed to Step 2. |
| 2 | QA | Assess severity, product scope, and potential consumer impact. (M) | Proceed to Step 3. |
| 3 | QA | Decision: Is Escalation Warranted? | **Yes:** Proceed to Step 4.  **No:** Proceed to Step 3.1. |
| 3.1 | QA | Close issue as non-recall deviation with CAPA (M). | Process ends (implicit). |
| 4 | QA | Informs the Recall Committee. Formal Recall Decision Form is initiated. Risk assessment report is completed (M). | Proceed to Step 5. |
| 5 | Regulatory Affairs | Drafts notification letter. Notify SFDA or other relevant authority. Provide traceability, quantity affected, and risk details (M). | Proceed to Step 6. |
| 6 | QA | Prepare product withdrawal notice. Communicate via email, phone, or official letters. Record acknowledgment. (M) | Proceed to Step 7. |
| 7 | QA | Stop all shipments of affected batches. Quarantine available stock. Coordinate with customers and record returned quantities (MO | Proceed to Step 8. |
| 8 | QA | Recall status reviewed daily. Any delays, non-cooperation, or serious findings are escalated to CEO. (M) | Proceed to Step 9. |
| 9 | Regulatory Affairs | Conduct recall effectiveness check. Prepare and Submit report to SFDA and archive per retention policy (M) | Proceed to End. |
| End | Regulatory Affairs | End | — |

---

```mermaid
graph TD

    start((Start))

    s1[1. Identifies a potential issue. Logs incident in SAP QM and initiates internal investigation (M).]
    s2[2. Assess severity, product scope, and potential consumer impact. (M)]
    d3{3. Is Escalation Warranted?}
    s31[3.1 Close issue as non-recall deviation with CAPA (M).]
    s4[4. Informs the Recall Committee. Formal Recall Decision Form is initiated. Risk assessment report is completed (M).]
    s5[5. Drafts notification letter. Notify SFDA or other relevant authority. Provide traceability, quantity affected, and risk details (M).]
    s6[6. Prepare product withdrawal notice. Communicate via email, phone, or official letters. Record acknowledgment. (M)]
    s7[7. Stop all shipments of affected batches. Quarantine available stock. Coordinate with customers and record returned quantities (MO]
    s8[8. Recall status reviewed daily. Any delays, non-cooperation, or serious findings are escalated to CEO. (M)]
    s9[9. Conduct recall effectiveness check. Prepare and Submit report to SFDA and archive per retention policy (M)]
    end((End))

    start --> s1 --> s2 --> d3

    d3 -- "No" --> s31 --> end
    d3 -- "Yes" --> s4 --> s5 --> s6 --> s7 --> s8 --> s9 --> end
```