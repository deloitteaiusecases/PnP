---
Department: General
Section: Policies & Procedure for Supplier Qualification
Section_Kind: core
Section_Priority: normal
Source: SCM_Procurement Policy and Procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Policies & Procedure for Supplier Qualification

Policies
The following policies govern the supplier qualification process at Arabian Mills to ensure that only competent, reliable, and compliant vendors are approved for procurement activities.
Approved Vendors List
 An official Approved Vendors List must be established and maintained by the Supply Chain Department. This list shall be developed based on a structured supplier selection and qualification procedure and must be used for all RFQ issuances.
Data Collection
 Comprehensive data must be collected for both existing and potential suppliers or service providers. This includes technical and financial data, which will assist in evaluating and selecting suitable suppliers.
Data Integrity and Security
 All supplier-related data collected during the qualification process must be treated as confidential. This information is not to be shared externally or with unauthorized personnel.
Ethical Practices
The supplier qualification process must be conducted in adherence to ethical principles, including:
   Avoidance of conflicts of interest
   Integrity in data handling
   Confidentiality of supplier information
   Transparent declarations of interests
   Ethical supplier engagement and relationship management
Transparency
 Qualification and selection criteria must be clearly communicated and transparent to all participating suppliers. Suppliers that are not selected must be informed of the reasons for rejection to support future improvement.
Fairness
 All suppliers and service providers must be granted equal opportunity to qualify based on their technical capabilities, financial strength, and performance. No preferential treatment shall be allowed.
Procedure
This procedure outlines the steps for qualifying new suppliers at Arabian Mills It includes public invitation, data collection, evaluation against predefined criteria, and formal approval to ensure that only competent and reliable vendors are added to the Approved Vendors List.

| S. No. | Responsibility | Procedure Description | Output / Report |
| --- | --- | --- | --- |
|  | Procurement Officer | Publish an advertisement in a local newspaper, Government Tender Bulletin, or issue direct invitations to prospective suppliers to apply for registration in relevant commodities and service categories. This process must be repeated every two years. | Advertisement |
|  | Prospective Providers and Suppliers | Submit a formal letter or application expressing their interest in registering as a supplier with Arabian Mills The company must compile and maintain a list of all applicants. | Official Letter / Supplier List |
|  | Procurement Officer | Request the listed suppliers to submit essential documents for supplier profiling, including entity name, registration numbers, address, ownership details, Zakat certificate, bank details, product/service list, capacity, references, etc. | Supplier Profile Information |
|  | Procurement Officer | Collect additional background information on each listed supplier using available internal and external sources (sales reps, trade journals, directories, experience, online research, etc.). | Supplier Background Data |
|  | Procurement Manager | Evaluate each supplier’s compliance with basic requirements and assess against 10 defined evaluation criteria. Each criterion carries 10 marks, with a total of 100. A minimum score of 70 is required for approval. | Evaluation Report / E-mail |
|  | Procurement Manager | Prepare the list of qualified suppliers based on evaluation results and submit it to the Supply Chain Director and COO for formal approval. | Approved Suppliers List |
|  | Procurement Officer | Notify any supplier that fails to meet qualification requirements. The rejection notice must include reasons for non-selection to support future improvement. | Rejection Notification Email |

Flowchart

**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Supplier Qualification  

**Header (top-right of diagram):** Procuremment  

**Roles / Swimlanes (from top to bottom):**
1. Existing & New Supplier  
2. Procurement Officer  
3. Procurement Manager, SC Director  
4. COO  
5. CFO / CEO  

---

### Steps

| Step # | Role                             | Action / Step Name                           | Decision / Next Step                                                                                                                                                          |
|--------|----------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Procurement Officer              | **Start**                                    | Flow begins at “Start” and moves to **Advertisement**.                                                                                                                        |
| 2      | Procurement Officer              | **Advertisement**                            | Next: **Invitation Letter and Application** (in Existing & New Supplier lane).                                                                                                |
| 3      | Existing & New Supplier          | **Invitation Letter and Application**        | Next: **Evaluation Document**.                                                                                                                                                |
| 4      | Existing & New Supplier          | **Evaluation Document**                      | Next: **Evaluation Report** (in Procurement Officer lane).                                                                                                                    |
| 5      | Procurement Officer              | **Evaluation Report**                        | Next: **Submitted Prospective Supplier List**.                                                                                                                                |
| 6      | Procurement Officer              | **Submitted Prospective Supplier List**      | Next: sent for approval to COO via decision **“Aproved”**.                                                                                                                   |
| 7      | COO                              | **Aproved** (decision diamond)               | If **Yes** (labelled “Yes” in green): flow continues to **Approved Prospective Supplier List**. If **No** (labelled “No” in red): flow does not continue (process ends / not approved). |
| 8      | Procurement Officer              | **Approved Prospective Supplier List**       | Next: sent for approval to CFO / CEO via decision **“Aproved”**.                                                                                                             |
| 9      | CFO / CEO                        | **Aproved** (decision diamond)               | If **Yes** (labelled “Yes” in green): flow continues to **End**. If **No** (labelled “No” in red): flow does not continue (process ends / not approved).                      |
| 10     | Procurement Officer              | **End**                                      | Process terminates.                                                                                                                                                           |
| —      | Procurement Manager, SC Director | *(no explicit steps or shapes shown)*        | This swimlane appears in the diagram but contains no activities or decisions.                                                                                                 |

Red text “No” appears next to the rejection paths from each “Aproved” decision.  
Green text “Yes” appears next to the approval paths from each “Aproved” decision.

---

### Mermaid.js diagram

```mermaid
graph TD

    %% Swimlane-style grouping (for visual clarity only)
    subgraph Existing_&_New_Supplier
        INV["Invitation Letter and Application"]
        EDOC["Evaluation Document"]
    end

    subgraph Procurement_Officer
        START["Start"]
        ADV["Advertisement"]
        EREP["Evaluation Report"]
        SUBLIST["Submitted Prospective Supplier List"]
        APPLIST["Approved Prospective Supplier List"]
        END["End"]
    end

    subgraph Procurement_Manager_SC_Director
        PMSCD[/"(No explicit steps shown)"/]
    end

    subgraph COO
        COOAPP{"Aproved"}
    end

    subgraph CFO_CEO
        CFOAPP{"Aproved"}
    end

    %% Main flow
    START --> ADV
    ADV --> INV
    INV --> EDOC
    EDOC --> EREP
    EREP --> SUBLIST

    %% COO decision
    SUBLIST --> COOAPP
    COOAPP -->|Yes (green "Yes")| APPLIST
    COOAPP -->|No (red "No")| REJECT1[/"No - Not approved (process ends)"/]

    %% CFO/CEO decision
    APPLIST --> CFOAPP
    CFOAPP -->|Yes (green "Yes")| END
    CFOAPP -->|No (red "No")| REJECT2[/"No - Not approved (process ends)"/]
```