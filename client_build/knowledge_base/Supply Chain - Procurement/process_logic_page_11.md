---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 11
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Supplier Qualification

2. **Roles (Swimlanes)**:
   - Existing & New Supplier
   - Procurement Officer
   - Procurement Manager/SC Director
   - COO
   - CFO/CEO

3. **Steps in a Markdown Table**:

   | Step # | Role                         | Action                                   | Next Step/Logic          |
   |--------|------------------------------|------------------------------------------|--------------------------|
   | 1      | Procurement Officer          | Start                                    | Step 2                   |
   | 2      | Procurement Officer          | Advertisement                            | Step 3                   |
   | 3      | Existing & New Supplier      | Invitation Letter and Application        | Step 4                   |
   | 4      | Procurement Officer          | Evaluation Document                      | Step 5                   |
   | 5      | Procurement Manager/SC Director | Evaluation Report                      | Step 6                   |
   | 6      | Procurement Manager/SC Director | Submitted Prospective Supplier List    | Step 7                   |
   | 7      | COO                          | Approved? No                            | Step 2                   |
   | 7      | COO                          | Approved? Yes                           | Step 8                   |
   | 8      | CFO/CEO                      | Approved? No                            | Step 2                   |
   | 8      | CFO/CEO                      | Approved? Yes                           | Step 9                   |
   | 9      | Procurement Manager/SC Director | Approved Prospective Supplier List   | Step 10                  |
   | 10     | Procurement Officer          | End                                      | -                        |

4. **Logic as Mermaid.js Code Block**:

   ```mermaid
   graph TD;
       A1(Start) --> A2[Advertisement]
       A2 --> B1[Invitation Letter and Application]
       B1 --> A3[Evaluation Document]
       A3 --> C1[Evaluation Report]
       C1 --> C2[Submitted Prospective Supplier List]
       C2 --> D1{Approved?}
       D1 -- No --> A2
       D1 -- Yes --> E1{Approved?}
       E1 -- No --> A2
       E1 -- Yes --> C3[Approved Prospective Supplier List]
       C3 --> A4(End)
   ```
