---
Department: FULL_DOCUMENT
Section: FULL_DOCUMENT
Section_Kind: full_document
Section_Priority: high
Source: 13__Open_Data___4_.docx
Document_Title: 13__Open_Data___4_
Document_Class: full_document
Document_View: body
Is_Full_Document: true
---

## . Reference and Master Data Management
The Reference and Master Data Management policy has been developed for , in compliance with relevant Data Management and Personal Data Protection Standards and Interim Regulation issued by the National Data Management Office (NDMO).
Systems and data in most businesses develop more naturally than data management specialists would want. Numerous projects and initiatives, mergers and acquisitions, and other business activity, especially in large businesses, lead to several systems doing basically the same tasks apart from one another. These circumstances necessarily result in differences in data values and data structure between systems. Costs and risks are raised by this unpredictability. Through the management of Master Data and Reference Data, both can be reduced.
Definitions of Reference and Master Data and related terms:

- Master Data: Master data is the consistent and uniform set of identifiers and extended attributes that describes the core entities of the enterprise including customers, prospects, citizens, residents, suppliers, sites, hierarchies, and accounts.

- Reference Data: Reference data are sets of values or classification schemas that are referred to by systems, applications, data stores, processes, and reports, as well as by transactional and master records.

- System of Reference: An authoritative system where data consumers can obtain reliable data to support transactions and analysis, even if the information did not originate in the system of reference. MDM applications, Data Sharing Hubs, and Data Warehouses often serve as systems of reference.

- System of Record: An authoritative system where data is created/captured, and/or maintained through a defined set of rules and expectations (e.g., an ERP system may be the System of Record for sell-to customers).

## .1. Policy Statements
The below statements of policy have been defined as the foundation of ’s view on reference and master data management. These statements are:

- Establish a Reference and Master Data Management capability, a Reference and Master Data Management approach and plan.

- The Reference and Master Data approach and plan shall be approved by the Data Governance Leadership Team and reviewed quarterly to monitor progress.

- Perform an initial review to identify all Reference and Master Datasets, considering internal and external data.

- Identify, document, and prioritize Reference and Master data objects owned by the  and categorize as either internal or external datasets.

- Identify and document data sources and applications where Reference and Master Data objects are created, read, updated, and deleted.

- Datasets shall be grouped logically where possible to create a single source of Reference or Master data, reduce data duplication and to create a common definition across the  for each Master or Reference data record.

- Prioritize the identified Reference and Master Data Objects for determining a phased approach to implement the target RMD Data architecture.

- Develop and document requirements for effectively managing Reference and Master Data across the data lifecycle.

- Reference data assets must be made available for reuse across the .

- Evaluate and select Reference Master Data Hub architecture design to effectively manage and support its Reference and Master Data Objects.

- For the desired Reference and Master Data environment, create conceptual and data architectures, and specify the technical requirements for the Reference and Master Data Hub platform as per prevailing SAMA and NDMO guidelines along with industry standards.

- Develop and document conceptual architecture for target Reference and Master data environment as per the selected Data Hub architecture design.

- Develop and design data architecture for target Reference and Master data environment based on defined conceptual architecture design.

- Conduct Reference and Master Data training for employees responsible for managing, creating and updating reference and master data.

- Assign Data Owner and Stewardship team to the identified Reference and Master Data Objects.

- Establish and follow clearly defined Data Lifecycle Management process with roles, responsibilities and actions for Reference and Master Data Objects.

- Implement the Reference and Master Data Hub as the 's Trusted Source as well as document and maintain Reference and Master Data Integration Mappings.

- Monitor and improvise quality of reference and master datasets regularly.

- The data quality issues should be raised and resolved as per the Data Quality Policy.

- Establish Service Level Agreements for Reference and Master Data requests.

- Establish Key Performance Indicators (KPIs) to measure the effectiveness of development of Reference and Master Data capabilities.

- Any exceptions, exemptions and/or changes in this policy should be approved by Data Governance Leadership team.

## .2. Reference and Master Data Management Principles
Reference and Master Data Management follows these guiding principles:

- Shared Data: Enabling Master and Reference Data to be shared across ’s functions and all applications.

- Ownership: Reference and Master Data belong to the , not to a particular Domain. Because being shared cross functionally, require a combined stewardship.

- Quality: Reference and Master Data Management require ongoing Data Quality monitoring and governance.

- Stewardship: Stewardship Team accountable for controlling and ensuring the quality of Reference and Master Data as per the instructions from data owner(s).

- Controlled Change:
  o At a given point of time, Master Data values should represent the ’s best understanding of what is accurate and current. Matching rules that change values should be applied with caution and oversight. Any identifier merged or split should be reversible.
  o Changes to Reference Data values should follow a defined process; changes should be approved and communicated before being implemented.

- Authority: Master Data values should be replicated only from ’s system of record. A system of reference may be required to enable sharing of Master Data across the . Ensuring  has complete, consistent, current, authoritative Master and Reference Data across al processes.

## .3. Roles, Responsibilities and RACI Matrix
The following roles and responsibilities are applicable to this policy
Enterprise Architecture Board (EAB):  EAB is accountable to approve the conceptual and data architectures for the desired Reference and Master data environments
Data Management and Governance Leadership Team: The DG Leadership Team is responsible for the approval for signing off on any changes, exemptions and exceptions to this policy. Further, the DG Leadership will provide strategic direction for Reference and Master Data Management in order to help/support the business operations run smoothly and without any conflict.
Data Governance Council: The Data Governance Council is responsible for implementing Reference and Master Data Hub in the  as a Trusted Source. Monitoring Reference and Master Data quality and monitoring Reference and Master Data KPIs to measure the effectiveness of development of Reference and Master Data capabilities. Further, the DG Council is accountable for approving the conceptual and data architectures for the desired Reference and Master data environments.
Stewardship Team: The Stewardship team is responsible for collecting and evaluating issues of the quality and management of reference and master data. The stewardship team shall work in collaboration with data specialists, data quality analyst and data architect to resolve the identified issues and communicate the data owner(s) and data governance officer upon resolution.
Head of : The Head of  is responsible for overseeing the implementation of data architecture based on conceptual architecture for the desired Reference and Master Data environment.
Sr. Mgr. data Management & Architecture Department: Sr. Mgr. is accountable for Implementing Reference and Master Data Hub, Resolve the Reference and Master Data issues, Monitoring the Reference and Master Data Management KPIs and Responsible for Approve the conceptual and data architectures for the desired Reference and Master data environments, Implementation of data architecture based on conceptual architecture for the desired Reference and Master Data environment, Signing off on any changes, exemptions and exceptions to Reference and Master Data Management policy, Develop MDM and RDM implementation approach.
MDM Team: MDM Team is accountable for Collecting and evaluating issues of the quality and management of reference and master data, Establish and operationalize rules for accurate matching and merging Master Data Records from different data sources to create Golden Records and is responsible for Monitoring Reference and Master Data KPIs, Resolve the Reference and Master Data issues, Raise the identified RMD issues to Data Governance Support or Data Governance Council, Track the resolution of the Reference and Master Data Management issues. Requirements for provisioning of Master Data Golden Records to Requirements for provisioning of requirements for Reference Data Objects to consuming systems and applications, Signing off on any changes, exemptions and exceptions to Reference and Master Data Management policy Approve Reference and Master Data approach and plan, Develop MDM and RDM implementation approach
Data Governance Officer: The Data Governance Officer is responsible for monitoring the Reference and Master Data Management KPIs and raising the identified issues to Data Governance Council (where necessary) and tracking the resolution of the Reference and Master Data Management issues.
Data Owner: The data owner is accountable to establish and operationalize rules for accurate matching and merging Master Data Records from different data sources to create Golden Record. Further, the data owner is responsible the requirements for provisioning of Master Data Golden Records, requirements for provisioning of Reference Data Objects to consuming systems and applications are met adequately and providing/suggesting data quality rules to stewardship team.
Data Quality Analyst: The data quality analyst is accountable to identify and resolve the data quality issues within reference and master data. This also includes creating, implementing and execution of data quality rules and supporting the stewardship team to resolve the data quality issues related to reference and master data.
Data Architect: The Data Architect is accountable for creating and documenting the conceptual architecture for the selected Data Hub architectural design and the intended Reference and Master data environments. Creating and documenting data architecture based on the conceptual architectural design for the desired Reference and Master data environment. Further, data architect is accountable for defining the data architecture framework, standards, and principles, including modeling, metadata, security, reference data such as product codes and client categories, and master data such as clients, vendors, materials, and employees and defining data flows, i.e., which systems/applications of the  generates data, which require data to function, how data flows are managed, and how data changes in transition
GRM Team: GRM Team is responsible to Identify and support in resolution of Reference and Master Data management data quality issues.
Data Specialist: Data Specialist is responsible for raise the identified RMD issues to Data Governance Support, establish and operationalize rules for accurate matching and merging Master Data Records from different data sources to create Golden Records, requirements for provisioning of Master Data Golden Records to consuming systems and applications, requirements for provisioning of requirements for Reference Data Objects to consuming systems and applications, creating and documenting the conceptual architecture for the selected Data Hub architectural design, creating and documenting information architecture based on the conceptual architectural design

| Main Activities | The Board | EAB | DG Leadership Team | Head of data management | DG Council | Sr. Mgr. data Management & Architecture Department | MDM Team | GRM Team | Data Governance Officer | Data Quality Analyst | Data Architect | Data Owner | Data Governance Operations | Data Specialist |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main Activities | The Board | EAB | DG Leadership Team | Head of data management | DG Council | Sr. Mgr. data Management & Architecture Department | MDM Team | GRM Team | Data Governance Officer | Data Quality Analyst | Data Architect | Data Owner | Data Domain Steward | Business Domain Steward | Data Steward | Business Steward | Data Specialist |
| Implementing Reference and Master Data Hub |  | I |  | A |  | C |  | C | R | C | I |  |  |  |  |  |  |
| Monitoring Reference and Master Data KPIs |  | A | I |  | R |  | I | C | I |  | C | I |  |  |  |  |  |
| Approve the conceptual and data architectures for the desired Reference and Master data environments |  | A |  | I | A | R | C |  | R | C |  |  |  |  |  |  |  |
| Collecting and evaluating issues of the quality and management of reference and master data |  | I |  | A |  | I | R | C | R | C |  |  |  |  |  |  |  |
| Resolve the Reference and Master Data issues |  | I |  | A | R |  | I | C | R |  | C |  |  |  |  |  |  |
| Implementation of data architecture based on conceptual architecture for the desired Reference and Master Data environment |  | C | I | R |  | I |  | A , R | R | I |  |  |  |  |  |  |  |
| Monitoring the Reference and Master Data Management KPIs |  | I | A |  | R | C | R | C | I | C | I | C |  |  |  |  |  |
| Raise the identified RMD issues to Data Governance Support |  | I |  | R |  | I | C | I | C | A | C | R |  |  |  |  |  |
| Raise the identified RMD issues to Data Governance Council |  | R |  | A |  | R |  |  |  |  |  |  |  |  |  |  |  |
| Track the resolution of the Reference and Master Data Management issues. |  | I |  | R |  | A | C | R | C |  |  |  |  |  |  |  |  |
| Establish and operationalize rules for accurate matching and merging Master Data Records from different data sources to create Golden Record s |  | I |  | A |  | I | C | R | C | R |  |  |  |  |  |  |  |
| Requirements for provisioning of Master Data Golden Records to consuming systems and applications |  | C | I |  | R |  | C | R | C | I | C | I | A, R |  |  |  |  |
| Requirements for provisioning of requirements for Reference Data Objects to consuming systems and applications |  | C | I |  | R |  | C | R | C | I | C | I | A, R |  |  |  |  |
| Identify the data quality issues |  | I |  | R | C | A | C | R | C | R | C |  |  |  |  |  |  |
| Resolve the data quality issues |  | I |  | C | R | C |  | A | C | I |  |  |  |  |  |  |  |
| Creating, implementing and execution of data quality rules in DQ Tool |  | I |  | C, I | A | C | R | C | R | C |  |  |  |  |  |  |  |
| Creating and documenting the conceptual architecture for the selected Data Hub architectural design |  | I | C | I | C |  | C, I |  | A | R | C | R |  |  |  |  |  |
| Creating and documenting information architecture based on the conceptual architectural design |  | I | C | I | C |  | C, I |  | A | R | C | R |  |  |  |  |  |
| Signing off on any changes, exemptions and exceptions to Reference and Master Data Management policy |  | A | C |  | R |  | C | I | R | I |  |  |  |  |  |  |  |
| Approve Reference and Master Data approach and plan | I |  | I | A | C |  | R |  | C |  | C | I |  |  |  |  |  |
| Define Definitions and standards for Reference and Master datasets |  | I |  | I | C |  | C | A | C | R | C |  |  |  |  |  |  |
| Develop MDM and RDM implementation approach |  | I | A | C | R |  | C |  | C |  |  |  |  |  |  |  |  |

## .4. Reference and Master Data Management KPIs
It is important to measure and analyze the coverage, accuracy and efficiency of Reference and Master Data management. The following table delineates the data classification key performance indicators.

| Category | Metric | Description |
| --- | --- | --- |
| Reference / Master data Identification | Number of master datasets | Total number of datasets identified as Master Datasets |
| Reference / Master data Identification | Number of Reference datasets | Total number of datasets identified as Reference Datasets |
| Reference / Master data Profiling | % of Profiled Reference/ Master Datasets | Percentage of datasets profiled as Reference / Master Datasets |
| Reference / Master data process efficiency | Number of Reference/Master Datasets updated in past 12 months | Updates made to master and/or reference datasets in last 12 months. |
| Reference / Master data process efficiency | Number of incorrect data values in the Reference / Master Data Records | Incorrect values identified in the Reference / Master Data Records. This should be a downward trend with the passage of time |
| Reference / Master data process efficiency | Number of Data Quality Issues identified in Reference/Master Datasets | Data quality issues identified within the Reference / Master Data Records and/or datasets. This should be a downward trend with the passage of time |
| Reference / Master data process efficiency | Number of Change Requests for Reference/Master Dataset(s) | Change requests made for Reference/Master Dataset(s). This will describe the frequency of changes made within Reference/Master Dataset(s) |

| organization |  |
| --- | --- |