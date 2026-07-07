---
Department: IT
Source_Document: IT.pdf
Page_Number: 11
Last_Updated: 2026-03-16
---

Sure, let's analyze the flowchart.

### 1. Process Name
- Asset Inventory Procedure

### 2. Roles (Swimlanes)
- IT Network and Server Administrator
- IT & Cybersecurity Manager

### 3. Steps in a Markdown Table

| Step # | Role                            | Action                                                                                                            | Next Step/Logic                |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------|
| 1      | IT Network and Server Administrator | List all devices under the custody of the IT department (A/M)                                                          | Step 2                         |
| 2      | IT Network and Server Administrator | List all applications and licensed software installed on production servers and desktops/laptops (A/M)              | Step 3                         |
| 3      | IT Network and Server Administrator | Fill the server & network device request form for all new server and network device requests (M)                      | Decision: Approved?            |
| Decision | IT & Cybersecurity Manager         | Approved?                                                                                                          | Yes: Step 5 <br> No: Step 4    |
| 4      | IT Network and Server Administrator | Fill the server & network device request form for all new server and network device requests (M) again if not approved | Back to Decision               |
| 5      | IT Network and Server Administrator | Update asset inventory file for any asset removed, disposed, or newly purchased (M)                                 | Step 7                         |
| 6      | IT Network and Server Administrator | Update asset inventory file for any asset removed, disposed, or newly purchased (M)                                 | Step 7                         |
| 7      | IT Network and Server Administrator | Capture asset information in a specified format including asset name, custodian, owner, description, and location (M) | Step 8                         |
| 8      | IT Network and Server Administrator | Capture licensed software information using a specified format including software name, license status, IP address/host name, and asset identification (M) | End                            |

### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A(Start) --> B1[List all devices under the custody of the IT department (A/M)]
    B1 --> B2[List all applications and licensed software installed on production servers and desktops/laptops (A/M)]
    B2 --> B3[Fill the server & network device request form for all new server and network device requests (M)]
    B3 --> C{Approved?}
    C -->|No| B4[Fill the server & network device request form again (M)]
    B4 --> C
    C -->|Yes| B5[Update asset inventory file for any asset removed, disposed, or newly purchased (M)]
    B5 --> B7[Capture asset information in a specified format (M)]
    B6 --> B7
    B7 --> B8[Capture licensed software information in a specified format (M)]
    B8 --> D(End)
```

This code block reflects the flow and decision-making process in the flowchart.