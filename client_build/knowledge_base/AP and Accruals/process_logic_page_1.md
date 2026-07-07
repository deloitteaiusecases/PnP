---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**
   - PO based invoice processing and payment

2. **Roles (Swimlanes)**
   - Supply Chain Team
   - Procurement Team
   - AP Accountant
   - AP Unit Head
   - Accounting Manager/GL Manager

3. **Steps Table**

| Step # | Role                     | Action                                                                                | Next Step/Logic         |
|--------|--------------------------|---------------------------------------------------------------------------------------|-------------------------|
| 1      | Supply Chain Team        | Start                                                                                 | Generation of PO        |
| 2      | Supply Chain Team        | Generation of PO                                                                      | Receipt of goods/services |
| 3      | Supply Chain Team        | Receipt of goods/services (system generated entry for GR/IR)                          | Step 4                  |
| 4      | Procurement Team         | Receipt of invoice on dedicated email ID and sharing all approved documents with AP Team | Step 5                  |
| 5      | AP Accountant            | Recording of Invoice (Recognition of liability) – PO based                           | Step 6                  |
| 6      | AP Unit Head             | Review the entry and documentation                                                   | Approved? (Decision)    |
| 7      | AP Accountant            | Provide the missing info/documents (if No)                                           | Step 6                  |
| 8      | Accounting Manager/GL Manager | Approved? (Decision)                                                        | Step 9 if Yes, Step 7 if No |
| 9      | AP Accountant            | The entry gets posted in SAP once approved                                           | End                     |

4. **Mermaid.js Code Block**

```mermaid
graph TD
    A1(Start) --> A2[Generation of PO]
    A2 --> A3[Receipt of goods/services (system generated entry for GR/IR)]
    A3 --> B1[Receipt of invoice on dedicated email ID and sharing all approved documents with AP Team]
    B1 --> C1[Recording of Invoice (Recognition of liability) – PO based]
    C1 --> D1[Review the entry and documentation]
    D1 -->|No| C3[Provide the missing info/documents]
    C3 --> D1
    D1 -->|Yes| E1{Approved?}
    E1 -->|No| C3
    E1 -->|Yes| F1[The entry gets posted in SAP once approved]
    F1 --> End[End]
```

This structure captures the process flow visually, step-by-step, in both a table and flow diagram format.