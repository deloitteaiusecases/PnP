---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 6
Last_Updated: 2026-03-16
---

### Analysis

#### 1. Process Name

- **Mixing (Batching)**

#### 2. Roles (Swimlanes)

- **Shift Operator Mixing / QA Analyst** 
- **QA Analyst**

#### 3. Process Steps in a Markdown Table

| Step # | Role                          | Action                                                              | Next Step/Logic          |
|--------|-------------------------------|---------------------------------------------------------------------|--------------------------|
| 1      | Shift Operator Mixing         | Confirm BOM, batch number, and material issue status                | 2                        |
| 2      | Shift Operator Mixing         | Validate Formulation & Material Availability                        | 2.1                      |
| 2.1    | Shift Operator Mixing         | Are all materials available?                                        | Yes: 3, No: 2.1.1        |
| 2.1.1  | Shift Operator Mixing         | Hold batch, inform Planning & SCM                                   | End                      |
| 3      | Shift Operator Mixing         | Inspect mixer (cleanliness, dryness, mechanical status)             | 4                        |
| 4      | Shift Operator Mixing         | Weigh Macro and Micro Ingredients                                   | 5                        |
| 5      | Shift Operator Mixing         | Follow SAP or formulation-defined sequence                          | 5.1                      |
| 5.1    | Shift Operator Mixing         | Any allergenic or sensitive ingredients?                            | Yes: 5.1.1, No: 6        |
| 5.1.1  | Shift Operator Mixing         | Perform pre-mix or segregation control                              | 6                        |
| 6      | Shift Operator Mixing         | Load Ingredients into Mixer                                         | 7                        |
| 7      | Shift Operator Mixing         | Start Mixing. Maintain validated mixing time and speed. Log parameters | 8                        |
| 8      | Shift Operator Mixing         | Take minimum 10 samples (top, mid, bottom)                          | 9                        |
| 9      | QA Analyst                    | Is CV% within acceptable limit?                                     | Yes: 10, No: 9.1         |
| 9.1    | QA Analyst                    | Block batch, rework, initiate RCA                                   | End                      |
| 10     | QA Analyst                    | Enter CV% Result in SAP – QM Module. Trigger usage decision and archive report | End              |
| 11     | QA Analyst                    | Conduct RCA, initiate CAPA, rework or discard batch                 | End                      |

#### 4. Mermaid.js Code Block

```mermaid
graph TD;
    A(Start) --> B1[Confirm BOM, batch number, and material issue status (M)]
    B1 --> B2[Validate Formulation & Material Availability (M)]
    B2 --> B3{Are all materials available?}
    B3 -- Yes --> B4[Inspect mixer (cleanliness, dryness, mechanical status) (M)]
    B3 -- No --> B5[Hold batch, inform Planning & SCM (M)] --> B16(End)
    B4 --> B6[Weigh Macro and Micro Ingredients (M)]
    B6 --> B7[Follow SAP or formulation-defined sequence (M)]
    B7 --> B8{Any allergenic or sensitive ingredients?}
    B8 -- Yes --> B9[Perform pre-mix or segregation control (M)]
    B9 --> B10[Load Ingredients into Mixer (M)]
    B8 -- No --> B10
    B10 --> B11[Start Mixing. Maintain validated mixing time and speed. Log parameters (M)]
    B11 --> B12[Take minimum 10 samples (top, mid, bottom) (M)]
    B12 --> B13{Is CV% within acceptable limit?}
    B13 -- Yes --> B14[Enter CV% Result in SAP – QM Module. Trigger usage decision and archive report (M)] --> B16
    B13 -- No --> B15[Block batch, rework, initiate RCA (M)]
    B15 --> B16
    B14 --> B16
```