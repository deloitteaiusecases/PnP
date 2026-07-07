---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 28
Last_Updated: 2026-03-16
---

## Analysis

### 1. Process Name
- Product Labelling

### 2. Roles (Swimlanes)
- Regulatory Affairs Officer
- QA
- Packaging Operator
- Warehouse Supervisor

### 3. Steps

| Step # | Role                    | Action                                                                                       | Next Step/Logic         |
|--------|-------------------------|----------------------------------------------------------------------------------------------|-------------------------|
| 1      | Regulatory Affairs Officer | Prepares master artwork and Label content. Obtain Approvals from QA and Document Control and archive (A/M). | 2                       |
| 2      | QA                       | Verify the latest approved template is used and Printer settings (M).                         | 3                       |
| 3      | QA                       | Correct template version available?                                                          | Yes: 4.1, No: 3.1       |
| 3.1    | QA                       | Halt printing, load correct version                                                          | 2                       |
| 4      | Packaging Operator       | Print labels or operate label applicator with pre-printed materials (M).                      | 4.1                     |
| 4.1    | QA                       | Checks first-off sample: Legibility, Accuracy, Log start of batch printing in SAP (M).        | 5                       |
| 5      | QA                       | Performs hourly line inspection (M).                                                         | 6                       |
| 6      | QA                       | Correct template version available?                                                          | Yes: 7, No: 6.1         |
| 6.1    | QA                       | Stop line, isolate affected units, issue NCR                                                 | End                     |
| 7      | Packaging Operator       | Ensures correct label placement and adhesion (M).                                            | 8                       |
| 8      | QA                       | Verifies Label match with SKU, Correct batch linkage, No stock mix-up, Sample pulled from warehouse before dispatch (M). | 9                       |
| 9      | QA                       | Any labeling deviation: Raised as NCRCRA + CAPA conducted. QA to document in SAP QM (A/M).   | 10                      |
| 10     | Warehouse Supervisor     | Reconciles label rolls issued vs. used. Returns leftovers to store (M).                      | 11                      |
| 11     | Warehouse Supervisor     | Label version, batch usage, inspections, and non-conformance logs are updated (M).           | End                     |

### 4. Logic in Mermaid.js

```mermaid
graph TD;
    A(Start) --> B[1. Prepares master artwork and Label content. Obtain Approvals (A/M)]
    B --> C[2. Verify the latest approved template is used and Printer settings (M)]
    C --> D{3. Correct template version available?}
    D -- Yes --> E[4. Print labels or operate label applicator (M)]
    D -- No --> F[3.1 Halt printing, load correct version]
    F --> C
    E --> G[4.1 Checks first-off sample: Legibility, Accuracy (M)]
    G --> H[5. Performs hourly line inspection (M)]
    H --> I{6. Correct template version available?}
    I -- Yes --> J[7. Ensures correct label placement and adhesion (M)]
    I -- No --> K[6.1 Stop line, isolate affected units, issue NCR]
    K --> L(End)
    J --> M[8. Verifies Label match with SKU, Correct batch linkage (M)]
    M --> N[9. Any labeling deviation: Raised as NCRCRA + CAPA (A/M)]
    N --> O[10. Reconciles label rolls issued vs. used (M)]
    O --> P[11. Label version, batch usage, inspections updated (M)]
    P --> L(End)
```