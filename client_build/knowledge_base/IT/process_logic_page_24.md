---
Department: IT
Source_Document: IT.pdf
Page_Number: 24
Last_Updated: 2026-03-16
---

Certainly! Let's break down the analysis of the flowchart for the "Data Sanitisation Procedure".

### 1. Process Name
**Data Sanitisation Procedure**

### 2. Roles (Swimlanes)
- Information Owner
- IT Network and System Admin

### 3. Steps as a Markdown Table

| Step # | Role                      | Action                                                                                                                                                              | Next Step/Logic                            |
|--------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1      | Information Owner         | Determine the type and classification level of media to be sanitised. (M)                                                                                           | Step 2                                     |
| 2      | IT Network and System Admin | Choose the appropriate method for data sanitisation (e.g., overwriting, degaussing, encryption, physical destruction) based on media type and sensitivity. (M)  | Step 3                                     |
| 3      | IT Network and System Admin | Use industry-standard tools and software for effective data removal. Ensure tools are up-to-date and meet security standards. (A/M)                                | Step 5                                     |
| 4      | IT Network and System Admin | Back up any necessary data before sanitisation and secure the media for processing. (A/M)                                                                           | Step 5                                     |
| 5      | IT Network and System Admin | Apply the selected sanitisation method using standardised tools to ensure complete data removal. (A/M)                                                              | Step 6                                     |
| 6      | IT Network and System Admin | Conduct verification processes using audits or validation software to ensure no residual data remains on the media. (A/M)                                          | End                                        |

### 4. Logic as Mermaid.js Code Block

```mermaid
graph TD;
    A1[Start] --> B1[Determine the type and classification level of media to be sanitised. (Step 1)]
    B1 --> C1[Choose the appropriate method for data sanitisation. (Step 2)]
    C1 --> D1[Use industry-standard tools and software for effective data removal. (Step 3)]
    C1 --> E1[Back up any necessary data before sanitisation. (Step 4)]
    D1 --> F1[Apply the selected sanitisation method. (Step 5)]
    E1 --> F1
    F1 --> G1[Conduct verification processes. (Step 6)]
    G1 --> H1[End]
```

This representation provides a clear understanding of the flow and actions involved in the Data Sanitisation Procedure as depicted in the chart.