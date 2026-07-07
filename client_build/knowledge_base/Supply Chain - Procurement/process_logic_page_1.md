---
Department: Supply Chain - Procurement
Source_Document: Supply Chain - Procurement.pdf
Page_Number: 1
Last_Updated: 2026-03-16
---

Certainly! Let's analyze the flowchart.

### 1. Process Name
- **Procurement Planning Flowchart**

### 2. Roles (Swimlanes)
- Procurement Manager
- SC Director
- COO
- CFO
- CEO

### 3. Steps as a Markdown Table

| Step # | Role              | Action                        | Next Step/Logic                                      |
|--------|-------------------|-------------------------------|------------------------------------------------------|
| 1      | Procurement Manager | Start                         | 2                                                    |
| 2      | Procurement Manager | Yearly Procurement Plan       | 3                                                    |
| 3      | SC Director       | Approved?                     | Yes: 4, No: 2 (Revision)                             |
| 4      | COO               | Approved?                     | Yes: 5, No: 2 (Revision)                             |
| 5      | CFO               | Approved?                     | Yes: 6, No: 2 (Revision)                             |
| 6      | CEO               | Approved?                     | Yes: 7, No: 2 (Revision)                             |
| 7      | Procurement Manager | Procurement Plan Issuance     | 8                                                    |
| 8      | Procurement Manager | End                           |                                                      |

### 4. Logic as Mermaid.js Code Block

```mermaid
graph TD
    A1[Start] --> B1[Yearly Procurement Plan]
    B1 --> C1{SC Director Approved?}
    C1 -- Yes --> D1{COO Approved?}
    C1 -- No --> B1
    
    D1 -- Yes --> E1{CFO Approved?}
    D1 -- No --> B1

    E1 -- Yes --> F1{CEO Approved?}
    E1 -- No --> B1
    
    F1 -- Yes --> G1[Procurement Plan Issuance]
    F1 -- No --> B1
    
    G1 --> H1[End]
```

This structure represents the steps and decision paths in the procurement planning flowchart.