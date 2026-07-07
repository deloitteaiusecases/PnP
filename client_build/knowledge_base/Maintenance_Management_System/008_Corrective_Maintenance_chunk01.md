---
Department: Maintenance Management System
Section: Corrective Maintenance
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Corrective Maintenance
Source: Maintenance Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 0
---

## Corrective Maintenance

Introduction and Background of the Section
Corrective Maintenance (CM) refers to reactive maintenance activities carried out to restore equipment to its operational condition following an unexpected failure, anomaly, or breakdown. At Arabian Mills, corrective maintenance is executed under a structured and traceable system that leverages the SAP Plant Maintenance (SAP PM) module to ensure accountability, timeliness, and cost control.
While preventive maintenance aims to avoid breakdowns, corrective maintenance is critical for addressing unforeseen events promptly and safely. A disciplined CM system ensures minimum disruption to production and allows valuable failure data to be captured for future improvements.
CM at Arabian Mills is based on the principles of ISO 14224, TPM pillar for Breakdown Maintenance, and Reliability-Centered Maintenance (RCM) to ensure quality and continuous improvement.
Policy
 All equipment failures or abnormal observations must be immediately reported and documented via SAP PM notifications.
 No corrective action shall be taken unless a work order is generated and approved, except for emergency situations.
 Each breakdown must be logged with failure mode, timestamp, equipment ID, symptoms, and operating condition to enable later Root Cause Analysis (RCA).
 Work order priorities shall be assigned based on safety, production impact, and cost implications, following the predefined priority matrix.
 Safety, hygiene, and product quality standards must be upheld during all CM activities.
 Root cause data from corrective maintenance shall be analyzed periodically to reduce recurring failures.
 Emergency CM interventions shall follow an expedited SAP workflow for logging, resolution, and analysis.
 All CM activities, material usage, and technician hours must be recorded in SAP. Data will be reviewed periodically to identify recurring faults and performance trends.
Corrective Maintenance Procedure Breakdown

| S. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Failure Identification**<br>• Detect and report equipment malfunction or deviation. | Operator | As incidents occur |
| 2 | **Notification Creation**<br>• Create SAP breakdown notification with equipment ID, problem description, and timestamp. | Technician | As incidents occur |
| 3 | **Notification Review**<br>• Review the notification details for completeness and accuracy. | Supervisor | As incidents occur |
| 4 | **Work Order Creation and Priority Assignment**<br>• Convert valid notifications into work orders. Assign priority using the plant priority matrix. | Maintenance Planner | As incidents occur |
| 5 | **Job Planning**<br>• Define job scope, resource requirements, tools, and duration. Update this information in SAP. | Maintenance Planner | As Required |
| 6 | **Material Requisition**<br>• Raise a material reservation or purchase requisition in SAP for required spares, tools, or consumables. | Supervisor | As Required |
| 7 | **Material Issuance**<br>• Issue parts and materials from stores against the work order. | Stores Team | Per Job |
| 8 | **Repair Execution**<br>• Carry out repair tasks per SAP work order. Record task completion and observations. | Technician | Per Job |
| 9 | **Supervisory Monitoring**<br>• Verify execution quality, ensure LOTO and safety compliance, and update SAP with work status. | Supervisor | Per Job |
| 10 | **Equipment Testing and Handover**<br>• Conduct post-repair testing and release the equipment for operation. | Technician | Per Job Completion |
| 11 | **Work Order Closure – Documentation**<br>• Review all logged details (time, materials used, and technician remarks). Return unused materials to stores and record returns in SAP. | Supervisor | Daily |
| 12 | **Work Order Closure – SAP Completion**<br>• Technically complete the work order in SAP, entering final fault codes and resolution status. | Maintenance Planner | Daily |
| 13 | **Root Cause Analysis**<br>• Initiate root cause analysis for repeated or critical failures. Document findings and attach to SAP work order. | Maintenance Manager | As Needed |
| 14 | **Reporting and Dashboard Preparation**<br>• Prepare reports on breakdown frequency and common failure modes using SAP data. | SAP PM Administrator | Monthly |
| 15 | **KPI and Trend Review**<br>• Review CM performance reports and identify improvement opportunities. | Maintenance Director | Monthly |

Corrective Maintenance Priority Matrix
Here is a Corrective Maintenance Priority Matrix for a wheat milling and animal feeds plant, using Safety, Production Impact, and Cost Implications as the three main criteria. The matrix helps determine the priority level for corrective maintenance work orders:

| Priority Level | Safety Impact | Production Impact | Cost Implication | Response Time | Example |
| --- | --- | --- | --- | --- | --- |
| P1 – Emergency | High risk to personnel or plant safety | Complete production stoppage or major process loss | High risk of significant equipment damage or regulatory penalty | Immediate (within 1 hour) | Fire hazard, exposed live wires, breakdown of main wheat mill drive motor |
| P2 – Urgent | Moderate safety concern (potential to escalate) | Partial line stoppage or major bottleneck | Significant loss if delayed but not catastrophic | Within 4 hours | Sifter blockage, pneumatic line rupture, elevator belt damage |
| P3 – High | No immediate safety risk, but recurring failure | Quality deviation or throughput reduction | Costly if ignored or repeated failure history | Within 24 hours | Vibrating roller mill, abnormal bearing noise, airlock motor overheating |
| P4 – Medium | Minor concern, isolated to a safe condition | No immediate production loss | Minor cost or easily controlled workaround | Within 3 working days | Faulty sensor on a redundant system, misalignment of chute |
| P5 – Low | No safety or production risk | No disruption to operations | Low value maintenance or cosmetic issue | As scheduled / backlog item | Paint touch-up, loose covers, non-functional indicator lamp on control panel |

Priority Assignment Guidelines
 P1: Must be escalated immediately to the Maintenance Manager.
 P2: Reviewed by the Production Maintenance Manager and escalated for resolution
 P3: Reviewed daily during maintenance planning by the maintenance supervisor; scheduled within 24 hours.
 P4: Bundled with planned maintenance or scheduled during low load.
 P5: Added to the backlog list and considered in weekly planning meetings.
Responsibility for Assignment
 Initial Notification: Technician or Operator
 Priority Review and Assignment: Maintenance Planner, with validation by Supervisor or Maintenance Manager based on defined criteria.
Roles and Responsibilities

| Role | Responsibilities |
| --- | --- |
| Maintenance Director | Oversees CM performance, ensures root cause review, and monitors SAP CM data integrity |
| Production Maintenance Manager | Converts notifications into work orders for the PM prioritizes jobs, and schedules repairs, It is Report to the branch maintenance manager . |
| Maintenance Planner | Converts notifications into work orders, prioritizes jobs, and schedules repairs |
| Maintenance Manager | Analyzes failure data, leads RCA, and proposes reliability improvements |
| Supervisor | Allocates tasks, enforces safety, and ensures SAP entries are complete and timely |
| Technician | Executes repair tasks, follows safety protocols, and updates SAP task completion |
| SAP PM Administrator | Supports configuration of corrective workflows and report customization |
| Safety Officer | Ensures all safety protocols including LOTO and PPE are applied |
| Stores & Inventory Team | Confirms availability of critical spares and materials for emergency breakdowns |