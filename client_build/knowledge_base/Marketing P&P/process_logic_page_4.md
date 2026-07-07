---
Department: Marketing P&P
Source_Document: Marketing P&P.pdf
Page_Number: 4
Last_Updated: 2026-03-16
---

### Analysis of Trade Marketing Activities Flowchart

1. **Process Name**: Trade Marketing Activities

2. **Identified Roles (Swimlanes)**:
   - Key Accounts Manager
   - B2C Director
   - Trade Marketing Manager
   - Customer

3. **Steps in Markdown Table**:

| Step # | Role                  | Action                                                                                                                   | Next Step/Logic                                          |
|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 1      | Key Accounts Manager  | Receives draft Agreement/Promotion Proposal from the Modern Trade/Key Accounts customer (M)                               | Step 2                                                   |
| 2      | B2C Director          | Shares the draft agreement with recommendations to Trade Marketing Manager for review. (M)                               | Step 3                                                   |
| 3      | Trade Marketing Manager | Review the draft agreements/proposal in meeting to discuss both departments’ recommendations. (M)                     | Step 4                                                   |
| 4      | Trade Marketing Manager | Negotiate draft agreement/Proposal with the customer. Revised draft agreement/proposal is submitted to Head of Marketing and Head of Sales for approval. (M) | Step 5                                                   |
| 5      | Trade Marketing Manager | In case of Agreement, submit draft agreement to Legal and then to CFO for approval. In case of proposal, submit proposal to CFO for approval. (M) | Step 6                                                   |
| 6      | Trade Marketing Manager | Share approved draft agreement to customer for further process. (M)                                                     | Step 7                                                   |
| 7      | Customer              | Submits official signed agreement along with required documentations for official agreement execution. (M)               | End                                                     |

4. **Logic as Mermaid.js Code Block**:

```mermaid
graph TD;
    A[Start] --> B[Receives draft Agreement/Promotion Proposal from the Modern Trade/Key Accounts customer (M)]
    B --> C[Shares the draft agreement with recommendations to Trade Marketing Manager for review. (M)]
    C --> D[Review the draft agreements/proposal in meeting to discuss both departments’ recommendations. (M)]
    D --> E[Negotiate draft agreement/Proposal with the customer. Revised draft agreement/proposal is submitted to Head of Marketing and Head of Sales for approval. (M)]
    E --> F[In case of Agreement, submit draft agreement to Legal and then to CFO for approval. In case of proposal, submit proposal to CFO for approval. (M)]
    F --> G[Share approved draft agreement to customer for further process. (M)]
    G --> H[Submits official signed agreement along with required documentations for official agreement execution. (M)]
    H --> I[End]
```