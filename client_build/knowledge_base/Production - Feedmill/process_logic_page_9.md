---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### Analysis

#### Process Name:
- Storage and Inventory Management of Finished Feed

#### Roles:
- Store Division Head
- QA Analyst 
- Data Entry Operator

#### Markdown Table

| Step # | Role                       | Action                                                                                     | Next Step/Logic               |
|--------|----------------------------|--------------------------------------------------------------------------------------------|-------------------------------|
| 1      | Store Division Head        | Batches of finished feed are transferred to the warehouse with accompanying batch documentation. | Step 2                        |
| 2      | QA Analyst                 | Verify packaging integrity, labeling, and batch documentation.                             | Step 2.1                      |
| 2.1    | QA Analyst                 | Any signs of damage or missing info?                                                        | Yes: Step 2.2, No: Step 3     |
| 2.2    | QA Analyst                 | Move batch to HOLD area and notify QA.                                                      | End                           |
| 3      | QA Analyst                 | Place product in designated storage area based on batch code and SAP bin mapping.           | Step 4                        |
| 4      | QA Analyst                 | Update batch location and status in SAP (e.g., "Released for Sale", "Hold").                | Step 5                        |
| 5      | QA Analyst                 | Run SAP alerts for near-expiry or overage stock.                                            | Step 5.1                      |
| 5.1    | QA Analyst                 | Any items within 60 days of expiry or misallocated?                                         | Yes: Step 5.2, No: Step 6     |
| 5.2    | QA Analyst                 | Tag, report to QA and Planning; initiate further action (disposal, revalidation).           | End                           |
| 6      | Data Entry Operator        | Only released stock to be picked as per dispatch schedule.                                  | Step 6.1                      |
| 6.1    | Data Entry Operator        | Does physical match SAP & QA status?                                                       | Yes: Step 6.2, No: Step 6.3   |
| 6.2    | Data Entry Operator        | Load verified stock to outbound vehicle with documentation.                                | Step 7                        |
| 6.3    | Data Entry Operator        | Stop loading. Reconcile SAP vs physical. Escalate to Inventory Supervisor.                 | End                           |
| 7      | QA Analyst / Data Entry Operator | Monitor temperature, humidity, and housekeeping.                                           | Step 8                        |
| 8      | QA Analyst / Data Entry Operator | Audit bin cards and SAP entries; resolve variances.                                        | End                           |

#### Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1["1. Batches of finished feed are transferred to the warehouse with accompanying batch documentation. (A)"]
    A1 --> A2["2. Verify packaging integrity, labeling, and batch documentation. (M)"]
    A2 --> B2{"2.1 Any signs of damage or missing info?"}
    B2 -- Yes --> A3["2.2 Move batch to HOLD area and notify QA. (M)"]
    B2 -- No --> A4["3. Place product in designated storage area based on batch code and SAP bin mapping. (M)"]
    A3 --> End
    A4 --> A5["4. Update batch location and status in SAP (e.g., 'Released for Sale', 'Hold'). (M)"]
    A5 --> A6["5. Run SAP alerts for near-expiry or overage stock. (M)"]
    A6 --> B5{"5.1 Any items within 60 days of expiry or misallocated?"}
    B5 -- Yes --> A7["5.2 Tag, report to QA and Planning; initiate further action (disposal, revalidation). (M)"]
    B5 -- No --> A8["6. Only released stock to be picked as per dispatch schedule. (M)"]
    A7 --> End
    A8 --> B6{"6.1 Does physical match SAP & QA status?"}
    B6 -- Yes --> A9["6.2 Load verified stock to outbound vehicle with documentation. (M)"]
    B6 -- No --> A10["6.3 Stop loading. Reconcile SAP vs physical. Escalate to Inventory Supervisor. (M)"]
    A10 --> End
    A9 --> B7["7. Monitor temperature, humidity, and housekeeping. (M)"]
    B7 --> B8["8. Audit bin cards and SAP entries; resolve variances. (M)"]
    B8 --> End
```