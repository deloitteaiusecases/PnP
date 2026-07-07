---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 9
Last_Updated: 2026-03-16
---

### Analysis

**1. Process Name:**
   - Accrual Management – PO based approvals

**2. Roles (Swimlanes):**
   - GL Manager
   - Supply Chain Team
   - Accounting Manager

**3. Steps in a Markdown Table:**

| Step # | Role                | Action                                                                                          | Next Step/Logic                                             |
|--------|---------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1      | GL Manager          | Send a monthly email to the procurement team to request list of POs which are still under approval stage. | Step 2                                                      |
| 2      | Supply Chain Team   | Provide the list of POs which are under approval stage via email.                               | Step 3                                                      |
| 3      | GL Manager          | Validate the list of POs and upload the working on SAP and parks the accrual entry in the system. | Step 4                                                      |
| 4      | GL Manager          | Check if POs are approved.                                                                     | Yes: Step 5 <br>No: Back to Step 3                          |
| 5      | GL Manager          | Reverse the accruals booked against approved POs and ensures they are recorded under GR/IR for the current month. | Step 6                                                      |
| 6      | Accounting Manager  | Review and Approve                                                                              | End                                                         |

**4. Mermaid.js Code Block:**

```mermaid
graph TD
    A1(Start) --> A2[Send a monthly email to request list of POs]
    A2 --> B1[Provide the list of POs via email]
    B1 --> A3[Validate the list of POs]
    A3 --> D1{Are POs approved?}
    D1 -- Yes --> A4[Reverse accruals and record under GR/IR]
    D1 -- No --> A3
    A4 --> C1[Review and Approve]
    C1 --> E1(End)
```
