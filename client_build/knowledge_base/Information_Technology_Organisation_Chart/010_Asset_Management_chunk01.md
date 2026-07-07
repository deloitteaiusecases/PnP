---
Department: Information Technology Organisation Chart
Section: Asset Management
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Asset Management
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 7
---

## Asset Management

#### Purpose
The purpose of the Asset Management Policy is to ensure the proper tracking, maintenance, and disposal of IT assets within Arabian Mills. This policy aims to enhance security, improve operational efficiency, and ensure compliance with regulatory standards.
#### Scope
This policy applies to all IT assets managed by Arabian Mills, including hardware, software, and network devices. It covers asset inventory, asset movement, and asset disposal procedures.
#### Objectives
 Security: Protect IT assets from unauthorized access, theft, and damage.
 Compliance: Ensure adherence to legal and regulatory requirements.
 Efficiency: Improve the accuracy and efficiency of asset tracking and management.
 Accountability: Establish clear responsibilities for asset management.
#### Responsibility
The IT & Cybersecurity Manager is responsible for the implementation and adherence to this policy. All IT staff are expected to comply with the procedures outlined in this section.
Asset Inventory Procedure:
The Asset Inventory Procedure outlines the steps required to maintain an accurate and up-to-date inventory of all IT assets within Arabian Mills. This includes listing all devices, applications, and licensed software managed by the IT department. The procedure ensures that all assets are properly tracked, maintained, and updated regularly to enhance security, operational efficiency, and compliance with regulatory standards.

| No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Inventory Listing: List all devices under the custody of the IT department, including desktops, monitors, IP telephones, mobiles, tablets, routers, switches, firewalls, servers, printers, network devices, access devices, CCTV, etc. | Preparer: IT Network and Server Administrator | Ongoing |
| 2 | Software Inventory: List all applications and licensed software installed on production servers and desktops/laptops. | Preparer: IT Network and Server Administrator | Annually |
| 3 | New Asset Requests: Fill the server & network device request form for all new server and network device requests. | Preparer: IT Network and Server Administrator | As Needed |
| 4 | Asset Request Approval: Review and approve the server and network device request form for all new server and network devices requests. | Preparer: IT Network and Server Administrator | As Needed |
| 5 | Asset Inventory Update: Update asset inventory file for any asset removed, disposed, or newly purchased. | Preparer: IT Network and Server Administrator | Within 5 Working Days |
| 6 | Software License Update: Update information about licensed software installed on servers, desktops, and laptops. | Preparer: IT Network and Server Administrator ; Reviewer: IT & Cybersecurity Manager | Annually |
| 7 | Asset Information Capture: Capture asset information using a specified format including asset name, custodian, owner, description, and location. | Preparer: IT Network and Server Administrator | Ongoing |
| 8 | Licensed Software Information Capture: Capture licensed software information using a specified format including software name, license status, IP address/host name, and asset identification. | Preparer: IT Network and Server Administrator | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Asset Inventory Procedure  

**Roles / Swimlanes:**

- IT Network and Server Administrator  
- IT & Cyber Security Manager  

---

### Steps

| Step # | Role | Action (verbatim where legible; `[illegible]` = text not readable) | Decision / Next Step |
|--------|------|---------------------------------------------------------------------|----------------------|
| Start | IT Network and Server Administrator | Start | Proceed to Step 1 |
| 1 | IT Network and Server Administrator | 1. List all devices under the custody of the IT department staff (A/M) | Proceed to Step 2 |
| 2 | IT Network and Server Administrator | 2. List all applications and source code software installed on all [illegible] systems (A/M) | Proceed to Step 3 |
| 3 | IT Network and Server Administrator | 3. Capture asset identification using predefined [illegible] including asset description, owner, and location [illegible]. (A/M) | Proceed to Step 4 |
| 4 | IT Network and Server Administrator | 4. Capture licensed software information using a specific template including software name, license, no. of authorized users, and asset identification. (A/M) | Proceed to Step 5 |
| 5 | IT & Cyber Security Manager | 5. If the server & network devices generate new [illegible] for all new connected hardware devices reported. (M) | Proceed to Decision “Approved?” |
| Decision: Approved? | IT & Cyber Security Manager | Approved? | Yes → Step 6; No → return to Step 5 |
| 6 | IT & Cyber Security Manager | 6. Update asset inventory list for any new asset removed, disposed of, moved, or purchased. (M) | Proceed to End |
| End | IT Network and Server Administrator | End | — |

---

```mermaid
graph TD

    S([Start])
    S1[1. List all devices under the custody of the IT department staff (A/M)]
    S2[2. List all applications and source code software installed on all [illegible] systems (A/M)]
    S3[3. Capture asset identification using predefined [illegible] including asset description, owner, and location [illegible]. (A/M)]
    S4[4. Capture licensed software information using a specific template including software name, license, no. of authorized users, and asset identification. (A/M)]
    S5[5. If the server & network devices generate new [illegible] for all new connected hardware devices reported. (M)]
    D{Approved?}
    S6[6. Update asset inventory list for any new asset removed, disposed of, moved, or purchased. (M)]
    E([End])

    S --> S1 --> S2 --> S3 --> S4 --> S5 --> D
    D -- "Yes" --> S6 --> E
    D -- "No" --> S5
```

#### Asset Movement Procedure
The Asset Movement Procedure defines the process for managing the movement of IT assets between different locations or vendors. This includes filling out and approving asset movement request forms, updating the asset movement register, and verifying the movement and return of assets. The procedure aims to ensure that all asset movements are properly documented and authorized to prevent unauthorized access, loss, or damage.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Asset Movement Request: Fill the Asset Movement Request Form for moving assets between locations or vendors. | Preparer: User/System Administrator | As Needed |
| 2 | Asset Movement Approval: Review and approve the Asset Movement Form. | Reviewer: IT & Cybersecurity Manager | As Needed |
| 3 | Asset Movement Register Update: Update the Asset Movement Register after approval. | Preparer: System Administrator | As Needed |
| 4 | Verification of Asset Movement: Verify outgoing/incoming media/asset as per the Asset Movement Request Form, including checking for approval signature and verifying with signatory if required. | Reviewer: On-duty Security Guard at Gate | As Needed |
| 5 | Media/Asset Return Verification: Verify the return of media/asset as per the return date specified in the Asset Movement Request Form. | Reviewer: System Administrator | As Needed |
| 6 | Asset Invoice Check: Check and verify Asset Invoice for any new device, system, or media brought inside the IT premises or Datacentre . | Reviewer: System Administrator | As Needed |
| 7 | Asset Inventory Maintenance: Update and maintain Asset Inventory for any new or discarded device, system, or media. | Preparer: System Administrator | Ongoing |
| 8 | Form Maintenance: Maintain forms for 2 years. | Preparer: System Administrator | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Asset Movement Procedure  

**Roles / Swimlanes:**
1. Business User  
2. System Administrator or IT & Cybersecurity Manager  
3. Security Guard  

---

### Steps

| Step # | Role | Action | Decision / Next Step |
|--------|------|--------|----------------------|
| Start | Business User | Start | Proceed to Step 1. |
| 1 | Business User | File the Asset Movement Request Form for moving assets between working units. (M) | Send form to “System Administrator or IT & Cybersecurity Manager” → Step 2. |
| 2 | System Administrator or IT & Cybersecurity Manager | File the Asset Movement Request Form for moving assets between sections/locations within MIS. (M) | Go to approval decision → “Approved?” |
| D1 | System Administrator or IT & Cybersecurity Manager | **Decision:** Approved? | **Yes:** proceed to Step 3 and Step 4 (parallel flows). **No:** return to Step 1 / Step 2 for re-filing (arrow back to both Step 1 and Step 2). |
| 3 | Business User | Update the Asset Movement Register after approval. (M) | After updating, send to “System Administrator or IT & Cybersecurity Manager” → Step 6. Also receive later feedback from Step 5 (return verification). |
| 4 | Security Guard | Verify equipment per the Asset Movement Request Form. (M) | After verification, pass information/confirmation upward to Business User → Step 3 (arrow from Step 4 to Step 3). |
| 5 | Business User | Verify the return of movable assets or the workstations specified in the Asset Movement Request Form. (M) | After return verification, update via Step 3 again (arrow from Step 5 back to Step 3). |
| 6 | System Administrator or IT & Cybersecurity Manager | Check and verify Asset Movement Request Form, including transfer details (e.g., number of items, destination, and method of movement). (M) | If verification complete, proceed to Step 7. |
| 7 | System Administrator or IT & Cybersecurity Manager | Update and revise an Asset Inventory Register for any new or discarded devices, system, or media. (M) | Send information to Business User for retention and to confirm closure; arrow to Step 5 (return verification) and toward Step 8 for record keeping. |
| 8 | Business User | Maintain form for 2 years. (M) | End. |
| End | Business User | End | — |

**Yes/No Branch Tracing**

- From Decision D1 “Approved?”  
  - **Yes:**  
    - Flow goes upwards to Business User → Step 3 “Update the Asset Movement Register after approval. (M)”  
    - Flow also goes downwards to Security Guard → Step 4 “Verify equipment per the Asset Movement Request Form. (M)”  
  - **No:**  
    - Flow returns back (arrows) to:  
      - Step 1 (Business User: initial filing for moving between working units).  
      - Step 2 (System Administrator or IT & Cybersecurity Manager: filing for movements within MIS).  

---

### Mermaid.js Diagram

```mermaid
graph TD

    %% Roles (comments for clarity)
    %% BU = Business User
    %% SA = System Administrator or IT & Cybersecurity Manager
    %% SG = Security Guard

    A[Start\n(Business User)] --> S1

    S1[1. File the Asset Movement Request Form for moving assets between working units. (M)\nRole: Business User] --> S2

    S2[2. File the Asset Movement Request Form for moving assets between sections/locations within MIS. (M)\nRole: System Administrator or IT & Cybersecurity Manager] --> D1

    D1{Approved?\nRole: System Administrator or IT & Cybersecurity Manager}

    D1 -- Yes --> S3
    D1 -- Yes --> S4
    D1 -- No --> S1
    D1 -- No --> S2

    S3[3. Update the Asset Movement Register after approval. (M)\nRole: Business User] --> S6

    S4[4. Verify equipment per the Asset Movement Request Form. (M)\nRole: Security Guard] --> S3

    S6[6. Check and verify Asset Movement Request Form, including transfer details. (M)\nRole: System Administrator or IT & Cybersecurity Manager] --> S7

    S7[7. Update and revise an Asset Inventory Register for any new or discarded devices, system, or media. (M)\nRole: System Administrator or IT & Cybersecurity Manager] --> S5

    S5[5. Verify the return of movable assets or the workstations specified in the Asset Movement Request Form. (M)\nRole: Business User] --> S3

    S3 --> S8

    S8[8. Maintain form for 2 years. (M)\nRole: Business User] --> E[End]
```

#### Asset Disposal Procedure
The Asset Disposal procedure is designed to ensure the secure and environmentally responsible disposal of IT assets within Arabian Mills. This process aims to prevent unauthorized access to sensitive data and comply with legal and regulatory requirements.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Asset Evaluation: Identify IT assets that are obsolete, damaged, or no longer required. | Preparer: IT Network and S erver Administrato r | As Needed |
| 2 | Disposal Approval: Obtain approval for asset disposal from the IT & Cybersecurity Manager , ensuring compliance with company policies and regulatory standards. | Reviewer: IT & Cybersecurity Manager | As Needed |
| 3 | Data Erasure: Securely erase all data from IT assets using approved data sanitization tools and methods. | Preparer: IT Network and Server Administrato r | As Needed |
| 4 | Disposal Method Selection: Determine the appropriate disposal method, such as recycling, donation, or physical destruction, based on the asset type and condition. | Preparer: IT Network and Server Administrato r | As Needed |
| 5 | Vendor Coordination: Coordinate with approved disposal vendors for secure pickup and disposal of IT assets. Ensure vendors comply with environmental and data protection standards. | Preparer: IT Network and Server Administrato r | As Needed |
| 6 | Documentation: Maintain records of disposed assets, including asset details, disposal method, vendor information, and approval documentation. | Preparer: IT Network and Server Administrato r | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Asset Disposal Procedure  

**Roles / Swimlanes:**
- IT Network and Server Administrator  
- IT & Cybersecurity Manager  

### Steps

| Step # | Role | Action | Decision/Next Step |
|--------|------|--------|--------------------|
| Start | IT Network and Server Administrator | Start | Proceed to Step 1. |
| 1 | IT Network and Server Administrator | Identify IT assets that are obsolete, damaged, or no longer in use. (M) | Proceed to Step 2 (Approval decision). |
| 2 | IT & Cybersecurity Manager | Approved? | **Yes:** Proceed to Step 3.  **No:** Return to Step 1 for re‑assessment or correction. |
| 3 | IT Network and Server Administrator | 2. Securely erase all data from IT assets using approved data destruction methods. (M) | Proceed to Step 4. |
| 4 | IT Network and Server Administrator | 4. Determine the appropriate disposal method (e.g., recycling, donation, or physical destruction) based on the asset type and condition. (M) | Proceed to Step 5. |
| 5 | IT Network and Server Administrator | 5. Coordinate with approved disposal or e‑waste vendors and obtain disposal certificates where necessary, ensuring compliance with data protection standards. (M) | Proceed to Step 6. |
| 6 | IT Network and Server Administrator | 6. Maintain a record of disposed assets, including serial numbers, disposal methods, data erasure information, and approval documentation. (M) | Proceed to End. |
| End | IT Network and Server Administrator | End | — |

### Mermaid.js Diagram

```mermaid
graph TD

    Start([Start])
    S1[1. Identify IT assets that are obsolete, damaged, or no longer in use. (M)]
    D1{Approved?}
    S3[2. Securely erase all data from IT assets using approved data destruction methods. (M)]
    S4[4. Determine the appropriate disposal method (e.g., recycling, donation, or physical destruction) based on the asset type and condition. (M)]
    S5[5. Coordinate with approved disposal or e‑waste vendors and obtain disposal certificates where necessary, ensuring compliance with data protection standards. (M)]
    S6[6. Maintain a record of disposed assets, including serial numbers, disposal methods, data erasure information, and approval documentation. (M)]
    End([End])

    Start --> S1
    S1 --> D1
    D1 -- No --> S1
    D1 -- Yes --> S3
    S3 --> S4
    S4 --> S5
    S5 --> S6
    S6 --> End
```

#### IT Asset Audit Procedure
The IT Asset Audit Procedure is designed to ensure the accuracy and completeness of the IT asset inventory through regular audits. This procedure aims to identify discrepancies, unauthorized changes, and ensure compliance with company policies and regulatory standards.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Audit Planning: Develop an audit plan outlining the scope, objectives, and schedule for periodic audits of IT assets. | Preparer: Internal Audit Department | Annually |
| 2 | Audit Execution: Conduct physical and logical audits of IT assets, comparing the actual state of assets with the inventory records. | Preparer: Internal Audit Department | Quarterly |
| 3 | Discrepancy Identification: Identify any discrepancies between the actual state of assets and inventory records, including unauthorized changes, missing assets, or incorrect information. | Preparer: Internal Audit Department | Quarterly |
| 4 | Discrepancy Resolution: Investigate and resolve identified discrepancies, updating inventory records as necessary. | Preparer: IT Network and S erver Administrato r ; Reviewer: IT & Cybersecurity Manager | Quarterly |
| 5 | Audit Reporting: Prepare and submit audit reports detailing findings, resolutions, and recommendations for improving asset management practices. | Preparer: Internal Audit Department; Reviewer: IT & Cybersecurity Manager | Quarterly |
| 6 | Management Review: Review audit reports with senior management to ensure awareness and support for necessary changes and improvements. | Reviewer: Senior Management | Quarterly |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** IT Asset Audit Procedure  

**Roles / Swimlanes:**

1. Internal Audit  
2. IT Network Engineer and Server Admin  
3. IT & Cybersecurity Manager  
4. Senior Management  

---

### Steps

| Step # | Role                                | Action | Decision/Next Step |
|--------|-------------------------------------|--------|--------------------|
| Start  | Internal Audit                      | Start | Next: Step 1 |
| 1      | Internal Audit                      | Develop an audit plan outlining the objectives, scope, and schedule for periodic audits of IT assets. (M) | Next: Step 2 |
| 2      | Internal Audit                      | Conduct physical and logical audits of IT assets, verifying that all assets are in the inventory records. (M) | Next: Step 3 |
| 3      | Internal Audit                      | Identify any discrepancies between the actual state of assets and recorded records, including unauthorized changes, missing assets, or incorrect information. (M) | Next: Step 4 (IT Network Engineer and Server Admin) |
| 4      | IT Network Engineer and Server Admin | Investigate and resolve identified discrepancies, updating inventory records as necessary. (M) | Next: Step 4 (IT & Cybersecurity Manager) |
| 4      | IT & Cybersecurity Manager          | Investigate and resolve identified discrepancies, updating inventory records as necessary. (M) | Next: Step 5 |
| 5      | Internal Audit                      | Prepare and submit audit report, detailing findings, risks, and recommendations for improving asset management practices. (M) | Next: Step 6 |
| 6      | Senior Management                   | Review audit reports with senior management to ensure awareness and support for necessary changes and improvements. (M) | Next: End |
| End    | Senior Management                   | End | — |

---

### Mermaid.js Flow

```mermaid
graph TD

    S[Start<br/>Role: Internal Audit]

    A1[1. Develop an audit plan outlining the objectives, scope, and schedule for periodic audits of IT assets. (M)<br/>Role: Internal Audit]

    A2[2. Conduct physical and logical audits of IT assets, verifying that all assets are in the inventory records. (M)<br/>Role: Internal Audit]

    A3[3. Identify any discrepancies between the actual state of assets and recorded records, including unauthorized changes, missing assets, or incorrect information. (M)<br/>Role: Internal Audit]

    B4[4. Investigate and resolve identified discrepancies, updating inventory records as necessary. (M)<br/>Role: IT Network Engineer and Server Admin]

    C4[4. Investigate and resolve identified discrepancies, updating inventory records as necessary. (M)<br/>Role: IT & Cybersecurity Manager]

    A5[5. Prepare and submit audit report, detailing findings, risks, and recommendations for improving asset management practices. (M)<br/>Role: Internal Audit]

    D6[6. Review audit reports with senior management to ensure awareness and support for necessary changes and improvements. (M)<br/>Role: Senior Management]

    E[End<br/>Role: Senior Management]

    S --> A1 --> A2 --> A3 --> B4 --> C4 --> A5 --> D6 --> E
```

#### IT Asset Verification Procedure
The IT Asset Verification Procedure is designed to ensure the accuracy and completeness of the IT asset inventory through regular verification processes. This procedure aims to confirm the existence, condition, and location of IT assets, ensuring compliance with company policies and regulatory standards.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Verification Planning: Develop a verification plan outlining the scope, objectives, and schedule for regular verification of IT assets. | Preparer: Finance Department | Annually |
| 2 | Asset Verification: Conduct physical verification of IT assets, confirming their existence, condition, and location as recorded in the inventory. | Preparer: Finance Department | Quarterly |
| 3 | Verification Documentation: Document the results of the verification process, including any discrepancies or issues identified. | Preparer: Finance Department | Quarterly |
| 4 | Discrepancy Resolution: Investigate and resolve any discrepancies identified during the verification process, updating inventory records as necessary. | Preparer: IT Network and Server Admin ; Reviewer: IT & Cybersecurity Manager | Quarterly |
| 5 | Verification Reporting: Prepare and submit verification reports detailing findings, resolutions, and recommendations for improving asset management practices. | Preparer: Finance Department; Reviewer: IT & Cybersecurity Manager | Quarterly |
| 6 | Management Review: Review verification reports with senior management to ensure awareness and support for necessary changes and improvements. | Reviewer: Senior Management | Quarterly |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** IT Asset Verification Procedure  

**Roles / Swimlanes:**

- Finance Department  
- IT Network and Server Admin  
- IT & Cybersecurity Manager  
- Senior Management  

---

### Steps

| Step # | Role | Action | Decision/Next Step |
|--------|------|--------|--------------------|
| Start | Finance Department | Start of the IT Asset Verification Procedure. | Proceed to Step 1. |
| 1. | Finance Department | Develop a verification plan, outlining the objectives, schedule, and the time for regular verification of IT assets. (R) | Proceed to Step 2. |
| 2. | Finance Department | Conduct physical verification of IT assets, confirming their existence, condition, and location as recorded in the inventory. (M) | Proceed to Step 3. |
| 3. | Finance Department | Document the results of the verification process, including any discrepancies or issues identified. (M) | Proceed to Step 4. (IT Network and Server Admin) |
| 4. | IT Network and Server Admin | Investigate and resolve any discrepancies identified during the verification, updating records as necessary. (M) | Proceed to Step 4. (IT & Cybersecurity Manager) |
| 4. | IT & Cybersecurity Manager | Investigate and resolve any discrepancies identified during the verification, updating records as necessary. (M) | Proceed to Step 5. |
| 5. | Finance Department | Prepare and submit verification reports, detailing findings, discrepancies, and recommendations for improving asset management practices. (M) | Proceed to Step 6. |
| 6. | Senior Management | Review verification reports with senior management to ensure awareness and confirm necessary changes and improvements. (M) | Proceed to End. |
| End | Senior Management | End of the IT Asset Verification Procedure. | — |

---

### Mermaid.js Flow

```mermaid
graph TD

    start([Start])

    s1["1. Finance Department: Develop a verification plan, outlining the objectives, schedule, and the time for regular verification of IT assets. (R)"]
    s2["2. Finance Department: Conduct physical verification of IT assets, confirming their existence, condition, and location as recorded in the inventory. (M)"]
    s3["3. Finance Department: Document the results of the verification process, including any discrepancies or issues identified. (M)"]
    s4a["4. IT Network and Server Admin: Investigate and resolve any discrepancies identified during the verification, updating records as necessary. (M)"]
    s4b["4. IT & Cybersecurity Manager: Investigate and resolve any discrepancies identified during the verification, updating records as necessary. (M)"]
    s5["5. Finance Department: Prepare and submit verification reports, detailing findings, discrepancies, and recommendations for improving asset management practices. (M)"]
    s6["6. Senior Management: Review verification reports with senior management to ensure awareness and confirm necessary changes and improvements. (M)"]

    end([End])

    start --> s1 --> s2 --> s3 --> s4a --> s4b --> s5 --> s6 --> end
```

#### Annexure

**[Diagram — Visio-EMF→PNG]:**

Asset Inventory  
Forms.pdf


**[Diagram — Visio-EMF→PNG]:**

The image shows a mostly blank white page with a single PDF file icon located near the bottom center.

- The icon is a standard PDF document symbol with a small red border and a red emblem.
- Directly beneath the icon, the file name is displayed on two lines:

1. `Asset Movement`  
2. `Template-.pdf`