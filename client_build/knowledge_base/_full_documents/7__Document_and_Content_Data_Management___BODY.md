---
Department: FULL_DOCUMENT
Section: FULL_DOCUMENT
Section_Kind: full_document
Section_Priority: high
Source: 7__Document_and_Content_Data_Management_.docx
Document_Title: 7__Document_and_Content_Data_Management_
Document_Class: full_document
Document_View: body
Is_Full_Document: true
---

## Purpose
# Policy
## Purpose

The  Policy (' 'the policy') sets out the guidelines, framework, and key roles and responsibilities concerning the management of data in  ('' or 'the '). Through this policy, the  will:

- Establish robust data management and ensure effective oversight, monitoring, and management of data assets.

- Ensure comprehensive controls are in place to ensure data cataloguing, data sharing data quality, accuracy, availability, integrity, and completeness.

- Promote data management awareness amongst the 's employees; and

- Leverage existing data assets to derive business value.

## Policy Scope and Applicability
This policy applies to all Business Units (BU), support functions, vendors/ third parties (undertaking any data-related activities for the ), employees (insourced, outsourced & contractual), members of the Board and its committees, and management committees.
() owns this policy, and it is subject to be reviewed every two (2) years or when deemed necessary. This policy will be reviewed and approved as per the standard  protocols applicable for other enterprise level policies.
This  Policy set out the overall Data Management Framework of . In case the provision of any other policy conflict with or are inconsistent with this policy, the provision of this Policy will prevail. If there are questions regarding the interpretation of applicable sections of this policy, the matter should be raised immediately to  for clarifications.

## Policy Governance, Ownership, Custody and Circulation
The roles & responsibilities for the approval and implementation of this policy are listed below:
Governance

| Responsibility | Function |
| --- | --- |
| Approval and oversight |  |
| Oversight, enforcement & recommendation to BOD |  |
| Document owner and implementations |  |
| Periodic review of policy |  |
Policy Governance Support

| Responsibility | Function |
| --- | --- |
| Policy custodian |  |
| Content issuance/ review |  |
| Periodic audit review |  |
This policy will be distributed to all  employees. All  employees are responsible for familiarizing themselves and ensuring compliance with the Policy requirements.
Update and maintenance of the document
1. The standards laid down by the Board through this document may be subject to changes, as deemed appropriate by the Board to ensure appropriate oversight and control over the ’s affairs. Such changes may be required due to one or more of the following reasons:
a) Changes in applicable laws, regulatory requirements / standards and specific instructions from governmental, legal and regulatory authorities
b) Changes in governance and organizational structures including institution of new committees or changes in the existing committees, changes in terms of references of groups / divisions and changes in the roles and responsibilities of relevant stakeholders
c) Inclusion of new data processes in the
d) New data management and application roles that are not envisioned or included in this document
e) Changes in data governance roles, responsibilities, or accountability matrix (as per the data governance handbook)
f) Any other change as deemed necessary by the Board
2. A formal 'Amendment Request Form' describing the proposed revision/ amendment shall be prepared by the person requesting changes (or 'requestor'). The amendment request inclusion and approval process will be as follows:
a) The requestor will complete the amendment request form, detailing the justification for changes to the policy document.
b) The amendment request form must be submitted to the Senior Manager, Data Governance and subsequently to the DG Management and Leadership Team for review and approval.
c) After approval is obtained from the DG Council, the amendment request form has to be submitted by PPU to the PPC members for their level of approval.
3. The Management of the  shall also have the right to propose amendments to the policy based on evolving circumstances and business needs. The Board, at its sole discretion shall have the authority to accept or reject such proposed changes and authorize amendment of the policy accordingly, if required.
a) will be responsible to carry out the required changes as directed by the Board and present the revised / updated policy to the Board for formal approval of the revised version.
b) Once the Board has approved an updated version of the policy,  will coordinate with PPU and PPU shall take the necessary steps to immediately inform the primary recipients of the changes / amendments, through an internal memorandum. Such revisions may also be communicated via email. The updated policy shall then be circulated, following the same circulation process as defined in the “Ownership, Custody and Circulation” section of this policy.
c) In the event of changes in the policy, the primary recipients shall be responsible to assess if the changes in this policy warrant a change in relevant policies and procedures, and if required, necessary updates to the policies and procedures will be made to ensure alignment with the revised Enterprise Data Governance Policy.

## Applicable Laws and Regulatory Compliance Requirement
This policy adheres to the guidelines and the principles stipulated in:
- National Data Governance Interim Regulations
- National Data Management Office Handbook
- Data Management and Personal Data Protection Standards
The  will also adhere to all other applicable laws and regulations around data governance and data management as and when will be issued by the SAMA, NDMO and other regulators, relevant to the 's operations.
Compliance to applicable laws and regulations shall be provided by the Compliance Group and Internal Audit Department of the .
This policy is for the internal use of , and all employees must ensure its confidentiality at all times. No content of this policy shall be reproduced or transmitted in any form by any means without the written permission of a competent authority.

## Effective Date of Policy
The Policy is effective from the date of its approval by the Board of Directors

## Data Quality
The data quality policy has been developed specifically for , in compliance with relevant Data Management and Personal Data Protection Standards and Interim Regulation issued by the National Data Management Office (NDMO). Inaccurate data, such as outdated customer details, incorrect billing data, erroneous ID information, etc., can cost  to compromise its accuracy in product development, providing excellent customer services, reputation, credibility and operational efficiency.
Data quality is a set of periodic procedures for data processing to ensuring the correctness, accuracy and completeness of data.  Adoption of the data quality management process facilitates providing accurate data to the business functions and thereby enables well-informed business decision making and high operational efficiency.

## Data Quality Dimensions
Data Quality dimensions are measurable features or characteristics of data, which are used to define results of initial data quality assessment as well as ongoing measurements. To measure the quality of data,  needs to establish characteristics that are both important to its business processes (worth measuring) and measurable.
While considering data quality at , below defined best practice core dimensions of data quality, which can be measured or assessed against defined standards, are to be followed.

| Data quality D imension | Definition | Data Example for [client] |
| --- | --- | --- |
| Completeness |
- Data completeness refers to whether the data required to meet the business information demand are available.<br>
- Completeness can be measures at the data set, record, or column level. Data can be complete even if optional data is missing, as long as the data meets the expectations. | Completeness of Customer Identification data ( Customer Name and Customer ID Number ) for all on-boarded customers |
| Uniqueness | **Uniqueness states that no entry exists more than once within the same data set**<br>
- Asserting uniqueness of entities within a data set implies that a key value relates to each unique entity/individual, and only to that specific entity/individual, within the dataset | Customer Identification data ( Customer Name and Customer ID Number ) is a unique data, two different Names/ID numbers of same customer cannot exist |
| Timeliness | Degree to which data is current and available for use in the expected time frame | Timeliness of Customer’s Address change data implies updating the address change in the database within the stipulated time period (For example, SLA of 7 days) |
| Validity |
- The conformity of data to the standards and syntax. Data is valid if it conforms to the syntax (format, type, range) of its definition<br>
- It is the level of data matching a reference | As the VAT Registration number is a 15-digit number, a VAT Registration number with <15 or >15 digits in the database will be invalid (data level validity) |
| Accuracy |
- The degree to which data correctly describes the "real world" object or the event being described<br>
- For a data to be accurate, values must be valid, and in the correct representation |
- While loading Credit Card Bill Issue Date , the format followed by data provider needs to match with the format followed in the organization data platform(s).<br>
- Entering US date formatted data (MM/DD/YYYY) to European date formatted (DD/MM/YYYY) database will cause the reversed representation of day and month |
| Consistency |
- Consistency is the absence of difference, when comparing multiple (two or more) representations of same data<br>
- Data elements having reliably the same definition and meaning across all data sources | The Street Address data of a particular Vendor is same across all the data sources without conflicting information. |
Table 1: Data Quality Dimensions/Criteria

## Policy Statements
The below statements of policy are defined as the foundation of  view on data quality and should guide all actions in creating, maintaining, and using data quality standards across the . These statements are:

- Create Data Quality Plan based on ’s defined Data Strategy and Plan, to implement and manage activities aiming to improve quality of ’s data.

- Ensure performing Data Quality Assessment on the data to prioritize the importance and criticality for Data Quality Management as per NDMO guidelines on Data Management and Personal Data Protection Standards. The master data can be given the highest priority.

- Develop a comprehensive list of data quality rules to monitor critical data assets across their entire lifecycle and to ensure that the data is up-to-date, complete and of sufficient quality appropriate to support its intended use.

- Update the full list of data quality rules periodically to accommodate new business requirements, new systems, changing data landscape as required.

- Build a portfolio of reconciliatory requirements to ensure the accuracy and completeness of data getting populated at the reporting layer.

- Implement automated data catalog tool to improve the quality of data.

- Create workflow(s) within automated data catalog tool to report data quality issues to the stewardship team (e.g., Business Domain Steward)

- Establish data quality and governance KPIs and scorecards to monitor data quality on a continuous basis; and

- Develop remediation solutions comprising of people, process and technology fixes to fully mitigate data issues considering the importance of quality and value of the data asset, by liaising with all key stakeholders.

- Data quality management is not a one-time initiative, but an ongoing commitment by the .

- Data quality management is the accountability of the data owners.

- Data quality management is the responsibility of all the personnel working with data.

- employees are responsible and accountable for highlighting any non-compliance or issues with the responsible data architect, stewardship team or data owner.

## Data Quality Principles
as financial institution should adhere to the following principles while managing data quality programs and processes:
1. Criticality: Data Quality program and processes should focus on the data which is most critical to the program, stakeholders, and customers. Priorities for improvement should be based on the criticality of the data and on the level of risk if a particular data is not correct shape.
2. Lifecycle management: Data quality should be managed across the data lifecycle, from creation or procurement through disposal. This includes managing data as it moves within and between systems, i.e., each link in the data chain should ensure data output is of high quality.
3. Prevention: The focus of a Data Quality program should be on preventing data errors and conditions that reduce the usability of data; it should not be focused on simply correcting records.
4. Root cause remediation: Improving the quality of data goes beyond correcting errors. Problems with the quality of data should be understood and addressed at their root causes, rather than just their symptoms. Because these causes are often related to process or system design, improving data quality often requires changes to processes and the systems that causes data quality issues.
5. Governance: Data management & governance activities must support the development of high-quality data and at the same time, data quality program activities must support and sustain a governed data environment.
6. Standards-driven: All stakeholders in the data lifecycle have data quality requirements. To the degree possible, these requirements should be defined in the form of measurable standards and expectations against which the quality of data can be measured.
7. Objective measurement and transparency: Data quality levels need to be measured objectively and consistently. Measurements and measurement methodology should be shared with stakeholders since they are the arbiters of quality.
8. Embedded in business processes: Business process owners are responsible for the quality of data produced through their processes and they are obliged to enforce data quality standards within the processes.
9. Systematically enforced: System owners must systematically enforce data quality requirements.
10. Connected to service levels: Wherever possible, data quality reporting and issues management should be incorporated into Service Level Agreements (SLA).

## Roles, Responsibilities and RACI Matrix
The following roles and responsibilities are applicable to this policy:

- Data Management and Governance Leadership Team: The executive body of  data management & governance is responsible for signing off on any changes, exemption, and exceptions to this policy.

- Data Governance Council: The strategic body of  data management & governance authorizes data quality exercises, defines priorities and critical data, and is responsible for approving their outputs.

- Data Governance officer: An experienced business domain representative responsible for managing all data management & governance initiatives and changes. The data governance officer overlooks and manages the delivery of data quality projects and maintains plans, timelines, budgets, ensuring that progress is made.

- Stewardship Team: The stewardship team is responsible for proposing business rules for data quality, proposing KPIs for monitoring data quality issues through reviewing profiling reports before and after remediation plans are executed, performing root cause assessment (RCA) to understand data quality issues, prioritizing data quality issues and escalating to the data governance council as required, assessing the rules and dimensions, defining and maintaining technical and business definitions, performing data profiling, and designing data remediation exercises. proposing data quality exercises to the Head of  and executing remediation plans.

- Head of : Head of  responsible for managing all data management & governance initiatives and changes. The Head of  overlooks and manages the delivery of data quality projects and maintains plans, timelines, budgets, ensuring that progress is made.

- Compliance Officer: The Compliance Officer is responsible for monitoring compliance with data management and data management & governance policies and standards. The GRM team supports in the monitoring of KPIs, receive alerts and flags from the wider organization, investigate and act accordingly to resolve them.

- Data Owner: The Data Owner is responsible for providing domain-specific executive-level support in data quality exercises, communicating the results of the exercises across the business domain and maintaining the established data quality standards in their domain.

- Data Quality Analyst: The Data Quality Analyst having deep understanding of the business responsible for the identification and documentation of the requirements and assessment criteria for the data quality exercises. Data Quality Analyst leads the initiatives to develop and document data quality rules, which define the business requirements for data quality, for all the data points in the  data platform.

- Data Architect: Data Architecture responsible for supporting data quality exercises. Their deep knowledge of the ’s data architecture allows them to validate the impact of data quality exercises on underlying data models, thus ensuring that data quality is consistent in the information systems and all the architectural documents are in line with the data quality rules. Responsible for carrying out the implementation activities of data quality projects and design relevant system changes, prove the viability for implementation. Receives and validates changes made on the development and test environments and deploys into production for all relevant databases.

- Data User: Any individual interacting with the data without having direct control over it. The data users are responsible for raising data quality issues that surface while interacting with the data.

- Data Specialist: Data Specialist is responsible Defining and maintaining technical and business definitions and develop data quality rules

| Control Activity | The Board | DG Leadership Team | Head of data management | Compliance Officer | DG Officer | DG Council | Data Owner | Data Quality Analyst | Data Architect | Data User | Stewardship Team | Data Specialist |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Control Activity | The Board | DG Leadership Team | Head of data management | Compliance Officer | DG Officer | DG Council | Data Owner | Data Quality Analyst | Data Architect | Data User | Data Domain Steward | Business Domain Steward | Data Steward | Business Steward | Data Specialist |
| Initiating and authorizing data quality management projects |  | C |  | R | A | R | I | C |  | I |  |  |  |  |  |
| Managing data quality projects |  | I |  | R | C | A, R | C |  | C | I | C |  |  |  |  |
| Analyzing, defining / re-defining data quality standards upon program maturity |  | I | C | A | R |  | C | I | C |  |  |  |  |  |  |
| Ensuring Policies and processes are defined for data quality management |  | I |  | R | A | R | C |  | I | C |  |  |  |  |  |
| Identifying and updating data quality KPIs |  | I |  | C | A |  | R | I | C |  |  |  |  |  |  |
| Monitoring data quality issues |  | I |  | C | R | A | I | C | R | I | C |  |  |  |  |
| Identifying and refining requirements for data remediation exercises |  | I |  | C | A, R |  | C |  | C | R | I | C |  |  |  |
| Prioritizing and escalating data quality issues |  | C | R | A |  | C |  | R | C |  |  |  |  |  |  |
| Performing data profiling |  | I |  | I | A | R | C |  | R | C |  |  |  |  |  |
| Planning and implementing data remediation |  | I |  | C | I | R | C | I | R | A | C |  |  |  |  |
| Defining and maintaining technical and business definitions |  | I |  | C | I | R | C | I | R | A | C | R |  |  |  |
| Logging data quality issues |  | I |  | C | I | R | I | R | A | C | C, I |  |  |  |  |
| Maintenance of data architecture documentation |  | I |  | I | C | I | A, R | I | C | I |  |  |  |  |  |
| Raising non-compliance with policy |  | I | A, R | C | I | C |  |  |  |  |  |  |  |  |  |
| Making and approving any exceptions or changes to data quality policy |  | A | C | I | R | I |  |  |  |  |  |  |  |  |  |
| Develop data quality rules |  | C | I | A | R | C | I | R | i | C | R |  |  |  |  |
| Implement and maintain data quality rules |  | I |  | C | I | R | A | C | R | C |  |  |  |  |  |
| Build a portfolio of data reconciliatory requirements |  | I |  | I | R | C |  | C | A | C | R |  |  |  |  |
| Develop and maintain data reconciliation rules |  | I | C | I | C | R | C |  | C | A | C | R |  |  |  |
| Perform Root Cause Assessment (RCA) to understand source of data quality issues |  | I | C | R | C | A | C, I | C | R |  |  |  |  |  |  |

## Data Quality Management KPIs
It is important to measure and analyze the data quality trends and data quality issues resolution efficiency across the  data platform(s) for assessing the overall efficiency of data quality management processes and practices. Head of  is accountable for adopting the Key Performance Indicators (KPIs). The following table delineate the two dimensions, Data Quality Trends and Data Quality Issue Resolution Efficiency, and their corresponding KPIs.

| Category | Metric | Description |
| --- | --- | --- |
| Data Quality Trends | Number of Data Quality Issues reported against each Data Quality Rule implemented | The number of data quality issues reported against each data quality rule implemented is expected to follow a reducing trend as the data quality management program matures |
| Data Quality Trends | Number of Data Quality Issues reported | The number of data quality issues reported is expected to go down as the data quality management program matures |
| Data Quality Trends | Number of Data Quality Rules implemented | The number of data quality rules implemented is expected to lower as the data quality management program matures as it is expected to implement more quality rules during the early phases of the program |
| Data Quality Issue Resolution Efficiency | Number of Data Quality Issues resolved out of reported Data Quality Issues | Measures the efficiency of resolving reported data quality issues and is expected to be scoring high |
| Data Quality Issue Resolution Efficiency | Number of Data Quality Issues resolved after the specified timeline | Measures the efficiency of resolving data quality issues within the specified timeline & It is expected to resolve all the issues within the specified timeline |
| Data Quality Issue Resolution Efficiency | Time taken for developing a remediation plan for an identified Data Quality Issue | Total time taken for developing a remediation plan, expected to be less time |
| Data Quality Issue Resolution Efficiency | Time taken for resolving Data Quality Issue | Time taken for root cause resolution implementation to address identified Data Quality Issue |

## Data Quality Exercises
Based on the dimensions/criteria provided and the approach, data quality exercises are carried out in order to monitor, identify, and address data quality issues. Different types of data quality exercises are detailed in the table below.

| Exercise | Definition |
| --- | --- |
| Data Quality Management | The practice of setting data quality standards and metrics that are applicable to data fields, domains, or subject areas. Data quality management includes the periodic evaluations of data quality against the data definitions and quality metrics, cleansing of erroneous data and root-causes remediation of erroneous data. |
| Data Quality Monitoring | An ongoing exercise that examines data for violations of data standards. The goals of monitoring are to maintain data quality, prevent past issues from recurring and identify previously unidentified data quality issues. |
| Data Quality Profiling | Profiling is a more detailed review of quality than monitoring and focuses on the content of data as well as data standards. Profiling results are documented in audit reports and resolutions are documented in remediation and improvement plans. |
| Data Quality Remediation |
- The exercise of resolving data quality issues, as identified through monitoring and profiling activities. Some examples of data quality remediation involve changes to source systems, business rules, transformation processes in databases, and the redesign of business processes and applicable staff training.<br>
- Whenever quality issues are identified with data from external sources, the same should be reported to the data producer/source, wherever possible. Appropriate data quality remediation plan should be discussed and agreed with the data producer in possible cases. |
| Remediation Plan | The detailed analysis and planning of resolution steps that must be performed to satisfactorily resolve an identified and prioritized data quality issue |