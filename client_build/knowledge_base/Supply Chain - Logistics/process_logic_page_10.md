---
Department: Supply Chain - Logistics
Source_Document: Supply Chain - Logistics.pdf
Page_Number: 10
Last_Updated: 2026-03-16
---

### 1. Process Name
Internal Stock Transfers Between Warehouses/Branches

### 2. Roles (Swimlanes)
- Warehouse
- Transport Coordinator
- QA Officer/Supervisor
- Driver/Dispatcher
- Receiving Clerk
- Inventory Supervisor
- Document Control Officer

### 3. Steps in Markdown Table

| Step # | Role                     | Action                                                                 | Next Step/Logic                                     |
|--------|--------------------------|------------------------------------------------------------------------|-----------------------------------------------------|
| 1      | Warehouse                | Start                                                                  | 2                                                   |
| 2      | Warehouse                | Create a Stock Transfer Order (STO) in SAP and get it approved         | 3                                                   |
| 3      | Warehouse                | Scan and weigh all items listed in the STO                             | 4                                                   |
| 4      | Transport Coordinator    | Assign vehicle based on product type and volume                        | 5                                                   |
| 5      | QA Officer/Supervisor    | Inspect vehicle cleanliness and apply seal after loading               | 6                                                   |
| 6      | Driver/Dispatcher        | Dispatch material to the destination branch                            | 7                                                   |
| 7      | Receiving Clerk          | Verify seal, scan and weigh incoming goods, and post receipt in SAP    | 8                                                   |
| 8      | Inventory Supervisor     | Discrepancy Report                                                     | 9                                                   |
| 9      | Document Control Officer | Digital Archive Folder                                                 | 10                                                  |
| 10     | Document Control Officer | End                                                                    | -                                                   |

### 4. Logic in Mermaid.js

```mermaid
graph TD
    A[Start] --> B[Create a Stock Transfer Order (STO) in SAP and get it approved]
    B --> C[Scan and weigh all items listed in the STO]
    C --> D[Assign vehicle based on product type and volume]
    D --> E[Inspect vehicle cleanliness and apply seal after loading]
    E --> F[Dispatch material to the destination branch]
    F --> G[Verify seal, scan and weigh incoming goods, and post receipt in SAP]
    G --> H[Discrepancy Report]
    H --> I[Digital Archive Folder]
    I --> J[End]
```
