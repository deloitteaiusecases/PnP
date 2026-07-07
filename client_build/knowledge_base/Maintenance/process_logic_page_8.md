---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 8
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name
- **Work Permit**

#### 2. Roles (Swimlanes)
- Maintenance
- Technicians
- Safety Officer
- Permit Authorizing Officer

#### 3. Steps in Markdown Table

| Step # | Role                     | Action                                                                                     | Next Step/Logic         |
|--------|--------------------------|--------------------------------------------------------------------------------------------|-------------------------|
| 1      | Maintenance              | Based on the job type, location, and risk level, confirm whether a permit is required.     | 2                       |
| 2      | Technicians              | Obtain the correct type of permit form from the permit issuing authority or SAP system.    | 3                       |
| 3      | Maintenance              | Enter details.                                                                             | 4                       |
| 4      | Maintenance              | Conduct a site inspection to confirm all controls are in place before approving the permit.| 5 (If high-risk, else 6)|
| 5      | Safety Officer           | For high-risk tasks, verify controls and sign the permit.                                  | 6                       |
| 6      | Permit Authorizing Officer | Sign the permit and authorize the start of the job.                                       | 7                       |
| 7      | Technicians              | Permit must be posted visibly at the work location until task completion.                  | 8                       |
| 8      | Maintenance              | Perform the maintenance job. Monitor safety compliance and intervene.                      | 9                       |
| 9      | Maintenance              | Clean the site, remove isolations, tools, and materials.                                   | 10                      |
| 10     | Maintenance              | Verify job completion and safe condition of equipment. Archive permit.                     | 11                      |
| 11     | Maintenance              | Maintain a record of all issued permits for traceability, audit, and learning.             | End                     |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A1[Start] --> B1[1. Confirm permit requirement] --> B2[2. Obtain permit form] --> B3[3. Enter details] --> B4[4. Conduct site inspection]
    B4 -->|If high-risk| B5[5. Safety Officer verifies]
    B5 --> B6[6. Authorize start]
    B4 -->|Not high-risk| B6
    B6 --> B7[7. Post permit at site] --> B8[8. Perform maintenance job] --> B9[9. Clean site]
    B9 --> B10[10. Verify completion] --> B11[11. Maintain records] --> C1[End]
```
