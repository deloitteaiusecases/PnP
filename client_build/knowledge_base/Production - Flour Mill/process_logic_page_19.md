---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 19
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

#### 1. Process Name
- Processing / Milling Operation (Process Air Quality Management)

#### 2. Roles (Swimlanes)
- Engineering Technician
- Maintenance Technicians
- QA Analyst
- QA Specialist

#### 3. Steps in Markdown Table

| Step # | Role                  | Action                                                                                                             | Next Step          |
|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|
| 1      | Engineering Technician | Perform routine maintenance of HVAC systems supplying process areas                                                | Step 2             |
| 2      | Engineering Technician | Monitor Differential Pressure (DP) between high care (packing, final flour) and adjacent zones                     | End                |
| 3      | Maintenance Technicians| Check cyclone separators, bag filters, and local extraction fans                                                   | Step 4             |
| 4      | QA Analyst             | Test compressed air quality used for product contact (e.g. pneumatic lines in flour transfer or packing)          | Step 5             |
| 5      | QA Specialist          | Perform air plate testing in milling zones (TSA for bacteria, DG-18 for yeast & mold)                              | Step 6             |
| 6      | QA Specialist          | All air quality and HVAC maintenance records entered in SAP PM; microbiological results logged in SAP QM          | End                |

#### 4. Mermaid.js Code Block

```mermaid
graph TD
    Start --> A[Perform routine maintenance of HVAC systems supplying process areas]
    A --> B[Monitor Differential Pressure (DP) between high care (packing, final flour) and adjacent zones]
    A --> C[Check cyclone separators, bag filters, and local extraction fans]
    C --> D[Test compressed air quality used for product contact (e.g. pneumatic lines in flour transfer or packing)]
    D --> E[Perform air plate testing in milling zones (TSA for bacteria, DG-18 for yeast & mold)]
    E --> F[All air quality and HVAC maintenance records entered in SAP PM; microbiological results logged in SAP QM]
    B --> End
    F --> End
```
