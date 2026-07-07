---
Department: Accounting Policies and Procedures
Section: RELATED PARTY TRANSACTIONS
Section_Kind: core
Section_Priority: normal
Source: Accounting Principles and procedures.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## RELATED PARTY TRANSACTIONS

Overview
Related party transactions involve sale of good and services between Arabian Mills and its related parties. These transactions are disclosed in the financial statements to ensure transparency and compliance with regulatory requirements.
Policy
In accordance with IAS 24 - Related Party Disclosures, Arabian Mills discloses relationships and transactions with related parties that could influence the financial position and performance of the Company. Related parties include individuals or entities with control, joint control, or significant influence over the entity, as well as key management personnel and their close family members.
 Identification and Validation: Related parties are identified by the Legal Department, including entities under control, key management personnel, and their close family members. The list of related parties is validated by accounting department to ensure compliance with IAS 24.
 Disclosure Requirements: Disclosures must include:
  o The nature of the relationship with the related party.
  o Transaction amounts with related parties.
  o Any outstanding balances with related parties.
  o Compensation of key management personnel, categorised and disclosed.
 Review and Approval: The nature of transactions with related parties is reviewed by the Legal Department and the CEO. All related party transactions are approved by the Board annually to ensure that they are planned and authorised in advance.
 Transaction with related party must be at arms-length price.
Procedure
The following accounting procedures shall be followed:

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | **Identification of related parties**<br>• The first step in accounting for related party transactions is the identification of related parties. Related parties include entities that control or are controlled by the reporting entity, entities under common control, key management personnel, and close family members of key management personnel. The legal team identifies the list of related parties, which the Accounting Manager validates as per IFRS and the CFO approves. | **Preparer: Legal department**<br>• Reviewer: Accounting Manager<br>• Approver – CF O | Frequency: In case of identification of new related party |
| 2 | **Transaction with related parties**<br>• The Legal Department and CEO review the nature of transactions to be conducted with related parties, and the Board approves them at the beginning of the year. This ensures that all transactions are planned and authorised in advance, maintaining transparency and compliance with corporate governance standards. | **Approver – Legal Department and CEO**<br>• Approver Board | Frequency: Annual |
| 3 | **Documentation of Transactions**<br>• The next step is to document all transactions with these parties. This documentation includes the nature of the transaction, the amount involved, the terms and conditions, and any other relevant details. Proper documentation is essential for transparency and for providing evidence that the transactions are conducted at arm's length. The AR Manager documents these transactions on a monthly basis, which the Accounting Manager and CFO validate. | **Preparer: AR Manager**<br>• Reviewer: Accounting Manager , CFO | Frequency: Monthly |
| 4 | **Disclosure in Financial Statements**<br>• The final step is to disclose related party transactions in the financial statements. The disclosure includes details such as the nature of the relationship, the types of transactions, the amounts involved, and any outstanding balances. Proper disclosure helps maintain the integrity of the financial statements and ensures compliance with regulatory requirements. The AR Manager prepares the disclosures, and the Accounting Manager reviews them. | **Preparer: AR Manager**<br>• Reviewer: Accounting Manager | Frequency: Quarterly |

Flow Chart

**[Diagram — Visio-EMF→PNG]:**

Process Name: Related Party  

Roles / Swimlanes:
- Accounting Manager
- CFO
- AR Manager

### Steps

| Step # | Role              | Action                                                                 | Decision/Next Step                                                                                      |
|--------|-------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 1      | Accounting Manager | Start                                                                  | Proceed to Step 2                                                                                       |
| 2      | Accounting Manager | Obtain list of related part from legal department (M)                 | Proceed to Step 3                                                                                       |
| 3      | Accounting Manager | Validates the listing as per IAS 24 (M)                               | Proceed to Step 4                                                                                       |
| 4      | CFO               | Approve (decision point)                                              | If **Yes** → Step 5. If **No** → return to Step 3 (Validates the listing as per IAS 24 (M)).           |
| 5      | AR Manager        | Documents transactions and disclosure of related party (M)            | Proceed to Step 6                                                                                       |
| 6      | CFO               | Review the transactions and disclosures (M)                           | Proceed to Step 7                                                                                       |
| 7      | CFO               | End                                                                    | Process ends                                                                                            |

Yes/No branches explicitly:

- From **Approve** (Step 4):
  - **Yes** → Documents transactions and disclosure of related party (M) (Step 5)
  - **No** → Validates the listing as per IAS 24 (M) (Step 3)

### Mermaid.js Flow

```mermaid
graph TD

  subgraph Accounting_Manager
    A1[Start]
    A2[Obtain list of related part from legal department (M)]
    A3[Validates the listing as per IAS 24 (M)]
  end

  subgraph CFO
    C1{Approve}
    C2[Review the transactions and disclosures (M)]
    E[End]
  end

  subgraph AR_Manager
    R1[Documents transactions and disclosure of related party (M)]
  end

  A1 --> A2 --> A3 --> C1
  C1 -- Yes --> R1
  C1 -- No --> A3
  R1 --> C2
  C2 --> E
```