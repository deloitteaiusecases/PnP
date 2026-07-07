---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 22
Last_Updated: 2026-03-16
---

### Analysis of the Flowchart

1. **Process Name**: 
   - Processing / Milling Operation

2. **Roles (Swimlanes)**:
   - Mill Supervisor
   - Mill Operator
   - Maintenance Technician
   - Sifter Operator
   - QA

3. **Steps Extracted into a Markdown Table**:

| Step # | Role                    | Action                                                                                                  | Next Step/Logic                                |
|--------|-------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------|
| 1      | Mill Supervisor         | Perform a full visual inspection of roller mill surfaces, sifter boxes, conveyors, and surrounding areas at start of each shift | Step 2                                        |
| 2      | Mill Operator           | Use approved methods (brushing, vacuum) to remove flour dust from roller surfaces, housings, and covers | Step 3                                        |
| 3      | Maintenance Technician  | Deep cleaning of roller assemblies, covers, feeder mechanisms per validated Master Sanitation Schedule (MSS) | Step 4                                        |
| 4      | Maintenance Technician  | Conduct pneumatic line air flushing, filter replacement, and cyclone vacuuming                         | Step 5                                        |
| 5      | Sifter Operator         | Remove and dry clean all screens using vacuuming, brushing. Air ducts and frames to be wiped            | Step 6                                        |
| 6      | QA                      | Monitor moisture-prone areas for condensation risk                                                      | Step 7                                        |
| 7      | QA                      | Record all cleaning events, non-conformances, and verifications in SAP PM, SAP QM                      | End                                           |

4. **Mermaid.js Code Block**:

```mermaid
graph TD
    A(Start) --> B[Perform a full visual inspection of roller mill surfaces, sifter boxes, conveyors, and surrounding areas]
    B --> C[Use approved methods (brushing, vacuum) to remove flour dust from roller surfaces, housings, and covers]
    C --> D[Deep cleaning of roller assemblies, covers, feeder mechanisms per validated Master Sanitation Schedule (MSS)]
    D --> E[Conduct pneumatic line air flushing, filter replacement, and cyclone vacuuming]
    E --> F[Remove and dry clean all screens using vacuuming, brushing. Air ducts and frames to be wiped]
    F --> G[Monitor moisture-prone areas for condensation risk]
    G --> H[Record all cleaning events, non-conformances, and verifications in SAP PM, SAP QM]
    H --> I(End)
```

This flowchart outlines a detailed process for maintaining the hygiene and efficiency of the milling operation, ensuring quality and compliance.