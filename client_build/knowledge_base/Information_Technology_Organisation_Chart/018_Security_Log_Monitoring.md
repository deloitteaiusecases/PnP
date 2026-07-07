---
Department: Information Technology Organisation Chart
Section: Security Log Monitoring
Section_Kind: core
Section_Priority: normal
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Security Log Monitoring

#### Purpose
The purpose of this procedure is to establish a systematic approach for monitoring security logs within Arabian Mills. By capturing and analysing security-related events, the organisation aims to detect and respond to potential security incidents, ensuring the integrity, confidentiality, and availability of its information assets.
#### Scope
This procedure applies to all critical servers, applications, databases, and network devices within Arabian Mills' IT infrastructure. It covers the identification, collection, analysis, and reporting of security logs to support proactive security management.
#### Procedure Reference
This procedure refers to the Security Event Logging and Monitoring Guidelines of ARABIAN MILLS Information Security, ensuring alignment with overarching security policies and standards.
#### Objectives
The objectives of this procedure are to:
 Capture Security Events: Identify and enable the capture of security-related events for critical IT systems.
 Centralise Log Management: Maintain logs on a central log server with sufficient capacity, ensuring efficient collection and storage.
 Enable Alerting and Reporting: Set email alerts for critical events and report them to asset owners for timely response.
 Analyse and Respond: Analyse the impact and risk of security events, raising incidents when necessary.
 Review and Document: Conduct regular log reviews and submit reports to asset owners, maintaining logs for a specified duration.
#### Security Log Monitoring Procedure
Effective security log monitoring is essential for detecting and responding to potential security incidents. The following table outlines the activities and responsibilities involved in the security log monitoring process:

| S No. | Procedure description | Responsibility | Frequency |
| --- | --- | --- | --- |
| 1 | Identify Security Events: Identify and enable security-related events to be captured for operating systems of critical servers, applications, databases, and network devices. | Preparer: IT Network and System Admin | As needed |
| 2 | Centralise Log Collection: Maintain logs on a central log server with sufficient hard disk capacity. Use SNMP trap or other feasible methods to collect logs centrally. | Preparer: IT Network and System Admin | Ongoing |
| 3 | Set Email Alerts: Set email alerts for critical events from the list identified. | Preparer: IT Network and System Admin | As needed |
| 4 | Report Critical Events: Report any critical event email alerts received to asset owners. | Preparer: IT Network and System Admin | As needed |
| 5 | Analyse Impact and Risk: Analyse the impact level and risk involved and raise incidents if required. | Preparer: IT Network and System Admin | As needed |
| 6 | Review Logs: Review logs monthly, preferably using application/system-generated reports. | Preparer: IT Network and System Admin | Monthly |
| 7 | Submit Log Review Report: Submit the log review report to asset owners, preferably using application/system-generated reports. | Preparer: IT Network and System Admin | Monthly |
| 8 | Maintain Logs: Maintain logs for 1 year. | Preparer: IT Network and System Admin | Ongoing |


**[Diagram — Visio-EMF→PNG]:**

**Process Name:** Security Log Monitoring Procedure  

**Roles / Swimlanes:**

- IT Network and System Admin  

---

### Steps

| Step # | Role | Action | Decision/Next Step |
|--------|------|--------|--------------------|
| 1 | IT Network and System Admin | Identify or enable security related events to be captured over operating systems, critical servers, applications, databases, and network devices. (IAM) | Proceed to Step 2 |
| 2 | IT Network and System Admin | Maintain logs on a central log server or individual critical host/device, using SNMP trap or other feasible methods, to collect logs centrally. (IA) | Proceed to Step 3 |
| 3 | IT Network and System Admin | Set e-mail alerts for critical events from the identified devices. (IA) | Proceed to Step 4 |
| 4 | IT Network and System Admin | Report any critical events via email alerts or send to asset owners. (IAM) | Proceed to Step 5 |
| 5 | IT Network and System Admin | Analyze the impact level and risk involved and initiate corrective action if required. (IAM) | Proceed to Step 6 |
| 6 | IT Network and System Admin | Review logs monthly, generating user, application/ system/department specific logs generated report. (IAM) | Proceed to Step 7 |
| 7 | IT Network and System Admin | Submit the logs review report to asset owners, post-review and sign-off on department generated reports. (IAM) | Proceed to Step 8 |
| 8 | IT Network and System Admin | Maintain logs for 1 year. (IAM) | End |

---

```mermaid
graph TD

    A[Start] --> S1[1. Identify or enable security related events to be captured over operating systems, critical servers, applications, databases, and network devices. (IAM)]
    S1 --> S2[2. Maintain logs on a central log server or individual critical host/device, using SNMP trap or other feasible methods, to collect logs centrally. (IA)]
    S2 --> S3[3. Set e-mail alerts for critical events from the identified devices. (IA)]
    S3 --> S4[4. Report any critical events via email alerts or send to asset owners. (IAM)]
    S4 --> S5[5. Analyze the impact level and risk involved and initiate corrective action if required. (IAM)]
    S5 --> S6[6. Review logs monthly, generating user, application/ system/department specific logs generated report. (IAM)]
    S6 --> S7[7. Submit the logs review report to asset owners, post-review and sign-off on department generated reports. (IAM)]
    S7 --> S8[8. Maintain logs for 1 year. (IAM)]
    S8 --> Z[End]
```