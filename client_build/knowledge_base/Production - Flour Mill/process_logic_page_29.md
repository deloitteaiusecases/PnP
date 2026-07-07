---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 29
Last_Updated: 2026-03-16
---

### Process Analysis

#### 1. Process Name
- Regulatory Compliance

#### 2. Roles (Swimlanes)
- Procurement Officer
- Silo Operator
- Milling Operator
- Packaging Supervisor
- QA
- Dispatch Officer

#### 3. Steps in a Markdown Table

| Step # | Role                  | Action                                                                                           | Next Step/Logic          |
|--------|-----------------------|--------------------------------------------------------------------------------------------------|--------------------------|
| 1      | Procurement Officer   | Ensures each delivery has a unique Supplier Lot No. (M)                                         | Step 2                   |
| 2      | Silo Operator         | Performs transfers wheat to silo. Links lot to specific bin in SAP. (M)                         | Step 3                   |
| 3      | Milling Operator      | Links production batch to raw wheat lot in SAP. Ensures UD from QA is posted in SAP QM. (M)     | Step 4                   |
| 4      | Packaging Supervisor  | Issues packaging materials via SAP (MM). Links packaging lot to product batch in SAP (M)        | Step 5                   |
| 5      | QA                    | QA posts UD in SAP QM to release finished product. (M)                                          | Step 6                   |
| 6      | Dispatch Officer      | Ensures Only SAP "Released" batches are dispatched. Each delivery note links to corresponding product batch in SAP SD. (A) | Step 7 |
| 7      | QA                    | Conducts quarterly traceability drills from product to wheat/packaging and from raw material to customer (M) | Step 8          |
| 8      | QA                    | Ensures all traceability records retained in SAP for ≥ 5 years (A/M)                            | Step 9                   |
| 9      | QA                    | If linkage is missing or incomplete: QA initiates NCR. Blocks batch in SAP. Corrective action logged (M) | End          |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A[Start] --> B[Step 1: Ensures each delivery has a unique Supplier Lot No. (M)]
    B --> C[Step 2: Performs transfers wheat to silo. Links lot to specific bin in SAP. (M)]
    C --> D[Step 3: Links production batch to raw wheat lot in SAP. Ensures UD from QA is posted in SAP QM. (M)]
    D --> E[Step 4: Issues packaging materials via SAP (MM). Links packaging lot to product batch in SAP (M)]
    E --> F[Step 5: QA posts UD in SAP QM to release finished product. (M)]
    F --> G[Step 6: Ensures Only SAP "Released" batches are dispatched. Each delivery note links to corresponding product batch in SAP SD. (A)]
    G --> H[Step 7: Conducts quarterly traceability drills from product to wheat/packaging and from raw material to customer (M)]
    H --> I[Step 8: Ensures all traceability records retained in SAP for ≥ 5 years (A/M)]
    I --> J{Step 9: If linkage is missing or incomplete}
    J -- Yes --> K[QA initiates NCR. Blocks batch in SAP. Corrective action logged (M)]
    J -- No --> L[End]
```
