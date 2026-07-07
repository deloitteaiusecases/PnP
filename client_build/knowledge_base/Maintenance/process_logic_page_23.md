---
Department: Maintenance
Source_Document: Maintenance.pdf
Page_Number: 23
Last_Updated: 2026-03-16
---

Here is the analysis based on the provided flowchart image:

### 1. Process Name:
- Energy Efficiency

### 2. Roles (Swimlanes):
- Engineering Team
- Maintenance
- Supervisor
- EHS Officer

### 3. Steps in Markdown Table:

```markdown
| Step # | Role            | Action                                                                                         | Next Step/Logic             |
|--------|-----------------|------------------------------------------------------------------------------------------------|-----------------------------|
| 1      | Engineering Team| Install and maintain sub-meters on major energy consumers (compressors, HVAC, mills). (M)      | 2                           |
| 2      | Maintenance     | Manager collects energy data and correlates with production volumes to calculate monthly KPI. (M) | 3                           |
| 3      | Maintenance     | Technicians ensure rotating equipment is aligned, cleaned, and lubricated to reduce load. (M)  | 4                           |
| 4      | Maintenance     | Technician conducts regular inspections using visual, auditory, or ultrasonic methods. (M)     | 5, 6                        |
| 5      | Maintenance     | Ensure airflow systems (compressors, HVAC, dust collectors) are running at low resistance. (M) | 9                           |
| 6      | Vendor          | Ensure correct readings and control responses for temperature, pressure, and flow. (M)         | 7                           |
| 7      | Vendor          | Provide technical input and execution support for VFDs, efficient motors, insulation upgrades, and power factor correction systems. (M) | 8                           |
| 8      | Maintenance     | Investigate spikes or drops in energy cost per ton; link with equipment condition, production load, or weather. (M) | 10                          |
| 9      | EHS Officer     | Promote awareness on idling, optimal usage, and shutdown procedures (M)                        | 10                          |
| 10     | Supervisor      | Collaborate with utilities and consultants to identify savings across systems and operations. (M) | End                          |
```

### 4. Logic in Mermaid.js Code Block:

```mermaid
graph TD;
    Start --> A1[Install and maintain sub-meters on major energy consumers (M)]
    A1 --> A2[Manager collect energy data and correlate with production volumes (M)]
    A2 --> A3[Technicians ensure rotating equipment is aligned, cleaned, and lubricated (M)]
    A3 --> A4[Conduct regular inspections using visual, auditory, or ultrasonic methods (M)]
    A4 --> A5[Ensure airflow systems are running at low resistance (M)]
    A4 --> A6[Ensure correct readings and control responses (M)]
    A5 --> A9[Promote awareness on idling, optimal usage, and shutdown procedures (M)]
    A9 --> A10[Collaborate with utilities and consultants (M)]
    A6 --> A7[Provide technical input and execution support (M)]
    A7 --> A8[Investigate spikes or drops in energy cost per ton (M)]
    A8 --> A10
    A10 --> End
```

This translates the flowchart into a structured format to aid in automation and process optimization.