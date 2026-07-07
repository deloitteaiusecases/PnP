---
Department: Information Technology Organisation Chart
Section: Data Management and Compliance
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Data Management and Compliance
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 3
---

## Data Management and Compliance

#### Purpose
The purpose of this policy is to establish standards for information classification, labelling, and media disposal within Arabian Mills. These standards are designed to protect sensitive information, ensure compliance with legal and regulatory requirements, and support effective data management practices.
#### Scope
This policy applies to all information assets and media within Arabian Mills, including electronic and physical formats. It covers the classification, labelling, and disposal of information to safeguard confidentiality, integrity, and availability.
#### Procedure Reference
This policy refers to the Information Classification & Media Handling Guidelines of ARABIAN MILLS Information Security, ensuring alignment with overarching security policies and standards.
#### Objectives
The objectives of this policy are to:
 Ensure Proper Classification: Classify information based on its value, sensitivity, legal requirements, and impact on operations.
 Implement Effective Labelling: Label information assets clearly to communicate their classification and required protection levels.
 Facilitate Secure Disposal: Establish procedures for the secure disposal of media containing sensitive information.
 Support Compliance: Ensure compliance with legal, regulatory, and organisational requirements for data management.
#### Responsibility
It is the responsibility of the Cybersecurity Manager/IT & Cybersecurity Manager to ensure the proper implementation of this policy. The policy shall be reviewed and updated as necessary or at least annually by the IT & Cybersecurity Manager.
#### Information Classification & Labelling Standard
Classification
1. Information must be classified in terms of its value, legal requirements, sensitivity, and criticality to ARABIAN MILLS. Asset owners must classify assets according to appropriate classification guidelines.
2. Classification levels are identified based on the impact on services/processes if confidentiality, integrity, or availability is compromised.
3. Files/emails created by individuals must be owned and classified by them.
4. Information stored in different media formats must have the same level of classification.
5. Information must be treated according to its need for protection, irrespective of the media on which it is stored.
6. Recipients must treat information according to the classification established by the originator/issuer.
Identification and Creation
1. The protection class must be visible to the recipient right away.
2. With written information, the label must be in an area where it is readily visible and easy to read, such as:
3. On the first page of paper documents and their electronic versions.
4. On the labelling area of data storing media such as CDs and backup devices.
5. In the footer of electronic information.
#### Information Classification Matrix
Information owners of ARABIAN MILLS must use the following matrix to classify information assets in a manner that balances the risk of compromise with the needs of normal operations.

| Classification Level | Definition | Examples |
| --- | --- | --- |
| Strictly Confidential | Applies to sensitive information, the unwanted disclosure of which can lead to grave legal consequences. Access is restricted to select employees or entities. | Strategies, technology planning, vendor agreements, security measures |
| Confidential | Applies to sensitive information for which unwanted disclosure can have damaging consequences. Accessible to named employees on a need-to-know basis. | Internal communications, service-related documents |
| Internal | Applies to information accessible to all employees but not intended for outsiders. | Internal guidelines, circulars, policies |
| Public | Applies to information approved by management for public release. | Service brochures, advertisements, press releases |

#### Declassification of Information
1. The designated information owner has sole rights to declassify the information at any time. To achieve this, the owner must change the classification label, along with the version number, appearing on the document and inform the original / intended recipients / users.
2. The designated information owner may, at any time prior to scheduled declassification or downgrading, extend the period that information is to remain at a certain classification level.
#### Media Disposal Procedure
The secure disposal of media containing sensitive information is critical to maintaining data security and compliance. The following table outlines the activities and responsibilities involved in the media disposal process:

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Identify Information for Disposal: Information owner identifies information for disposal and fills the Media Disposal Form if required. | Preparer: Information Owner | As needed |
| 2 | Approval for Confidential Information: Approval from line manager is required for disposal of "Strictly Confidential" or "Confidential" information. Identify mode of disposal. | Reviewer: Line Manager | As needed |
| 3 | Dispose Media: Disposal of document/media is done in the presence of the information owner. | Preparer: IT Network and Server Admin | As needed |
| 4 | IT & Cybersecurity Manager Backup Media Disposal Approval: Approval needed from IT & Cybersecurity Manager for backup media disposal. Inform them once disposal is complete via email. | Reviewer: IT & Cybersecurity Manager | As needed |
| 5 | CFO Manager Backup Media Disposal Approval: Approval needed from IT & Cybersecurity Manager for backup media disposal. Inform them once disposal is complete via email. | Reviewer: CFO | As needed |
| 6 | Update Asset Inventory: Update the asset inventory for backup media. | Preparer: Finance Department User | As needed |
| 7 | Maintain Disposal Form: Disposal Media form is maintained for a period of 3 year s . | Preparer: IT Network and Server Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Media Disposal Procedure

**Roles / Swimlanes:**

1. Information Owner  
2. Line Manager  
3. IT Network & Server Admin  
4. IT & Cybersecurity Manager  
5. CISO  
6. Finance  

---

### Steps

| Step # | Role                        | Action                                                                                                                                              | Decision / Next Step                                                                                                  |
|--------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1      | Information Owner           | Information owner identifies information for disposal and fills the Media Disposal Form if required. (M)                                           | Goes to Step 2 (approval decision by Line Manager).                                                                   |
| 2      | Line Manager                | Approved?                                                                                                                                            | If **Yes** → Step 3. If **No** → (implied: process stops / return to Information Owner; no further step shown).       |
| 3      | IT Network & Server Admin   | Disposal of document/media is done in the presence of the information owner. (A/M)                                                                 | After disposal, goes to Step 4 (approval decision by IT & Cybersecurity Manager).                                     |
| 4      | IT & Cybersecurity Manager  | Approved?                                                                                                                                            | If **Yes** → Step 5 (approval decision by CISO). If **No** → (implied: process stops / revisit previous step).        |
| 5      | CISO                        | Approved?                                                                                                                                            | If **Yes** → Step 6 (Finance updates asset inventory). If **No** → (implied: process stops / revisit previous step).  |
| 6      | Finance                     | Update the asset inventory for backup media. (M)                                                                                                    | After updating inventory, parallel update of form in same step number; then proceeds to Step 7.                       |
| 7      | IT Network & Server Admin   | Disposal Media form will be maintained for a period of 3 years. (M)                                                                                | Then **End**.                                                                                                         |
| 8      | —                           | End                                                                                                                                                 | Terminal step of the process.                                                                                         |

---

```mermaid
graph TD

A[Start]

%% Step 1
A --> B[1. Information owner identifies information for disposal and fills the Media Disposal Form if required. (M)]

%% Step 2 - Line Manager approval
B --> C{2. Approved? (Line Manager)}

C -- Yes --> D[3. Disposal of document/media is done in the presence of the information owner. (A/M)]
C -- No --> Z1[Process not approved / return to Information Owner]

%% Step 4 - IT & Cybersecurity Manager approval
D --> E{4. Approved? (IT & Cybersecurity Manager)}

E -- Yes --> F{5. Approved? (CISO)}
E -- No --> Z2[Process not approved / revisit disposal step]

%% Step 5 - CISO approval
F -- Yes --> G[6. Update the asset inventory for backup media. (M)]
F -- No --> Z3[Process not approved / revisit previous step]

%% Step 7 - Maintain form
G --> H[7. Disposal Media form will be maintained for a period of 3 years. (M)]

H --> I[End]
```

#### Data Sanitisation Procedure
To ensure the complete removal of sensitive data from media, Arabian Mills has established a comprehensive data sanitisation procedure. This procedure involves selecting appropriate sanitisation methods, using industry-standard tools, and verifying the effectiveness of data removal. The following table outlines the activities and responsibilities involved in the detailed data sanitisation process:

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Identify Media for Sanitisation: Determine the type and classification level of media to be sanitised. | Preparer: Information Owner | As needed |
| 2 | Select Sanitisation Method: Choose the appropriate method for data sanitisation (e.g., overwriting, degaussing, encryption, physical destruction) based on media type and sensitivity. | Preparer: IT Network and System Admin | As needed |
| 3 | Standardise Tools: Use industry-standard tools and software for effective data removal. Ensure tools are up-to-date and meet security standards. | Preparer: IT Network and System Admin | Regularly |
| 4 | Prepare for Sanitisation: Back up any necessary data before sanitisation and secure the media for processing. | Preparer: IT Network and System Admin | Before each sanitisation cycle |
| 5 | Execute Sanitisation: Apply the selected sanitisation method using standardised tools to ensure complete data removal. | Preparer: IT Network and System Admin | During each sanitisation cycle |
| 6 | Verify Data Removal: Conduct verification processes using audits or validation software to ensure no residual data remains on the media. | Preparer: IT Network and System Admin | After each sanitisation cycle |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Data Sanitisation Procedure  

**Roles / Swimlanes:**
- Information Owner  
- IT Network and System Admin  

---

### Steps

| Step # | Role                          | Action | Decision/Next Step |
|--------|-------------------------------|--------|---------------------|
| 0      | —                             | **Start** | Proceed to Step 1 |
| 1      | Information Owner             | 1. Determine the type and classification level of media to be sanitised. (M) | Proceed to Step 2 |
| 2      | IT Network and System Admin   | 2. Choose the appropriate method for data sanitisation (e.g., overwriting, physical destruction, degaussing), depending on classification level, type and sensitivity. (M) | Proceed to Step 3 |
| 3      | IT Network and System Admin   | 3. Use industry-standard tools and hardware for effective sanitisation. Ensure tools are up-to-date and meet security standards. (A/M) | Proceed to Step 4 |
| 4      | IT Network and System Admin   | 4. Back up any necessary data before performing sanitisation to ensure no valuable information is lost. (A/M) | Proceed to Step 5 |
| 5      | IT Network and System Admin   | 5. Apply the selected sanitisation methods using standard tools to ensure complete data removal. (A/M) | Proceed to Step 6 |
| 6      | IT Network and System Admin   | 6. Conduct verification processes, such as audits or validation tests, to ensure the information is removed from the media. (A/M) | Proceed to Step 7 |
| 7      | —                             | **End** | — |

*(No explicit Yes/No decision branches are shown in the diagram; the flow is linear from Start to End.)*

---

```mermaid
graph TD

    A0([Start])
    A1[1. Determine the type and classification level of media to be sanitised. (M)\nRole: Information Owner]
    A2[2. Choose the appropriate method for data sanitisation (e.g., overwriting, physical destruction, degaussing), depending on classification level, type and sensitivity. (M)\nRole: IT Network and System Admin]
    A3[3. Use industry-standard tools and hardware for effective sanitisation. Ensure tools are up-to-date and meet security standards. (A/M)\nRole: IT Network and System Admin]
    A4[4. Back up any necessary data before performing sanitisation to ensure no valuable information is lost. (A/M)\nRole: IT Network and System Admin]
    A5[5. Apply the selected sanitisation methods using standard tools to ensure complete data removal. (A/M)\nRole: IT Network and System Admin]
    A6[6. Conduct verification processes, such as audits or validation tests, to ensure the information is removed from the media. (A/M)\nRole: IT Network and System Admin]
    A7([End])

    A0 --> A1 --> A2 --> A3 --> A4 --> A5 --> A6 --> A7
```

#### Annexure

**[Diagram — Visio-EMF→PNG]:**

Media Disposal  
Form.pdf