---
Department: AP and Accruals
Source_Document: AP and Accruals.pdf
Page_Number: 2
Last_Updated: 2026-03-16
---

Certainly! Here's the analysis of the flowchart:

### 1. Process Name
- **NON - PO based invoice processing and payment**

### 2. Roles (Swimlanes)
- Procurement Team
- AP Accountant
- AP Unit Head
- Accounting Manager / GL Manager

### 3. Steps in a Markdown Table

| Step # | Role                        | Action                                                                                      | Next Step/Logic                       |
|--------|-----------------------------|---------------------------------------------------------------------------------------------|---------------------------------------|
| 1      | Procurement Team            | Receipt of invoice and sharing documents with AP Team (M)                                   | Step 2                                |
| 2      | AP Accountant               | Recording of Invoice (Recognition of liability) – non - PO based (SADAD or payable to government) (M) | Step 3                                |
| 3      | AP Unit Head                | Review the entry and documentation. (A)                                                     | If approved, Step 5; else Step 4      |
| 4      | AP Accountant               | Provide the missing info/documents (A)                                                      | Step 3                                |
| 5      | Accounting Manager / GL Manager | Post the entry in SAP (A)                                                                 | End                                   |

### 4. Logic as a Mermaid.js Code Block

```mermaid
graph TD;
    A[Start] --> B[Receipt of invoice and sharing documents with AP Team (M)]
    B --> C[Recording of Invoice (Recognition of liability) – non - PO based (M)]
    C --> D[Review the entry and documentation. (A)]
    D -->|No| E[Provide the missing info/documents (A)]
    E --> D
    D -->|Yes| F{Approved?}
    F -->|Yes| G[Post the entry in SAP (A)]
    G --> H[End]
    F -->|No| E
```

This code and table structure models the process flow as depicted in the flowchart image.