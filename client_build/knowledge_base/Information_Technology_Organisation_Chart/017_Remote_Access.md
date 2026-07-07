---
Department: Information Technology Organisation Chart
Section: Remote Access
Section_Kind: core
Section_Priority: normal
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 2
---

## Remote Access

#### Purpose
The purpose of this procedure is to establish a secure and efficient framework for remote access to Arabian Mills' IT systems. By defining clear protocols and responsibilities, the organisation aims to facilitate authorised remote access while ensuring the confidentiality, integrity, and availability of its information assets.
#### Scope
This procedure applies to all employees and vendors requiring remote access to Arabian Mills' IT systems. It covers the process for requesting, approving, enabling, and monitoring remote access, ensuring compliance with security policies and standards.
#### Procedure Reference
This procedure refers to the Identity & Access Control Management Guidelines of ARABIAN MILLS Information Security, ensuring alignment with overarching security policies and standards.
#### Objectives
The objectives of this procedure are to:
 Facilitate Secure Remote Access: Provide a secure method for employees and vendors to access Arabian Mills' IT systems remotely.
 Ensure Compliance: Ensure that remote access is granted in accordance with security policies and guidelines.
 Monitor and Manage Access: Continuously monitor remote access sessions to detect and respond to any suspicious activity.
 Protect Information Assets: Safeguard the confidentiality, integrity, and availability of information assets during remote access sessions.
#### Remote Access Procedure
The secure and efficient management of remote access is critical to maintaining data security and operational efficiency. The following table outlines the activities and responsibilities involved in the remote access process:

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Fill Remote Access Request Form: Requester fills the Remote Access Request Form. For vendors, the concerned department fills the form. Security Team determines if the Vendor Remote Access Agreement is required. | Preparer: Requester | As needed |
| 2 | Review and Approve Request: Line manager and IT & Cybersecurity Manager review and approve the request for remote access. | Reviewer: Line Manager/ IT & Cybersecurity Manager | As needed |
| 3 | Enable Access: System administrator enables access for the specified IP address. Ensure session timeout after 5 minutes of inactivity for VPN access. Create a unique user for each request. | Preparer: IT Network and System Admin | As needed |
| 4 | Set Access Duration: Access is enabled for the approved duration with automatic expiry date set. | Preparer: IT Network and System Admin | As needed |
| 5 | Monitor Activity Logs: Activity logs are monitored during remote access sessions. Investigate any suspected high bandwidth usage and terminate connection if necessary. | Preparer: IT Network and System Admin | Ongoing |
| 6 | Maintain Documentation: Remote Access Request Forms & Vendor Remote Access Agreement are maintained for 3 year s . | Preparer: IT Network and System Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Remote Access Procedure

**Roles / Swimlanes:**

- Requester  
- Line Manager/IT & Cybersecurity Manager  
- IT Network and System Admin  

---

### Steps

| Step # | Role                                   | Action                                                                                                                                                             | Decision / Next Step                                                                                                                                                                      |
|--------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Requester                              | **Start**                                                                                                                                                          | Proceeds to Step 2.                                                                                                                                                                       |
| 2      | Requester                              | `1. Requester fills the Remote Access Request Form. For [illegible] department fills this form. (A)`                                                              | Proceeds to Step 3.                                                                                                                                                                       |
| 3      | Line Manager/IT & Cybersecurity Manager | Decision: `Approved`                                                                                                                                               | If approved: proceed to Step 4 (System administrator enables access for the specified IP address). No alternate (e.g., “Not approved”) path is shown in the diagram.                     |
| 4      | IT Network and System Admin            | `3. System administrator enables access for the specified IP address. (M)`                                                                                        | Proceeds to Step 5.                                                                                                                                                                       |
| 5      | IT Network and System Admin            | `4. Access is enabled for the approved device with automatic expiry date set. (M)`                                                                                | Proceeds to Step 6.                                                                                                                                                                       |
| 6      | IT Network and System Admin            | `5. Activity logs are monitored during remote access sessions. (A/M)`                                                                                             | Proceeds to Step 7.                                                                                                                                                                       |
| 7      | IT Network and System Admin            | `6. Remote Access Request Form and Remote Access Agreements are retained for 3 years. (M)`                                                                        | Proceeds to Step 8.                                                                                                                                                                       |
| 8      | IT Network and System Admin (end state location in diagram) | **End**                                                                                                                                                            | Process terminates.                                                                                                                                                                       |

---

### Mermaid.js Diagram

```mermaid
graph TD

    %% Roles as subgraphs for visual grouping
    subgraph R[Requester]
        A([Start])
        B[1. Requester fills the Remote Access Request Form.<br/>For [illegible] department fills this form. (A)]
    end

    subgraph LM[Line Manager/IT & Cybersecurity Manager]
        C{Approved}
    end

    subgraph IT[IT Network and System Admin]
        D[3. System administrator enables access for the specified IP address. (M)]
        E[4. Access is enabled for the approved device with automatic expiry date set. (M)]
        F[5. Activity logs are monitored during remote access sessions. (A/M)]
        G[6. Remote Access Request Form and Remote Access Agreements are retained for 3 years. (M)]
        H([End])
    end

    A --> B
    B --> C
    C -->|Approved| D
    D --> E
    E --> F
    F --> G
    G --> H
```

#### Annexure

**[Diagram — Visio-EMF→PNG]:**

Remote Access Annexure.pdf