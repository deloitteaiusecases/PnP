---
Department: Cash Management
Source_Document: Cash Management.pdf
Page_Number: 12
Last_Updated: 2026-03-16
---

### 1. Process Name
- Balance Confirmation

### 2. Roles (Swimlanes)
- Accounting Unit Head
- Treasury Manager, GL Manager, and Accounting Manager

### 3. Steps in Markdown Table

| Step # | Role                                        | Action                                                                      | Next Step/Logic                   |
|--------|---------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------|
| 1      | Accounting Unit Head                        | On a quarterly basis, balances are confirmed and reconciled with the GL balance (M) | Step 2                            |
| 2      | Treasury Manager, GL Manager, and Accounting Manager | Keep informed Treasury Manager, GL Manager, and Accounting Manager (M)                      | End                               |

### 4. Logic in Mermaid.js Code Block

```mermaid
graph TD;
    A(Start) --> B[On quarterly basis, balances are confirmed and reconciled with the GL balance (M)];
    B --> C[Keep informed Treasury Manager, GL Manager, and Accounting Manager (M)];
    C --> D(End);
```
