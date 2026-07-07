---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 35
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name:**
   - Process Waste Management

2. **Roles (Swimlanes):**
   - Production Supervisor
   - Waste Handling Team
   - Facilities Manager
   - QA Specialist

3. **Steps in Markdown Table:**

   | Step # | Role                | Action                                                                                 | Next Step/Logic                                      |
   |--------|---------------------|----------------------------------------------------------------------------------------|------------------------------------------------------|
   | 1      | Production Supervisor | Ensure waste is correctly identified and segregated by type. Labelled containers used at source. | Step 2                                                 |
   | 2      | Production Supervisor | Waste stored in closed containers. Quickly removed from production zones. Moved to designated waste storage. | Step 3                                                 |
   | 3      | Waste Handling Team | Waste removed on set frequencies. Removal records maintained.                          | Step 4                                                 |
   | 4      | Facilities Manager  | Only approved contractors used. Disposal documented with permits, receipts.            | Step 5                                                 |
   | 5      | Facilities Manager  | Used lubricants, filters, parts managed separately. Disposal via licensed contractors. | End                                                    |
   | 6      | QA Specialist       | Pest residues (dead pests, bait waste) disposed separately.                            | End                                                    |

4. **Logic in Mermaid.js Code Block:**

```mermaid
graph TD;
    A[Start] --> B[Ensure waste is correctly identified and segregated by type. Labelled containers used at source];
    B --> C[Waste stored in closed containers. Quickly removed from production zones. Moved to designated waste storage];
    C --> D[Waste removed on set frequencies. Removal records maintained];
    D --> E[Only approved contractors used. Disposal documented with permits, receipts];
    E --> F[Used lubricants, filters, parts managed separately. Disposal via licensed contractors];
    E --> G[Pest residues (dead pests, bait waste) disposed separately];
    F --> H[End];
    G --> H[End];
```

This breakdown provides a clear understanding of each step within the process along with the roles responsible for each action.