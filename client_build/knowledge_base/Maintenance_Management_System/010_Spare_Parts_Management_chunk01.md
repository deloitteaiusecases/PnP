---
Department: Maintenance Management System
Section: Spare Parts Management
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Spare Parts Management
Source: Maintenance Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 0
---

## Spare Parts Management

Introduction and Background of the Section
Spare parts management is vital to ensure equipment reliability and timely maintenance execution. At Arabian Mills, the spare parts system is designed to support both preventive and corrective maintenance with readily available, correctly specified, and cost-effective parts. The system is governed by best practices in inventory control and is fully integrated with the SAP MM and PM modules.
Spare parts are categorized based on criticality, usage frequency, and lead time. Reorder points, minimum and maximum stock levels, and inventory movement histories are tracked digitally. The Stores and Maintenance teams collaborate to ensure high availability of critical components while minimizing excess inventory and procurement delays.
Policy
 All spare parts must be classified and maintained in the SAP MM module with clearly defined specifications, reorder levels, and criticality tags.
 Spare parts shall be categorized as critical, fast-moving, or slow-moving based on usage frequency, lead time, and impact on production downtime:
  o Critical spares: Required to avoid significant production loss or safety risk; high availability must be ensured.
  o Slow-moving spares: Used infrequently; reviewed periodically to optimize stock levels and avoid overstocking or obsolescence.
 Only SAP-authorized requisitions and issues are allowed for all maintenance work orders.
 Any emergency purchases must be justified by a breakdown notification or safety risk, approved by the Maintenance Director, and processed through an expedited SAP PO flow.
 Periodic reconciliation, consumption tracking, and obsolete stock reviews must be conducted, and Material Requirements Planning (MRP) shall be run through SAP to propose purchase actions based on stock policies.
 Adjustments to stock levels or planning parameters must be approved by the Maintenance Director based on documented justification.
 Vendors for external spares or services shall be prequalified and linked in the SAP supplier database.
Spare Parts Management Procedure

| S. No. | Procedure Description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Critical Spares Identification**<br>• Tag parts with safety, regulatory, or high downtime impact as “critical” in SAP. | **Maintenance Manager +**<br>• Spare Parts Controller +<br>• Maintenance Coordinator | Annual / As Needed |
| 2 | **Slow-Moving Parts Classification**<br>• Review movement history and classify parts with minimal annual usage as slow-moving. | Stores Team | Quarterly |
| 3 | **Set Inventory Levels**<br>• Define and enter min/max stock and reorder points for all stocked parts in SAP. | Stores Team | Annual / As Needed |
| 4 | **Stock Level Authorization**<br>• Review and approve any proposed changes to reorder levels or MRP parameters. | Maintenance Director | As Needed |
| 5 | **Run MRP in SAP**<br>• Run Material Requirements Planning (MRP) in SAP to trigger proposals for purchase requisitions based on stock policy. | SAP PM/MM Administrator | Weekly |
| 6 | **Spare Parts Requisition**<br>• Raise material reservations or PRs through SAP against a work order. | Technician | As Required |
| 7 | **Requisition Approval**<br>• Review and approve spare part requisitions for processing. | Supervisor | As Required |
| 8 | **Purchase Order Processing**<br>• Convert approved PRs into POs in SAP and issue to vendor. | Procurement Department | As Required |
| 9 | **Emergency Purchase Approval**<br>• Authorize emergency spares procurement due to breakdown or safety-critical needs. | Maintenance Director | As Required |
| 10 | **Goods Receipt and Stocking**<br>• Receive delivered parts, verify quantity/quality, and record goods receipt in SAP. | Stores Team | Per Delivery |
| 11 | **Issuance to Work Order**<br>• Issue spare parts through SAP against the relevant maintenance work order. | Stores Team | Daily |
| 12 | **Parts Consumption Logging**<br>• Log part usage details in the SAP work order and return unused materials. | Technician | Per Task |
| 13 | **Stock Reconciliation**<br>• Reconcile physical and SAP stock, investigate variances, and adjust where necessary. | Stores Team | Monthly |
| 14 | **Obsolescence and Movement Review**<br>• Generate SAP reports to flag non-moving, excess, or obsolete inventory. | SAP PM/MM Administrator | Quarterly |
| 15 | **Action on Obsolete or Excess Stock**<br>• Evaluate SAP reports and recommend corrective actions (write-off, reallocation, etc.). | Maintenance Manager | Quarterly |

Roles and Responsibilities

| Role | Responsibilities |
| --- | --- |
| Maintenance Manager | **- Identify and tag critical spare parts in SAP**<br>• - Provide justification for new parts or changes in classification |
| Stores Team | **- Classify slow-moving items**<br>• - Maintain and update stock levels (min/max/reorder)<br>• - Perform goods receipt- Issue and return parts against work orders<br>• - Conduct monthly stock reconciliation |
| Maintenance Director | **- Approve emergency purchases**<br>• - Authorize changes to inventory parameters<br>• - Decide actions on obsolete/excess inventory |
| SAP PM/MM Administrator | **- Run MRP in SAP**<br>• - Generate reports on non-moving/excess stock<br>• - Support technical configuration of spares management |
| Technician | **- Raise spare part requisitions linked to work orders**<br>• - Log usage and return unused items in SAP |
| Supervisor | **- Approve material requisitions from technicians**<br>• - Ensure correct spare usage and documentation |
| Procurement Department | **- Process approved PRs into POs in SAP**<br>• - Coordinate with vendors for timely deliveries |

Spare Parts Categorization
In a wheat milling and animal feeds plant, spare parts can be effectively categorized using a triangular approach based on:
1. Criticality – impact of part failure on safety, production, and compliance
2. Usage Frequency – how often the part is consumed or replaced
3. Lead Time – time required to procure the part (especially from OEMs abroad)
1. Categorization by Criticality

| Category | Criteria | Examples (Wheat Mill / Feed Plant) |
| --- | --- | --- |
| Critical | **- Causes full line stoppage or safety hazard**<br>• - No redundancy | Main drive motors (roller mills, pellet press), PLC modules, gearboxes |
| Semi-Critical | **- Causes quality issues or partial downtime**<br>• - Workaround possible | Plansifter sieve frames, feeder belts, VFD units |
| Non-Critical | - No significant impact on production or safety | Panel indicators, control switch covers, inspection windows |

2. Categorization by Usage Frequency

| Category | Criteria | Examples |
| --- | --- | --- |
| Fast-Moving | **Frequently consumed parts**<br>• Used weekly or monthly | Bearings (bucket elevators, roller mills), V-belts, pneumatic fittings |
| Slow-Moving | **Used infrequently**<br>• Every 6–12 months | Shaft couplings, die clamps (pellet press), spare pulleys |
| Non-Moving | **Rarely or never used**<br>• No consumption in past year | Obsolete HMI panels, discontinued sensor models |

3. Categorization by Lead Time

| Category | Criteria | Examples |
| --- | --- | --- |
| Short Lead Time | Locally available, standard stock | Grease nipples, fasteners, seals, pneumatic tubing |
| Medium Lead Time | Regionally sourced or off-the-shelf OEM parts | Control relays, timing belts, vibration sensors |
| Long Lead Time | Imported/customized/OEM-exclusive parts | Cylinder shells, die rings (pellet press), imported PLC I/O modules |

Combined Examples Table

| Spare Part | Equipment | Criticality | Usage Frequency | Lead Time | Comments |
| --- | --- | --- | --- | --- | --- |
| Main Gearbox | Roller Mill | Critical | Slow-Moving | Long | Keep 1 in stock; lead time > 6 weeks |
| Nylon Sieve Frames | Plansifter | Semi-Critical | Medium | Order quarterly based on wear rate |  |
| V-Belts | Pellet Mill / Elevators | Semi-Critical | Fast-Moving | Short | Maintain buffer stock; used across multiple machines |
| Pressure Transmitter | Pneumatic Lines | Semi-Critical | Medium | Keep minimum 2 in stock; vendor lead time ~2 weeks |  |
| Control Panel Indicator Light | Electrical Cabinets | Non-Critical | Slow-Moving | Short | Procure as needed |
| Cylinder Shell | Roller Mill | Critical | Slow-Moving | Long | Imported, expensive; stock 1 based on usage history |