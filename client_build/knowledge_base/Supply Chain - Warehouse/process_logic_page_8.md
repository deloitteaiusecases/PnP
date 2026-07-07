---
Department: Supply Chain - Warehouse
Source_Document: Supply Chain - Warehouse.pdf
Page_Number: 8
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

1. **Process Name**: Warehouse Archive File Management

2. **Roles (Swimlanes)**:
   - DC Officer / WH Head
   - Warehouse Section Head
   - Warehouse Manager
   - HQ Warehouse Manager

3. **Steps Table**:

| Step # | Role                     | Action                                                                                      | Next Step/Logic                             |
|--------|--------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------|
| 1      | DC Officer / WH Head     | Start                                                                                       | 2                                           |
| 2      | DC Officer / WH Head     | Master List of File Categories                                                              | 3                                           |
| 3      | DC Officer / WH Head     | Label files using the approved format. Print and attach label. File documents in date order. | 4                                           |
| 4      | DC Officer / WH Head     | Maintain a File Index Register. Excel-Based or Manual File Logbook.                         | 5                                           |
| 5      | DC Officer / WH Head     | Arrange physical files in designated shelves or rooms according to department, year, and file type. | 6                                           |
| 6      | DC Officer / WH Head     | Scan critical documents and save digital copies in official shared drive with same label code. | 7                                           |
| 7      | Warehouse Section Head   | Conduct weekly reviews of new and existing files to ensure proper labelling, order, and completeness. | 8                                           |
| 8      | Warehouse Manager        | Disposal List and Approval Sheet                                                            | 9                                           |
| 9      | HQ Warehouse Manager     | Destruction Certificate + File Audit Record                                                 | End                                         |
| End    | HQ Warehouse Manager     | End                                                                                         |                                             |

4. **Mermaid.js Code Block**:

```mermaid
graph TD

A1[Start] --> B1[Master List of File Categories]
B1 --> C1[Label files using the approved format. Print and attach label. File documents in date order.]
C1 --> D1[Maintain a File Index Register. Excel-Based or Manual File Logbook.]
D1 --> E1[Arrange physical files in designated shelves or rooms according to department, year, and file type.]
E1 --> F1[Scan critical documents and save digital copies in official shared drive with same label code.]
F1 --> G1[Conduct weekly reviews of new and existing files to ensure proper labelling, order, and completeness.]
G1 --> H1[Disposal List and Approval Sheet]
H1 --> I1[Destruction Certificate + File Audit Record]
I1 --> J1[End]

classDef startEnd fill:#f96,stroke:#333,stroke-width:2px;
classDef process fill:#bbf,stroke:#333,stroke-width:2px;
classDef decision fill:#fff,stroke:#333,stroke-width:2px;

A1:::startEnd
J1:::startEnd
```