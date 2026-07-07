---
Department: Data Quality
Section: Data Quality Dimensions
Section_Kind: core
Section_Priority: normal
Source: 8__Data_Architecture_and_Modelling___13_.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 0
---

## Data Quality Dimensions

Data Quality dimensions are measurable features or characteristics of data, which are used to define results of initial data quality assessment as well as ongoing measurements. To measure the quality of data,  needs to establish characteristics that are both important to its business processes (worth measuring) and measurable.
While considering data quality at , below defined best practice core dimensions of data quality, which can be measured or assessed against defined standards, are to be followed.

| Data quality D imension | Definition | Data Example for [client] |
| --- | --- | --- |
| Completeness | • Data completeness refers to whether the data required to meet the business information demand are available.<br>• Completeness can be measures at the data set, record, or column level. Data can be complete even if optional data is missing, as long as the data meets the expectations. | Completeness of Customer Identification data ( Customer Name and Customer ID Number ) for all on-boarded customers |
| Uniqueness | **Uniqueness states that no entry exists more than once within the same data set**<br>• Asserting uniqueness of entities within a data set implies that a key value relates to each unique entity/individual, and only to that specific entity/individual, within the dataset | Customer Identification data ( Customer Name and Customer ID Number ) is a unique data, two different Names/ID numbers of same customer cannot exist |
| Timeliness | Degree to which data is current and available for use in the expected time frame | Timeliness of Customer’s Address change data implies updating the address change in the database within the stipulated time period (For example, SLA of 7 days) |
| Validity | • The conformity of data to the standards and syntax. Data is valid if it conforms to the syntax (format, type, range) of its definition<br>• It is the level of data matching a reference | As the VAT Registration number is a 15-digit number, a VAT Registration number with <15 or >15 digits in the database will be invalid (data level validity) |
| Accuracy | • The degree to which data correctly describes the "real world" object or the event being described<br>• For a data to be accurate, values must be valid, and in the correct representation | • While loading Credit Card Bill Issue Date , the format followed by data provider needs to match with the format followed in the organization data platform(s).<br>• Entering US date formatted data (MM/DD/YYYY) to European date formatted (DD/MM/YYYY) database will cause the reversed representation of day and month |
| Consistency | • Consistency is the absence of difference, when comparing multiple (two or more) representations of same data<br>• Data elements having reliably the same definition and meaning across all data sources | The Street Address data of a particular Vendor is same across all the data sources without conflicting information. |

Table 1: Data Quality Dimensions/Criteria