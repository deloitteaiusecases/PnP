---
Department: Performance Monitoring
Section: Maintenance KPIs
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Maintenance KPIs
Source: Maintenance Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 0
---

## Maintenance KPIs

Introduction and Background of the Section
Maintenance KPIs are essential tools for monitoring how well the maintenance function supports plant availability, reliability, and cost effectiveness. This procedure introduces a broader set of KPIs that reflects global best practices and provides greater visibility into planning, execution, efficiency, and effectiveness of maintenance operations. The purpose is to establish what KPIs are tracked, how they are calculated, and how responsibility is assigned for their definition, configuration, and data integrity
Categorized Maintenance KPIs for Arabian Mills-

| KPI Category | KPI Name | Definition / Purpose | Formula / Calculation Method |
| --- | --- | --- | --- |
| Operational Performance | Downtime Hours | - Total time equipment is unavailable due to maintenance. - Measures production impact | Sum of downtime logged in SAP (minutes or hours). |
| Operational Performance | Energy Consumption per Ton | - kWh used per unit of production output. - Assesses energy efficiency of equipment. | Total energy consumed (kWh) / Total tons produced. |
| Operational Performance | Emergency Work Ratio | - Percentage of emergency maintenance work orders out of total WOs. - Indicates reactivity vs. proactivity in maintenance. | (Emergency WOs / Total WOs)  x 100 |
| Reliability | Mean Time Between Failures (MTBF) | - Average time between two successive failures of equipment. - Measures equipment reliability. | Total Operating Time / Number of Failures |
| Reliability | Mean Time to Repair (MTTR) | - Average time taken to repair equipment after failure. - Indicates speed of recovery. | Total Downtime for Failures / Number of Failures |
| Reliability | Repeat Failures | - Number of repeated failures on same equipment over time. - Flags chronic issues requiring root cause elimination. | Count of repeat failures per equipment over defined period. |
| Planning & Scheduling | Planned Maintenance Compliance (PMC) | - Percentage of PM tasks completed on time as per schedule. - Evaluates discipline in PM execution. | (PM Tasks Completed On Time / PM Tasks Scheduled)  x 100 |
| Planning & Scheduling | Schedule Compliance | - Percentage of all scheduled WOs completed in their planned period. - Tracks adherence to weekly/monthly plan. | (Scheduled WOs Completed / Total Scheduled WOs)  x 100 |
| Planning & Scheduling | Backlog Age | - Average age (in days) of open work orders. - Identifies overdue or de-prioritized work. | Average (Today' Date - WO Creation Date) for all open WOs. |
| Cost Management | Maintenance Cost per Ton | - Total maintenance cost divided by tons of product produced. - Tracks cost-efficiency of maintenance. | Total Maintenance Cost / Total Tons Produced |
| Cost Management | Spare Parts Consumption vs. Budget | - Actual spare part usage vs. allocated budget. - Ensures inventory discipline. | ((Actual Usage - Budgeted Usage) / Budgeted Usage)  x 100 |
| Technician Productivity | Work Order Completion Rate | - Percentage of assigned work orders completed by technician. - Measures technician effectiveness. | (WOs Completed by Technician / WOs Assigned)  x 100 |
| Technician Productivity | Wrench Time (%) | - Percentage of shift time spent on direct maintenance tasks. - Directly assesses labor utilization. | (Direct Maintenance Time / Total Shift Time) x 100 |
| Technician Productivity | Feedback Accuracy | - Percentage of WOs with complete and accurate technical feedback. - Indicates data quality and accountability. | (WOs with Complete Feedback / Total WOs Closed)  x 100 |
| Safety | Safety Incidents during Maintenance | - Number of safety incidents that occurred during maintenance tasks. - Tracks risk exposure and incident trend. | Count of safety incidents linked to maintenance tasks. |
| Safety | LOTO Compliance Rate | - Percentage of tasks where LOTO was correctly applied. - Ensures life-safety compliance. | (LOTO Applied Jobs / Total Jobs Requiring LOTO) x 100 |
| Safety | THA Completion Rate | - Percentage of tasks requiring THA where THA was completed. - Prevents unsafe task execution. | (THA Completed / Jobs Requiring THA)  x 100 |
| Compliance & Process | Permit Issuance Accuracy | - Percentage of tasks requiring permits where valid permits were issued. - Enforces procedural compliance. | (Correct Permits Issued / WOs Requiring Permits) x 100 |
| Compliance & Process | Inspection Checklist Utilization | - Percentage of PM tasks executed with a checklist. - Ensures task standardization. | (PM Jobs with Checklists Used / Total PM Jobs)  x 100 |
| Compliance & Process | Calibration Compliance Rate | - Percentage of instruments calibrated within their due date. - Supports QA, food safety, and regulatory compliance. | (Calibrated Instruments / Instruments Due for Calibration)  x 100 |

Procedure

| S. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Define KPI Categories and Metrics**<br>• Develop and approve KPI list aligned with global best practices and plant priorities. | Maintenance Director | Annual / As Updated |
| 2 | **Assign Ownership per KPI**<br>• Link each KPI to a primary and supporting role using the KPI Responsibility Matrix. | Maintenance Director | Annual / As Updated |
| 3 | **Configure SAP PM to Enable KPI Tracking**<br>• Ensure required fields (e.g., failure codes, work order types) are standardized and mapped. | SAP PM Administrator | Quarterly |
| 4 | **Maintain Master Data Accuracy**<br>• Ensure asset hierarchy, work centers, and task lists are kept current to support reliable KPI extraction. | SAP PM Administrator / Planner | Ongoing |
| 5 | **Ensure Field-Level Data Entry Discipline**<br>• Train technicians and supervisors to enter complete, timely, and structured feedback. | Maintenance Supervisor | Ongoing |
| 6 | **Review Data Integrity of KPI Inputs**<br>• Check accuracy of core SAP entries that feed into KPI formulas (e.g., downtime, completion codes). | SAP PM Administrator | Weekly / Monthly |
| 7 | **Update KPI Definitions as Needed**<br>• Refine formulas, targets, and tracking methodology based on changes in plant strategy or systems. | Maintenance Manager | Annual / As Needed |

Roles and Responsibilities – Maintenance KPIs

| Role | Responsibilities |
| --- | --- |
| Technician | - Enter complete and accurate work order feedback in SAP (e.g., time, cause, action, parts). |
| Maintenance Supervisor | • - Ensure SAP feedback is validated before closure.<br>• - Reinforce field-level compliance (LOTO, THA, completion codes). |
| Planner | • - Maintain updated task lists and master data relevant to KPIs.<br>• - Support validation of data feeding KPI metrics. |
| SAP PM Administrator | • - Ensure SAP PM system supports data structure required for all defined KPIs.<br>• - Configure downtime codes, feedback forms, etc. |
| Maintenance Manager | • - Define KPI formulas and classifications.<br>• - Suggest additions or revisions to the KPI framework based on reliability focus. |
| Maintenance Director | • - Approve KPI structure and assignments.<br>• - Ensure ownership and integration with strategic goals. |