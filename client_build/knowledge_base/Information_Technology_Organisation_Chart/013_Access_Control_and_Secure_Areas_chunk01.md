---
Department: Information Technology Organisation Chart
Section: Access Control and Secure Areas
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Access Control and Secure Areas
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 5
---

## Access Control and Secure Areas

#### Purpose
The purpose of this procedure manual is to establish standards for access control and secure areas within Arabian Mills. By defining clear protocols and responsibilities, the organisation aims to ensure that access to information, applications, and secure areas is granted only to authorised users, maintaining the confidentiality, integrity, and availability of its information assets.
#### Scope
This procedure manual applies to all servers, applications, network devices, physical hosts, and secure areas within Arabian Mills. It covers the processes for reviewing access rights and managing access to secure areas, ensuring compliance with security policies and guidelines.
#### Procedure Reference
This procedure manual refers to the Identity & Access Control Management, Information Classification & Media Handling, and Physical and Environmental Security Guidelines of ARABIAN MILLS Information Security, ensuring alignment with overarching security policies and standards.
#### Objectives
The objectives of this procedure manual are to:
 Ensure Proper Access Control: Review access rights regularly to ensure that only authorised users have access to information and applications.
 Manage Access to Secure Areas: Implement procedures for granting and monitoring access to secure areas, ensuring that access is restricted to authorised personnel.
 Support Compliance: Ensure compliance with security policies, standards, and regulatory requirements for access control and secure areas.
#### Responsibility
It is the responsibility of the IT & Cybersecurity Manager to ensure the proper implementation of these procedures. The procedures shall be reviewed and updated as necessary or at least annually by the IT & Cybersecurity Manager.
#### Access Right Review Procedures
1. Access Right Review Procedure - Servers & Applications
To maintain secure access to servers and applications, Arabian Mills conducts regular access right reviews. This procedure ensures that access is limited to authorised users, preventing unauthorised or unnecessary access to critical information systems.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Generate User Access List: Generate list of users having access to servers/applications. System generated list is preferred over manual list. | Preparer: IT Network and Server Admin | Quarterly |
| 2 | Share User Access List: Share the user access list with the concerned owners of the server/application for review. | Preparer: IT Network and Server Admin | Quarterly |
| 3 | Review User Access: Review the user access on the servers/applications and inform the updates/modifications to the server/application administrator. | Preparer: Concerned Owner of Server/Application | Quarterly |
| 4 | Update User Access List: Update the user access list and send the final revised user access list to the concerned owner of server/application for final review and approval. | Preparer: Server/Application Administrator | Quarterly |
| 5 | Approve Updates: Obtain approval from the concerned owner of the server/application for the updates/modifications to the user access list. | Reviewer : Concerned Owner of Server/Application | Quarterly |
| 6 | Repeat Review Process: Repeat the review process every three months for any access change, resigned employees, and elevated privileges. | Preparer: IT Network and Server Admin | Quarterly |
| 7 | Maintain User Access Review List: Maintain and update the user access review list as a digital record and retain the documents for 3 years. | Preparer: IT Network and Server Admin | Ongoing |
| 8 | Shred Documents: Shred any physical documents using a shredder after 3 years. | Preparer: IT Network and Server Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Access Right Review - Server and Application Procedure  

**Roles / Swimlanes:**
- IT Network and Server Admin  
- Application / Server User  

| Step # | Role                          | Action                                                                                                                                                                                                 | Decision/Next Step                                                                                                                                                                                                                                       |
|--------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start  | —                             | Start                                                                                                                                                                                                  | Proceed to Step 1                                                                                                                                                                                                                                        |
| 1      | IT Network and Server Admin   | Generate list of users having access to servers/ applications. (AM)                                                                                                                                   | Proceed to Step 2                                                                                                                                                                                                                                        |
| 2      | IT Network and Server Admin   | Share the user access list with the owner/custodian of the server/application for review. (M)                                                                                                         | Proceed to Step 3                                                                                                                                                                                                                                        |
| 3      | Application / Server User     | Review the user access on the server/application and identify any modification \[unreadable]. Mention the necessary modification on the user \[unreadable] list. (M)                                   | Return the reviewed list to IT Network and Server Admin (proceeds to Step 4).                                                                                                                                                                           |
| 4      | IT Network and Server Admin   | Update the user access list as per the server/application user review and send the same to the \[server/application] owner for final review and approval. (M)                                         | Proceed to Decision D1 (“Approved”).                                                                                                                                                                                                                    |
| D1     | IT Network and Server Admin / Application / Server User | **Decision: Approved**                                                                                                                                                                                 | **Yes:** Proceed to Step 6.  **No:** Backward arrow to the earlier review/update steps on the left (loop between the review by Application / Server User and the update by IT Network and Server Admin — exact target of the “No” arrow is unreadable). |
| 6      | IT Network and Server Admin   | Repeat the review process every 6 months for any users having privileged access, newly created users, and elevated privileges. (M)                                                                     | Proceed to Step 7                                                                                                                                                                                                                                        |
| 7      | Application / Server User     | Maintain and update the user access review list in \[an] electronic format and retain all approval records and review documents for 3 years. (M)                                                      | Proceed to Step 8                                                                                                                                                                                                                                        |
| 8      | IT Network and Server Admin   | Shred any physical documents after 3 years. (M)                                                                                                                                                        | Proceed to End                                                                                                                                                                                                                                          |
| End    | —                             | End                                                                                                                                                                                                    | —                                                                                                                                                                                                                                                        |

```mermaid
graph TD

    Start([Start])

    S1[1. Generate list of users having access to servers/ applications. (AM)]
    S2[2. Share the user access list with the owner/custodian of the server/application for review. (M)]
    S3[3. Review the user access on the server/application and identify any modification [unreadable]. Mention the necessary modification on the user [unreadable] list. (M)]
    S4[4. Update the user access list as per the server/application user review and send the same to the owner for final review and approval. (M)]
    D1{Approved}
    S6[6. Repeat the review process every 6 months for any users having privileged access, newly created users, and elevated privileges. (M)]
    S7[7. Maintain and update the user access review list in electronic format and retain all approval records and review documents for 3 years. (M)]
    S8[8. Shred any physical documents after 3 years. (M)]
    End([End])

    Start --> S1 --> S2 --> S3 --> S4 --> D1

    D1 -->|Yes| S6 --> S7 --> S8 --> End
    D1 -->|No| S3
```

2. Access Right Review Procedure - Network Devices & Physical Hosts
Regular access right reviews for network devices and physical hosts are essential to ensure secure and authorised access. This procedure outlines the steps for reviewing and updating user access to these critical components of the IT infrastructure.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Generate User Access List: Generate list of users having access to network devices and physical hosts. System generated list is preferred over manual list. | Preparer: IT Network and Server Admin | Quarterly |
| 2 | Share User Access List: Share the generated user access list with the IT & Cybersecurity Manager for review. | Preparer: IT Network and Server Admin | Quarterly |
| 3 | Review User Access: Review the user access on the network devices and physical hosts and inform the updates to the system administrator. | Preparer: IT & Cybersecurity Manager | Quarterly |
| 4 | Update User Access List: Update the user access list based on approved modifications and send the final revised list to the IT & Cybersecurity Manager for final review and approval. | Preparer: IT Network and Server Admin | Quarterly |
| 5 | Approve Updates: Obtain approval from the IT & Cybersecurity Manager for the updates/modifications to the user access list. | Reviewer : IT & Cybersecurity Manager | Quarterly |
| 6 | Repeat Review Process: Repeat the review process every three months for any access change, resigned employees, and elevated privileges. | Preparer: IT Network and Server Admin | Quarterly |
| 7 | Maintain User Access Review List: Maintain and update the user access review list as a digital record and retain the documents for 3 years. | Preparer: IT Network and Server Admin | Ongoing |
| 8 | Shred Documents: Shred any physical documents using a shredder after 3 years. | Preparer: IT Network and Server Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Access Right Review - Network Devices and Physical Hosts Procedure  

**Roles / Swimlanes:**
- IT Network and Server Admin  
- IT & Cyber Security Manager  

---

### Steps

| Step # | Role | Action | Decision / Next Step |
|--------|------|--------|----------------------|
| 0 | IT Network and Server Admin | **Start** | Go to Step 1 |
| 1 | IT Network and Server Admin | Generate list of users having access to network devices and physical host. (ANM) | Go to Step 2 |
| 2 | IT Network and Server Admin | Share the user access list with the IT & Cyber Security Manager for review. (ANM) | Go to Step 3 |
| 3 | IT & Cyber Security Manager | Review the user access on network devices and physical host, then communicate updates to the system administrator. (M) | Go to Decision 4 |
| 4 | IT Network and Server Admin | Update the user access list as needed and make system updates. Then share with IT & Cyber Security Manager for final review and approval. (ANM) | Decision “Approved?” – If Yes, go to Step 6; If No, go to Step 5 |
| 5 | IT & Cyber Security Manager | Repeat the review process, ensuring records for every new, moved, temporary, and revoked privileges. (M) | After review, return to Decision 4 (“Approved?”) |
| 6 | IT Network and Server Admin | Maintain and update the user access control list in alignment with retention requirements and retain documents for 7 years. (ANM) | Go to Step 7 |
| 7 | IT Network and Server Admin | Shred any physical documentation as practical after 7 years. (ANM) | Go to Step 8 |
| 8 | IT Network and Server Admin | **End** | — |

**Decision Point:**

- **Decision 4: Approved**
  - **Yes:** proceed to Step 6  
  - **No:** go to Step 5, then loop back to Decision 4 after re‑review  

---

```mermaid
graph TD

    %% Roles (lanes noted in comments)
    A0([Start]):::admin
    A1[1. Generate list of users having access to network devices and physical host. (ANM)]:::admin
    A2[2. Share the user access list with the IT & Cyber Security Manager for review. (ANM)]:::admin
    M3[3. Review the user access on network devices and physical host, then communicate updates to the system administrator. (M)]:::manager
    A4[4. Update the user access list as needed and make system updates. Then share with IT & Cyber Security Manager for final review and approval. (ANM)]:::admin
    D4{Approved}:::admin
    M5[5. Repeat the review process, ensuring records for every new, moved, temporary, and revoked privileges. (M)]:::manager
    A6[6. Maintain and update the user access control list in alignment with retention requirements and retain documents for 7 years. (ANM)]:::admin
    A7[7. Shred any physical documentation as practical after 7 years. (ANM)]:::admin
    A8([End]):::admin

    A0 --> A1 --> A2 --> M3 --> A4 --> D4
    D4 -- Yes --> A6 --> A7 --> A8
    D4 -- No --> M5 --> D4

    classDef admin fill:#e6f2ff,stroke:#003366,stroke-width:1px;
    classDef manager fill:#ffe6e6,stroke:#660000,stroke-width:1px;
```

#### Access Area Procedures
Procedure to Access Secure Areas
Managing access to secure areas is critical to protecting sensitive information and maintaining operational security. This procedure outlines the steps for requesting, approving, and monitoring access to secure areas within Arabian Mills.

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Request Access: Request IT & Cybersecurity Manager for access to secure areas for vendors, third-party, and consultants through filling out the access to secure area form. | Preparer: Requestor | As needed |
| 2 | Approve Access: Access to secure areas required by vendors, third-party, and consultants must be approved. | Preparer: IT & Cybersecurity Manager | As needed |
| 3 | Monitor Loading/Unloading Area: Access to loading and unloading areas must be monitored. | Preparer: IT Network and System Admin | Ongoing |
| 4 | Fill Datacentre Access Register: Data Center Register must be filled for Datacentre Access by vendors, third-party, and consultants. | Preparer: IT Network and System Admin | As needed |
| 5 | Maintain Access Approval Emails: Access approval forms to be maintained for 1 year. | Preparer: IT Network and System Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Access Secure Areas Procedure  

**Roles / Swimlanes:**
- Requestor  
- IT & Cybersecurity Manager  
- IT Network and Server Admin  

---

### Steps

| Step # | Role                        | Action                                                                                                                                           | Decision / Next Step                          |
|--------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 1      | Requestor                   | Request IT Manager for access to secure area for vendors, third-parties, and consultants by filling the security access request form.            | Goes to Step 2                                |
| 2      | IT & Cybersecurity Manager  | Approved                                                                                                                                         | **Yes** → Step 3  /  **No** → Step 6 (End)    |
| 3      | IT Network and Server Admin | Access to loading and unloading areas may be monitored. (M)                                                                                      | Goes to Step 4                                |
| 4      | IT Network and Server Admin | Data Center Register must be filled out for all employees, service providers, vendors, and consultants. (M)                                     | Goes to Step 5                                |
| 5      | IT Network and Server Admin | Access approval forms to be maintained for 1 year. (M)                                                                                           | Goes to Step 6 (End)                          |
| 6      | —                           | End                                                                                                                                              | —                                             |

---

### Branch Tracing

- From Step 2 (Approved? decision):
  - **Yes** → Step 3 → Step 4 → Step 5 → Step 6 (End)
  - **No** → Step 6 (End)

---

### Mermaid.js Diagram

```mermaid
graph TD

    A[Start] --> B[1. Request IT Manager for access to secure area for vendors, third-parties, and consultants by filling the security access request form. (Requestor)]

    B --> C{2. Approved (IT & Cybersecurity Manager)}

    C -- Yes --> D[3. Access to loading and unloading areas may be monitored. (M) (IT Network and Server Admin)]
    D --> E[4. Data Center Register must be filled out for all employees, service providers, vendors, and consultants. (M) (IT Network and Server Admin)]
    E --> F[5. Access approval forms to be maintained for 1 year. (M) (IT Network and Server Admin)]
    F --> G[End]

    C -- No --> G
```

#### Secure Areas
Secure areas are designated locations within Arabian Mills that require restricted access due to the sensitive nature of the information and activities conducted within them. These areas are protected to ensure the confidentiality, integrity, and availability of critical information assets.
1. Data Center
The Data Center is a secure area where critical IT infrastructure, servers, and network equipment are housed. Access to the Data Center is strictly controlled to protect sensitive data and ensure the reliability of IT services.
2. IT Load-Unloading Area
The IT Load-Unloading Area is a secure location where IT equipment and supplies are received and dispatched. This area is monitored to prevent unauthorised access and ensure the secure handling of IT assets.
3. IT Team Working Area
The IT Team Working Area is a designated space within Arabian Mills where IT personnel conduct their daily operations. Access to this area is restricted to authorised IT staff to maintain the security of ongoing projects and sensitive information.
#### Annexure

**[Diagram — Visio-EMF→PNG]:**

Access Review List  
Format.pdf


**[Diagram — Visio-EMF→PNG]:**

Data Center Access Register.pdf