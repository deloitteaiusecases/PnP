---
Department: Zakat, VAT and WHT
Source_Document: ZAKAT, VAT and WHT.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name:
- **Zakat**

#### 2. Roles (Swimlanes):
- Tax Manager
- CFO
- Consultant

#### 3. Steps in Markdown Table:

| Step # | Role         | Action                                                      | Next Step/Logic                        |
|--------|--------------|-------------------------------------------------------------|----------------------------------------|
| 1      | Tax Manager  | Start                                                       | 2                                      |
| 2      | Tax Manager  | Shares documents with consultant for Zakat computation      | 3                                      |
| 3      | Consultant   | Compute Zakat based on information received                 | 4                                      |
| 4      | CFO          | Review the computation                                      | 5                                      |
| 5      | CFO          | Approve                                                     | 6 (Yes) / 3 (No)                       |
| 6      | Tax Manager  | Share information with AP and treasury team for payment     | 7                                      |
| 7      | Tax Manager  | End                                                         |                                        |

#### 4. Mermaid.js Code Block:

```mermaid
graph TD;
    A1(Start) --> A2["Shares documents with consultant for Zakat computation"];
    A2 --> B1["Compute Zakat based on information received"];
    B1 --> C1["Review the computation"];
    C1 --> D1{"Approve"};
    D1 -- Yes --> E1["Share information with AP and treasury team for processing payment"];
    E1 --> F1(End);
    D1 -- No --> B1;
```