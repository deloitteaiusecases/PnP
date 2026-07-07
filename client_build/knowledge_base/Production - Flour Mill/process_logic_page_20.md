---
Department: Production - Flour Mill
Source_Document: Flour Mill Flow Charts.pdf
Page_Number: 20
Last_Updated: 2026-03-16
---

### Analysis

1. **Process Name**: Processing / Milling Operation - Metal and Foreign Object Management

2. **Roles (Swimlanes)**:
   - Engineering Technician
   - QA Analyst
   - Sifter Operator
   - QA Manager
   - QA Specialist

3. **Steps in Markdown Table**:

| Step # | Role                | Action                                                                                          | Next Step/Logic                                                     |
|--------|---------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1      | Engineering Technician | Inspect and clean inline magnets as per mill layout. Document findings in SAP PM.              | Step 2                                                              |
| 2      | QA Analyst          | Verify metal detector sensitivity using test wands.                                            | Step 3                                                              |
| 3      | QA Analyst          | Conduct manual screening of flour samples (e.g. hand sieve + magnetic check).                  | Step 4                                                              |
| 4      | Sifter Operator     | Visually inspect sifter screens for damage: Torn mesh, sagging, loose fittings.                 | Step 5                                                              |
| 5      | QA Manager          | Lead RCA for any detection event: Identify source; initiate CAPA; coordinate with Maintenance. Block affected lots. | Step 6                                                     |
| 6      | QA Specialist       | All calibration, rejection, RCA, and CAPA records are to be entered in SAP PM and SAP QM.       | End                                                                |

4. **Mermaid.js Code Block**:

```mermaid
graph TD;
    Start --> A1[Inspect and clean inline magnets as per mill layout. Document findings in SAP PM.]
    A1 --> A2[Verify metal detector sensitivity using test wands]
    A2 --> A3[Conduct manual screening of flour samples (e.g. hand sieve + magnetic check).]
    A3 --> A4[Visually inspect sifter screens for damage: Torn mesh, sagging, loose fittings.]
    A4 --> A5[Lead RCA for any detection event: Identify source; initiate CAPA; coordinate with Maintenance. Block affected lots.]
    A5 --> A6[All calibration, rejection, RCA, and CAPA records are to be entered in SAP PM and SAP QM.]
    A6 --> End
```

This structure represents the logical flow and roles involved in the processing/milling operation.