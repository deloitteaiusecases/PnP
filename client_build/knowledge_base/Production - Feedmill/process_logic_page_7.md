---
Department: Production - Feedmill
Source_Document: Feedmill flowchart.pdf
Page_Number: 7
Last_Updated: 2026-03-16
---

### Analysis

**1. Process Name:**  
Pelleting

**2. Roles (Swimlanes):**  
- Pelleting Operator
- Pelleting Operator / QA Analyst
- Utility Technician

**3. Steps in Markdown Table:**

| Step # | Role                               | Action                                                      | Next Step/Logic          |
|--------|------------------------------------|-------------------------------------------------------------|--------------------------|
| 1      | Pelleting Operator                 | Receive conditioned mash (A)                                | Step 2                   |
| 2      | Pelleting Operator                 | Check Conditioning Parameters [Temp & Moisture] (M)         | Step 3                   |
| 3      | Pelleting Operator                 | Are Conditioning Parameters within limits?                  | Yes: Step 4, No: Step 3.1 |
| 3.1    | Pelleting Operator                 | Adjust steam input or retention time (M)                    | Step 2                   |
| 4      | Pelleting Operator                 | Pellet Formation via Press (A)                              | Step 5                   |
| 5      | Pelleting Operator / QA Analyst    | Perform Pellet Quality Check (Moisture, Durability, Hardness) (M) | Step 6                   |
| 6      | Pelleting Operator / QA Analyst    | Do Pellet Properties meet defined specs?                    | Yes: Step 7, No: Step 6.1 |
| 6.1    | Pelleting Operator / QA Analyst    | Isolate batch. Conduct RCA. Apply CAPA (M)                  | Step 5                   |
| 7      | Utility Technician                 | Transfer to Cooler (A)                                      | Step 8                   |
| 8      | Utility Technician                 | Measure Cooler Airflow and Relative Humidity (M)            | Step 9                   |
| 9      | Utility Technician                 | Are Cooler Parameters within acceptable range?              | Yes: Step 10, No: Step 9.1 |
| 9.1    | Utility Technician                 | Adjust fan speed / Calibrate sensors (M)                    | Step 8                   |
| 10     | Utility Technician                 | Transfer to Finished Product Holding Bin (A)                | Step 11                  |
| 11     | Pelleting Operator / QA Analyst    | Are All QA Checks Passed?                                   | Yes: Step 12, No: Step 11.1 |
| 11.1   | Pelleting Operator / QA Analyst    | Block batch. Log deviation in SAP. RCA and CAPA (M)         | Step 5                   |
| 12     | Pelleting Operator / QA Analyst    | Approve Batch for Packaging or Dispatch (M)                 | End                      |

**4. Mermaid.js Code Block:**

```mermaid
graph TD;
    Start --> A1[Receive conditioned mash (A)];
    A1 --> A2[Check Conditioning Parameters [Temp & Moisture] (M)];
    A2 --> A3{Are Conditioning Parameters within limits?};
    A3 --Yes--> A4[Pellet Formation via Press (A)];
    A3 --No--> A3.1[Adjust steam input or retention time (M)];
    A3.1 --> A2;
    A4 --> A5[Perform Pellet Quality Check (Moisture, Durability, Hardness) (M)];
    A5 --> A6{Do Pellet Properties meet defined specs?};
    A6 --Yes--> A7[Transfer to Cooler (A)];
    A6 --No--> A6.1[Isolate batch. Conduct RCA. Apply CAPA (M)];
    A6.1 --> A5;
    A7 --> U8[Measure Cooler Airflow and Relative Humidity (M)];
    U8 --> U9{Are Cooler Parameters within acceptable range?};
    U9 --Yes--> U10[Transfer to Finished Product Holding Bin (A)];
    U9 --No--> U9.1[Adjust fan speed / Calibrate sensors (M)];
    U9.1 --> U8;
    U10 --> P11{Are All QA Checks Passed?};
    P11 --Yes--> P12[Approve Batch for Packaging or Dispatch (M)];
    P11 --No--> P11.1[Block batch. Log deviation in SAP. RCA and CAPA (M)];
    P11.1 --> A5;
    P12 --> End;
```