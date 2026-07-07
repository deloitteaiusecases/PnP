---
Department: IT
Source_Document: IT.pdf
Page_Number: 14
Last_Updated: 2026-03-16
---

### Analysis of IT Asset Audit Procedure Flowchart

#### 1. Process Name
- **IT Asset Audit Procedure**

#### 2. Roles (Swimlanes)
- Internal Audit
- IT Network and Server Admin
- IT & Cybersecurity Manager
- Senior Management

#### 3. Steps in Markdown Table

| Step # | Role                         | Action                                                                                             | Next Step/Logic            |
|--------|------------------------------|----------------------------------------------------------------------------------------------------|----------------------------|
| 1      | Internal Audit               | Develop an audit plan outlining the scope, objectives, and schedule for periodic audits of IT assets.| Step 2                     |
| 2      | Internal Audit               | Conduct physical and logical audits of IT assets, comparing the actual state of assets with the inventory records.| Step 3                     |
| 3      | Internal Audit               | Identify any discrepancies between the actual state of assets and inventory records, including unauthorized changes, missing assets, or incorrect information.| Step 4 (if discrepancies)  |
| 4      | IT Network and Server Admin  | Investigate and resolve identified discrepancies, updating inventory records as necessary.         | Step 5                     |
| 4      | IT & Cybersecurity Manager   | Investigate and resolve identified discrepancies, updating inventory records as necessary.         | Step 5                     |
| 5      | Internal Audit               | Prepare and submit audit reports detailing findings, resolutions, and recommendations for improving asset management practices. | Step 6                    |
| 6      | Senior Management            | Review audit reports with senior management to ensure awareness and support for necessary changes and improvements. | End               |

#### 4. Logic in Mermaid.js Code Block

```mermaid
graph TD;
    Start --> A1;
    A1[Develop audit plan] --> A2;
    A2[Conduct audits] --> A3;
    A3[Identify discrepancies] -->|Yes| A4;
    A3 -->|No| A5;
    A4[Investigate and resolve discrepancies (Admin/Manager)] --> A5;
    A5[Prepare and submit audit reports] --> A6;
    A6[Review audit reports with senior management] --> End;
```
