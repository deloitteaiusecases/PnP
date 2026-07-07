---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 8
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: Finished Product Quality

2. **Roles (Swimlanes)**:
   - **QA Analyst / Data Entry Operator**

3. **Steps in Markdown Table**:

| Step # | Role                        | Action                                                                 | Next Step/Logic               |
|--------|-----------------------------|------------------------------------------------------------------------|-------------------------------|
| 1      | A                           | Mixer finishes blend cycle; batch is transferred to holding bin.       | 2                             |
| 2      | M                           | QA draws samples for uniformity testing.                               | 3                             |
| 3      | A                           | Lab/NIR testing conducted.                                             | 3.1                           |
| 3.1    | M                           | Is CV% within acceptable range?                                        | Yes: 4 / No: 3.1.1            |
| 3.1.1  | M                           | Re-mix and Retest                                                      | 2                             |
| 4      | M                           | QA tests moisture and Pellet Durability Index.                         | 6                             |
| 5      | A                           | Monthly or risk-based testing.                                         | 6                             |
| 6      | M                           | Inspect pack integrity, seal strength, label accuracy, barcode, net weight. | 7                         |
| 7      | M                           | Are all Quality Parameters Within Spec?                                | Yes: 8 / No: 9                |
| 8      | M                           | Record results in SAP Quality Lot; Release batch.                      | End                           |
| 9      | M                           | Batch is blocked in SAP; RCA initiated; CAPA implemented.              | 10                            |
| 10     | M                           | Can batch be reprocessed?                                              | Yes: 10.1 / No: 10.2          |
| 10.1   | M                           | Rework under QA supervision                                            | 2                             |
| 10.2   | M                           | Dispose batch per waste SOP; document in SAP.                          | End                           |

4. **Mermaid.js Code Block**:

```mermaid
graph TD
    Start --> A1["1. Mixer finishes blend cycle; batch is transferred to holding bin."]
    A1 --> M2["2. QA draws samples for uniformity testing."]
    M2 --> A3["3. Lab/NIR testing conducted."]
    A3 --> M3["3.1 Is CV% within acceptable range?"]
    M3 -->|Yes| M4["4. QA tests moisture and PDI."]
    M3 -->|No| M3.1["3.1.1 Re-mix and Retest"]
    M3.1 --> M2
    M4 --> M6["6. Inspect pack attributes."]
    A5["5. Monthly or risk-based testing."] --> M6
    M6 --> M7["7. Are all Quality Parameters Within Spec?"]
    M7 -->|Yes| M8["8. Record results in SAP Quality Lot; Release batch."]
    M7 -->|No| M9["9. Batch is blocked in SAP; RCA initiated; CAPA implemented."]
    M9 --> M10["10. Can batch be reprocessed?"]
    M10 -->|Yes| M10.1["10.1 Rework under QA supervision"]
    M10.1 --> M2
    M10 -->|No| M10.2["10.2 Dispose batch per waste SOP; document in SAP."]
    M8 --> End
    M10.2 --> End
```

This outlines the flowchart's steps and decision points clearly for analysis and communication within the organization.