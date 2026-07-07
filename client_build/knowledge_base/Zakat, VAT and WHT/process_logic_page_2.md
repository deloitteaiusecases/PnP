---
Department: Zakat, VAT and WHT
Source_Document: ZAKAT, VAT and WHT.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: VAT

2. **Roles (Swimlanes)**:
   - Tax Manager
   - CFO
   - Consultant

3. **Steps in a Markdown Table**:

   | Step # | Role        | Action                                                       | Next Step/Logic                |
   |--------|-------------|--------------------------------------------------------------|--------------------------------|
   | 1      | Tax Manager | Start                                                        | Step 2                         |
   | 2      | Tax Manager | Shares information with consultant for VAT filing            | Step 3                         |
   | 3      | Consultant  | VAT Filing and reconciliation                                | Step 4                         |
   | 4      | Tax Manager | Review the filing and reconciliation                         | Step 5                         |
   | 5      | CFO         | Approve                                                      | Yes: Step 6, No: Step 3        |
   | 6      | Tax Manager | Share information with AP and treasury team for payment, if any | Step 7                         |
   | 7      | Tax Manager | End                                                          |                                |

4. **Logic in Mermaid.js Code Block**:

   ```mermaid
   graph TD;
       A1(Start) --> A2;
       A2(Shares information with consultant for VAT filing) --> A3;
       A3(VAT Filing and reconciliation) --> A4;
       A4(Review the filing and reconciliation) --> A5;
       A5{Approve}
       A5 -- Yes --> A6;
       A5 -- No --> A3;
       A6(Share information with AP and treasury team for payment, if any) --> A7;
       A7(End);
   ```

This flowchart represents the process for VAT filing, indicating decision making and information flow across different roles.