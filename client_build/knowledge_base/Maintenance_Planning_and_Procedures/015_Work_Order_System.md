---
Department: Maintenance Planning and Procedures
Section: Work Order System
Section_Kind: core
Section_Priority: normal
Source: Maintenance Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Work Order System

Introduction and Background of the Section
The work order system is the foundation of maintenance execution control at Arabian Mills. It enables structured planning, resource allocation, safety compliance, documentation, and post-job performance analysis. All maintenance activities—whether planned, corrective, emergency, or improvement-based—must be captured in the SAP Plant Maintenance (PM) work order system to ensure operational visibility, cost control, and continuous improvement.
A robust work order system supports strategic maintenance goals by enabling:
 Planned vs. reactive maintenance analysis
 Resource and cost accountability
 Regulatory and safety compliance
 Historical data capture for root cause analysis and reliability improvement
Procedure for Work Order

| S. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Work Request Generation**<br>• Notification is raised by technician, operator, or supervisor for any maintenance need. | Technician / Operator / Supervisor | As Needed |
| 2 | **Work Order Creation in SAP**<br>• Planner reviews notification and creates work order with scope, priority, and safety needs. | Maintenance Planner | As needed |
| 3 | **Job Planning and Scheduling**<br>• Planner schedules work order, assigns resources, checks material availability, and ensures permits. | Maintenance Planner | Weekly / Rolling |
| 4 | **Execution of Task**<br>• Technician performs task as per scope and safety requirements. THA, permits, and checklist must be in use. | Technician | As per Schedule |
| 5 | **Feedback and Confirmation**<br>• Technician enters technical feedback, time spent, and materials used. | Technician | After Execution |
| 6 | **Review and Closure**<br>• Supervisor verifies work completion, evaluates feedback, and closes work order in SAP. | Maintenance Supervisor | Daily |
| 7 | **Backlog and Exception Monitoring**<br>• Planner tracks open, overdue, and rejected work orders and reports weekly to Maintenance Manager. | Planner | Weekly |
| 8 | **Data Analysis and Improvement**<br>• Engineers and managers review work order history, breakdown causes, and trends for continuous improvement. | Maintenance Manager | Monthly / Quarterly |


**[Diagram — PNG]:**

**Process Name:** Work Order System

**Roles / Swimlanes:**
- Technician
- Maintenance

### Steps

| Step # | Role        | Action                                                                                             | Decision/Next Step                          |
|--------|-------------|----------------------------------------------------------------------------------------------------|---------------------------------------------|
| Start  | Technician  | Start                                                                                              | No decision; proceed to Step 1              |
| 1      | Technician  | Notification is raised for any maintenance need. (A)                                              | No decision; proceed to Step 2              |
| 2      | Maintenance | Reviews notification and creates work order. (M)                                                  | No decision; proceed to Step 3              |
| 3      | Maintenance | Schedules work order, assigns resources, checks material availability, and ensures permits. (M)   | No decision; proceed to Step 4              |
| 4      | Technician  | Performs task as per scope and safety requirements. (M)                                           | No decision; proceed to Step 5              |
| 5      | Technician  | Enters technical feedback, time spent, and materials used. (A)                                    | No decision; proceed to Step 6              |
| 6      | Maintenance | Verifies work completion, evaluates feedback, and closes work order in SAP. (A/M)                | No decision; proceed to Step 7              |
| 7      | Maintenance | Tracks open, overdue, and rejected work orders and reports weekly. (A)                            | No decision; proceed to Step 8              |
| 8      | Maintenance | Engineers and managers review work order history, breakdown causes, and trends. (M)               | No decision; proceed to End                 |
| End    | Maintenance | End                                                                                               | Process ends                                |

### Mermaid.js Flow

```mermaid
graph TD

  subgraph Technician
    S([Start])
    S1[1. Notification is raised for any maintenance need. (A)]
    S4[4. Performs task as per scope and safety requirements. (M)]
    S5[5. Enters technical feedback, time spent, and materials used. (A)]
  end

  subgraph Maintenance
    M2[2. Reviews notification and creates work order. (M)]
    M3[3. Schedules work order, assigns resources, checks material availability, and ensures permits. (M)]
    M6[6. Verifies work completion, evaluates feedback, and closes work order in SAP. (A/M)]
    M7[7. Tracks open, overdue, and rejected work orders and reports weekly. (A)]
    M8[8. Engineers and managers review work order history, breakdown causes, and trends. (M)]
    E([End])
  end

  S --> S1
  S1 --> M2
  M2 --> M3
  M3 --> S4
  S4 --> S5
  S5 --> M6
  M6 --> M7
  M7 --> M8
  M8 --> E
```

Roles and Responsibilities – Work Order System

| Role | Responsibilities |
| --- | --- |
| Technician | • - Create maintenance notifications in SAP for faults or breakdowns.<br>• - Execute work orders using checklists and comply with THA and permit requirements.<br>• - Enter work confirmations: time, parts used, and technical feedback. |
| Operator | - Raise maintenance notifications in SAP for abnormalities observed during operations. |
| Maintenance Supervisor | • - Review completed work and validate technician entries.<br>• - Ensure safety documents (THA, permits) are attached.<br>• - Approve and close work orders in SAP. |
| Maintenance Planner | • - Review notifications and create structured work orders with safety, material, and manpower requirements.<br>• - Schedule and assign work orders.<br>• - Track backlogs and generate weekly compliance reports. |
| Maintenance Manager | • - Analyze work order trends for root causes and reliability issues.<br>• - Recommend preventive actions and support continuous improvement initiatives. |
| Maintenance Director | • - Ensure policy compliance for work order system.<br>• - Monitor SAP KPIs: backlog, completion rate, repeat failures.<br>• - Lead improvement efforts in planning and execution processes. |
| SAP PM Administrator | • - Maintain SAP PM master data (equipment, task lists, locations).<br>• - Assign and manage SAP user roles.<br>• - Ensure workflow, integration, and reporting functions properly. |