---
Department: Maintenance Planning and Procedures
Section: Maintenance Scheduling
Section_Kind: core
Section_Priority: normal
Source: Maintenance Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Maintenance Scheduling

Introduction and Background of the Section
Maintenance scheduling is the structured process of assigning specific maintenance tasks to specific time periods and responsible personnel, in coordination with production schedules and operational constraints. It ensures timely execution of preventive and corrective maintenance activities, with minimal impact on plant throughput and safety.
At Arabian Mills, the SAP PM module is the central platform for managing the maintenance schedule. It supports automated schedule generation based on pre-set frequencies and allows visibility across departments. Maintenance schedules are prepared weekly and reviewed daily for adjustments based on priority, resource shifts, or emergency interventions.
Policy
 Once approved by the S&OP Core Team, the monthly preventive maintenance schedule shall be considered frozen.
 Any proposed deviation, deferral, or acceleration of scheduled PM tasks must be reviewed and approved through the formal change control process outlined below.
 All changes must be documented in SAP, including the justification, approver, and impact (e.g., on operations, reliability, or safety).
 Only the S&OP Core Team is authorized to approve changes to the PM plan.
Procedure for Maintenance Scheduling

| S. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Initiate Monthly Scheduling Cycle**<br>• Trigger scheduling process based on active PM plans and pending CM notifications in SAP. | SAP PM Administrator | Monthly |
| 2 | **Review Open Work Orders and Notifications**<br>• Extract list of open PM and CM work orders from SAP and validate for scope, parts, and permits. | Maintenance Planner | Monthly |
| 3 | **Determine Task Priority and Workload**<br>• Classify work orders by priority (P1–P5), duration, and resource requirement. | Maintenance Planner | Monthly |
| 4 | **Coordinate with Production Team**<br>• Confirm equipment availability windows and integrate with production schedule. | Maintenance Planner | Monthly |
| 5 | **Develop Monthly Maintenance Plan**<br>• Create a comprehensive monthly schedule in SAP, with work orders distributed by week and resource allocation. | Maintenance Planner | Monthly |
| 6 | **Refine into Weekly and Daily Schedules**<br>• Break down the monthly plan into weekly and daily task lists. Assign tasks to teams via SAP and briefings. | Maintenance Supervisor | Weekly / Daily |
| 7 | **Adjust for Unplanned Work**<br>• Reschedule deferred work and insert urgent/emergency jobs into the active plan using SAP. | Maintenance Planner | As Needed |
| 8 | **Communicate Plan to All Stakeholders**<br>• Share finalized monthly schedule with maintenance, production, and stores teams via SAP reports and meetings. | Maintenance Supervisor | Monthly / Weekly |
| 9 | **Monitor Execution and Compliance**<br>• Track completion status in SAP and record delays, early completions, or task deferrals. | SAP PM Administrator | Daily / Weekly |
| 10 | **Evaluate Planning Effectiveness**<br>• Review KPIs (schedule compliance %, reactive maintenance %, deferred jobs, etc.) and initiate improvement actions. | Maintenance Manager | Monthly |

Changes to Approved Monthly Preventive Maintenance Plans
In high-performing maintenance organizations, stability in the monthly preventive maintenance (PM) plan is a core principle. Changes to an approved plan should be exceptional, disciplined, and transparent, as they impact production schedules, resource allocation, and plant reliability. Arabian Mills recognizes that any change to an approved PM plan must follow a structured governance process involving joint ownership by Maintenance, Production, and Planning functions.
Roles and Responsibilities – Maintenance Scheduling

| Role | Responsibilities |
| --- | --- |
| SAP PM Administrator | Initiates scheduling cycle in SAP, supports system configuration, and generates compliance reports |
| Maintenance Planner | Reviews open work orders, assigns priorities, coordinates with production, and prepares weekly/daily schedules |
| Maintenance Supervisor | Communicates task assignments, ensures resource readiness, and handles daily scheduling at team level |
| Production Coordinator | Confirms equipment availability and collaborates with planner to minimize production disruption |
| Stores Team | Ensures spare parts and tools are issued on time as per scheduled tasks |
| Maintenance Manager | Reviews scheduling performance, approves high-impact deviations, and drives improvements in planning discipline |


**[Diagram — PNG]:**

**Process Name:** Maintenance Scheduling  

**Roles / Swimlanes:**
- SAP PM Administrator
- Maintenance  

---

### Steps

| Step # | Role                | Action | Decision / Next Step |
|--------|---------------------|--------|-----------------------|
| Start  | SAP PM Administrator | Start | Proceed to step 1. |
| 1      | SAP PM Administrator | Trigger scheduling process (M) | Proceed to step 2. |
| 2      | Maintenance          | Extract list of open PM and CM work orders from SAP and validate for scope, parts, and permits. (A) | Proceed to step 3. |
| 3      | Maintenance          | Classify work orders by priority (P1–P5), duration, and resource requirement. (M) | Proceed to step 4. |
| 4      | Maintenance          | Confirm equipment availability windows and integrate with production schedule. (M) | Proceed to step 5. |
| 5      | Maintenance          | Create a comprehensive monthly schedule in SAP, with work orders. (M) | Proceed to step 6. |
| 6      | Maintenance          | Break down the monthly plan into weekly and daily task lists. (A/M) | Proceed to step 7. |
| 7      | Maintenance          | Reschedule deferred work and insert urgent/emergency jobs. (M) | Proceed to step 8. |
| 8      | Maintenance          | Share finalized monthly schedule with maintenance, production, and stores teams. (A/M) | Proceed to step 9. |
| 9      | Maintenance          | Track completion status in SAP and record delays, early completions, or task deferrals. (M) | Proceed to step 10. |
| 10     | Maintenance          | Review KPIs and initiate improvement actions. (M) | Proceed to End. |
| End    | Maintenance          | End | Process completed. |

*(There are no explicit Yes/No decision branches in this flow; all transitions are linear as described.)*

---

```mermaid
graph TD

    Start([Start])
    S1[1. Trigger scheduling process (M)]
    S2[2. Extract list of open PM and CM work orders from SAP and validate for scope, parts, and permits. (A)]
    S3[3. Classify work orders by priority (P1–P5), duration, and resource requirement. (M)]
    S4[4. Confirm equipment availability windows and integrate with production schedule. (M)]
    S5[5. Create a comprehensive monthly schedule in SAP, with work orders. (M)]
    S6[6. Break down the monthly plan into weekly and daily task lists. (A/M)]
    S7[7. Reschedule deferred work and insert urgent/emergency jobs. (M)]
    S8[8. Share finalized monthly schedule with maintenance, production, and stores teams. (A/M)]
    S9[9. Track completion status in SAP and record delays, early completions, or task deferrals. (M)]
    S10[10. Review KPIs and initiate improvement actions. (M)]
    End([End])

    Start --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> End
```