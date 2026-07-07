---
Department: Internal Stock Transfers Between Warehouses/Branches
Section: Internal Stock Transfers Between Warehouses/Branches
Section_Kind: core
Section_Priority: normal
Source: SCM_Logistics Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

# Internal Stock Transfers Between Warehouses/Branches

To establish a standardized, traceable, and SAP-integrated process for all internal stock movements between Arabian Mills warehouses and branches (e.g., Riyadh to Jizan), covering finished goods, raw materials, packaging materials, and spare parts. This process ensures inventory control, product accountability, vehicle compliance, and accurate system reconciliation.
Policies
System-Based Authorization:
 All inter-warehouse transfers must be initiated through a Stock Transfer Order (STO) generated in SAP. No manual dispatch will be allowed.
Approval Protocol:
 The STO must be approved by either the Supply Chain Planning Head or the respective Warehouse Manager before execution.
Approved Transport Use Only:
 Internal transfers will be executed only through company-owned vehicles or approved third-party transporters enlisted by Arabian Mills.
Product-Vehicle Compatibility:
 Vehicle selection must reflect the product’s handling needs — e.g., reefer trucks for temperature-sensitive items, covered trucks for flour and bran.
Loading Compliance:
 All materials must be scanned, weighed, and loaded as per the STO item list. Seal placement is mandatory before dispatch.
FIFO Discipline:
 Unless specifically exempted, FIFO (First-In-First-Out) shall apply for inventory release. LIFO (Last-In-First-Out) is only permissible with Planning Head’s approval and documented justification.
Receiving Verification:
 Receiving Warehouse must verify seal integrity, weight, and quantity prior to SAP posting. All discrepancies must be recorded immediately and escalated.
Documentation Integrity:
 Transfer-related documentation must be complete, stamped, and archived digitally in the SAP document management module.
Timeliness & Escalation:
 Delays, shortages, or seal tampering must be escalated to the Transport Supervisor and Logistics Head within 2 working hours.
Inventory Traceability:
 Each transfer must be traceable by STO number, vehicle ID, transporter name, and receiving confirmation in SAP.
Procedure
This procedure outlines the standardized process followed by Arabian Mills to execute internal stock transfers between warehouses or branches. It ensures product accuracy, transportation compliance, real-time inventory reconciliation in SAP, and strict documentation control. The steps below detail responsibilities from initiation to final receipt posting.

| Step | Responsibility | Procedure Description | Output / Report |
| --- | --- | --- | --- |
| 1 | Warehouse Supervisor | Create a Stock Transfer Order (STO) in SAP and get it approved | Approved STO Printout |
| 2 | Transport Coordinator | Assign vehicle based on product type and volume | Vehicle Assignment Log |
| 3 | Warehouse Staff | Scan and weigh all items listed in the STO | Loading Sheet |
| 4 | QA Officer / Supervisor | Inspect vehicle cleanliness and apply seal after loading | Dispatch Seal Log |
| 5 | Driver / Dispatcher | Dispatch material to the destination branch | Trip Sheet |
| 6 | Receiving Clerk | Verify seal, scan and weigh incoming goods, and post receipt in SAP | Receiving Checklist + SAP GRN |
| 7 | Inventory Supervisor | Investigate and escalate any quantity or seal discrepancy | Discrepancy Report |
| 8 | Document Control Officer | File all transfer documents and upload scanned versions to SAP archive | Digital Archive Folder |

Flow Chart

**[Diagram — PNG]:**

**Process Name: Internal Stock Transfers Between Warehouses/Branches**

**Roles/Swimlanes:**
- Warehouse
- Transport Coordinator
- QA Officer/Supervisor
- Driver/Dispatcher
- Receiving Clerk
- Inventory Supervisor
- Document Control Officer

**Steps:**

| Step # | Role                   | Action                                                                                   | Decision/Next Step                 |
|--------|------------------------|------------------------------------------------------------------------------------------|------------------------------------|
| 1      | Warehouse              | Start                                                                                    |                                    |
| 2      | Warehouse              | Create a Stock Transfer Order (STO) in SAP and get it approved                           |                                    |
| 3      | Transport Coordinator  | Assign vehicle based on product type and volume                                          |                                    |
| 4      | Warehouse              | Scan and weigh all items listed in the STO                                               |                                    |
| 5      | QA Officer/Supervisor  | Inspect vehicle cleanliness and apply seal after loading                                 |                                    |
| 6      | Driver/Dispatcher      | Dispatch material to the destination branch                                              |                                    |
| 7      | Receiving Clerk        | Verify seal, scan and weigh incoming goods, and post receipt in SAP                      |                                    |
| 8      | Inventory Supervisor   | Discrepancy Report                                                                       |                                    |
| 9      | Document Control Officer | Digital Archive Folder                                                                      |                                    |
| 10     | Document Control Officer | End                                                                                       |                                    |

**Mermaid.js Code Block:**

```mermaid
graph TD
    A[Start] --> B[Create a Stock Transfer Order (STO) in SAP and get it approved]
    B --> C[Assign vehicle based on product type and volume]
    B --> D[Scan and weigh all items listed in the STO]
    D --> E[Inspect vehicle cleanliness and apply seal after loading]
    E --> F[Dispatch material to the destination branch]
    F --> G[Verify seal, scan and weigh incoming goods, and post receipt in SAP]
    G --> H[Discrepancy Report]
    H --> I[Digital Archive Folder]
    I --> J[End]
```