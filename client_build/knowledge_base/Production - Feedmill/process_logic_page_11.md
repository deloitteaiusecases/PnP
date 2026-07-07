---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 11
Last_Updated: 2026-03-16
---

Sure, here's the analysis of the flowchart:

### 1. Process Name
- Waste and Rework Handling

### 2. Roles (Swimlanes)
- QA Analyst / Data Entry Operator

### 3. Steps in a Markdown Table

| Step # | Role                           | Action                                                                                         | Next Step/Logic                      |
|--------|--------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------|
| 1      | QA Analyst / Data Entry Operator | Segregate Non-Conforming Material from Process. Record Waste in Daily Production / QA Log. (M) | 2                                    |
| 2      | QA Analyst / Data Entry Operator | Classify as Reworkable or Non-Reworkable Waste (M)                                              | 2.1                                  |
| 2.1    | QA Analyst / Data Entry Operator | Is that Reworkable?                                                                            | Yes: 3, No: 4                        |
| 3      | QA Analyst / Data Entry Operator | Conduct Visual, Chemical, or Micro Analysis. Compare Against Original Batch Specifications (M) | 3.1                                  |
| 3.1    | QA Analyst / Data Entry Operator | Approve for Inclusion (≤5% of New Batch)?                                                      | Yes: 5, No: 4                        |
| 4      | QA Analyst / Data Entry Operator | Tag and Isolate Waste Material. Update Waste Register and SAP Waste Movement. Arrange Disposal. Record Certificate of Disposal. (M) | 6                                    |
| 5      | QA Analyst / Data Entry Operator | Weigh and Document Approved Rework. Enter Rework Data in SAP Linked to New Batch. Add Rework at Defined Formulation Step. Conduct Final QA Clearance of Batch (M) | 6                                    |
| 6      | QA Analyst / Data Entry Operator | QA and Production to Monitor Trends in Waste. Report Monthly Summary to Plant Head / Quality Head. Trigger RCA if Rework/Waste exceeds internal threshold (M) | End                                  |

### 4. Mermaid.js Code Block
```mermaid
graph TD;
    A(Start) --> B[Step 1: Segregate Non-Conforming Material and Record (M)];
    B --> C[Step 2: Classify as Reworkable or Non-Reworkable (M)];
    C --> D{Step 2.1: Is that Reworkable?};
    D -- Yes --> E[Step 3: Conduct Analysis and Compare (M)];
    D -- No --> F[Step 4: Tag, Isolate, Update Register, Arrange Disposal (M)];
    E --> G{Step 3.1: Approve for Inclusion (≤5% of New Batch)?};
    G -- Yes --> H[Step 5: Weigh, Document, Enter Data, Final Clearance (M)];
    G -- No --> F;
    F --> I[Step 6: Monitor, Report Summary, Trigger RCA if Needed (M)];
    H --> I;
    I --> J(End);
```
