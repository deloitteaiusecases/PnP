---
Department: Revenue flow chart
Source_Document: Revenue flow chart.pdf
Page_Number: 3
Last_Updated: 2026-03-16
---

### 1. Process Name:
AR Ageing

### 2. Roles (Swimlanes):
- AR Team
- Accounting Manager
- CFO

### 3. Steps in Markdown Table:

| Step # | Role              | Action                                                              | Next Step      |
|--------|-------------------|---------------------------------------------------------------------|----------------|
| 1      | AR Team           | Extract auto generated AR Ageing report from SAP (M)                | Step 2         |
| 2      | Accounting Manager| Review ageing report and approve listing of customers for follow-up purpose (M) | Step 3         |
| 3      | CFO               | Final review (M)                                                    | End            |

### 4. Logic in Mermaid.js Code Block:

```mermaid
graph TD;
    A[Start] --> B[Extract auto generated AR Ageing report from SAP (M)];
    B --> C[Review ageing report and approve listing of customers for follow-up purpose (M)];
    C --> D[Final review (M)];
    D --> E[End];
```
