---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 27
Last_Updated: 2026-03-16
---

### Analysis of Flowchart

1. **Process Name**: Packaging Quality

2. **Roles (Swimlanes)**:
   - Packaging Supervisor
   - QA
   - Packaging Operator
   - Data Entry Operator

3. **Steps in Markdown Table**:

```markdown
| Step # | Role                  | Action                                                                                  | Next Step/Logic        |
|--------|-----------------------|-----------------------------------------------------------------------------------------|-------------------------|
| 1      | Packaging Supervisor  | Ensure only approved packaging materials are used. (M)                                  | Step 2                  |
| 2      | QA                    | Checks visual defects. Correct SKU and label match. Defective material is quarantined. (M) | Step 5                  |
| 3      | Packaging Operator    | Performs start-up validation of batch code, expiry date, product label. (M)             | Step 4                  |
| 4      | Packaging Operator    | Print and label correct?                                                               | Yes: Step 5 / No: Step 4.1 |
| 4.1    | Packaging Operator    | Halt and Correct (M)                                                                    | Step 3                  |
| 5      | QA                    | Verify filler calibration and fill weight (M)                                           | Step 6                  |
| 6      | QA                    | Conducts seal integrity testing: Peel/pull strength tests every hour. Visual inspection for leaks (M) | Step 7                  |
| 7      | QA                    | Checks bags on conveyor. (M)                                                           | Step 8                  |
| 8      | QA                    | All finished packs pass through a calibrated metal detector (A)                        | Decision: Approved?     |
| 9      | QA                    | Approved?                                                                              | Yes: Step 10 / No: Step 9.1 |
| 9.1    | QA                    | Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M) | End                     |
| 10     | Packaging Operator    | Ensures stable pallet stacking, correct pallet label, proper shrink wrapping (M)        | Step 11                 |
| 11     | Data Entry Operator   | Posts batch data into SAP MM/WM. (M)                                                   | End                     |
```

4. **Mermaid.js Code Block**:
```mermaid
graph TD;
    Start --> A1[Ensure only approved packaging materials are used (M)]
    A1 --> A2[Checks visual defects. Correct SKU and label match. Defective material is quarantined (M)]
    A2 --> A5[Verify filler calibration and fill weight (M)]
    A3[Performs start-up validation of batch code, expiry date, product label (M)] --> A4{Print and label correct?}
    A4 -->|Yes| A5
    A4 -->|No| A4.1[Halt and Correct (M)]
    A4.1 --> A3
    A5 --> A6[Conducts seal integrity testing: Peel/pull strength tests every hour. Visual inspection for leaks (M)]
    A6 --> A7[Checks bags on conveyor (M)]
    A7 --> A8[All finished packs pass through a calibrated metal detector (A)]
    A8 --> A9{Approved?}
    A9 -->|Yes| A10[Ensures stable pallet stacking, correct pallet label, proper shrink wrapping (M)]
    A9 -->|No| A9.1[Any deviation: NCR raised by QA. Root cause analysis conducted. CAPA documented and linked in SAP QM (A/M)]
    A9.1 --> End
    A10 --> A11[Posts batch data into SAP MM/WM (M)]
    A11 --> End
```