---
Department: Information Technology Organisation Chart
Section: Industrial Control Systems
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Industrial Control Systems
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 0
---

## Industrial Control Systems

#### Purpose
The purpose of this policy is to establish comprehensive guidelines for the protection of Industrial Control Systems (ICS) within Arabian Mills. These guidelines aim to safeguard the integrity, confidentiality, and availability of ICS by implementing robust security measures. The policy ensures that ICS are protected against cyber threats, unauthorised access, and other vulnerabilities that could compromise operational efficiency and safety.
#### Scope
This policy applies to all ICS networks, devices, and systems within Arabian Mills. It encompasses all mills and facilities where ICS are utilised, including Programmable Logic Controllers (PLC), Supervisory Control and Data Acquisition (SCADA) systems, Distributed Control Systems (DCS), and other related infrastructure. The guidelines are mandatory for all employees, contractors, and third-party vendors who have access to or interact with ICS within Arabian Mills.
#### Objectives
The objectives of this policy are to:
 Enhance Security Measures: Implement stringent security controls to protect ICS networks and systems from cyber threats and unauthorised access.
 Ensure Operational Continuity: Maintain the reliability and availability of ICS by preventing disruptions caused by security breaches or vulnerabilities.
 Protect Sensitive Data: Safeguard the confidentiality and integrity of data processed and transmitted within ICS networks.
 Compliance with Standards: Align ICS security practices with international standards such as CIS benchmarks, NIST Cybersecurity Framework, and ISO27001.
 Regular Monitoring and Assessment: Conduct continuous monitoring, vulnerability assessments, and audits to identify and mitigate potential risks.
 Manage Third-Party Access: Establish protocols for secure third-party access to ICS networks, ensuring that external interactions do not compromise security.
 Promote Physical Security: Ensure that physical access to critical ICS components is restricted and monitored to prevent tampering and unauthorised entry.
 Foster a Security Culture: Encourage awareness and adherence to ICS security guidelines among all employees and stakeholders.
#### Responsibility
It is the responsibility of the Cybersecurity Manager, IT & Cybersecurity Manager, and Plant Manager to ensure the implementation of the guidelines.
#### ICS Guidelines
1. Network
 Each mill network should have its network physically separated (Air Gap) from each other.
 Each mill network should use a separate IP range.
 Static IP should be provided to IP network devices/systems.
 Internet should not be provided to systems connecting to Programmable Logic Controller (PLC), Supervisory Control and Data Acquisition (SCADA), or Distributed Control System (DCS) systems.
 VLAN should be implemented for ICS processing critical data or activity; access to such systems should only be through specific systems.
 Purdue Architecture Network diagram for each mill should be maintained.
 Network Diagram showing proper segregation of network at lower levels using segmentation (VLAN) should be maintained.
 IPS/IDS should be implemented in the ICS network.
 Only required ports and protocols should be permitted.
 VOIP network should be different from ICS network.
 Network Access Control (NAC) should be implemented for ICS network.
 Data Flow Diagram showing communication path from command to physical device should be maintained for each critical process.
 A firewall should be placed between the SCADA and automation system.
 Configuration review for IP-based devices should be conducted regularly.
 Unused ports on the switches used inside the mill network should be disabled.
 Network devices and ICS equipment should be securely configured.
 If the internet is required for any system, it should be done through the firewall and such connections should be temporary only.
2. Physical Security
 Critical ICS should be physically protected from unauthorized access.
 Biometric Access should protect physical access to ICS.
 Ethernet cables/communication lines connecting the ICS should be physically protected from physical tampering and environmental effects.
 USB/serial ports on ICS should be disabled or physically damaged if not required.
 Removable media drives should be physically damaged or removed from the system connecting to critical ICS if not required.
 Critical ICS and entry-exit points should be always monitored by CCTV.
 Loading/Unloading areas should be monitored by CCTV and physical guards.
 Unused areas inside the mill should be locked.
3. System Security
 Access to the system should be tightly controlled with passwords.
 Administrative access to the system should be provided on a "Need-to-have" basis.
 The desktops connected to the mill network should be configured as per the "Operating System Secure configuration" by the ARABIAN MILLS IT team.
 USB ports on the desktop should be disabled or physically destroyed if not required.
 MAC binding should be implemented for desktops in the LAN network.
 Maintain a list of all IP-based assets in the ICS network.
 Access control to ICS network logical and physical should be maintained centrally.
 Document all privileged accounts used in the ICS network.
 Audit logs should be centrally maintained for each ICS network, with restricted access.
4. Vulnerability Management
 Vulnerability scanning for IP-based systems, including the ICS, should be conducted regularly.
 Identified patches for the ICS system should be tested on an offline system before implementation.
 Vendors should be involved in ICS updates and patches.
 ICS firmware updates should be installed regularly.
 Anti-malware solutions should be installed on the systems, and such systems should be updated manually.
 A regular predefined scan schedule should be implemented.
5. Third-Party Access
 Remote access to ICS network should be provided only through a temporary VPN. A complex password of a minimum of 14 digits should be used and changed monthly.
 Direct access to ICS network should not be provided to any entity outside ARABIAN MILLS.
 Risk assessment should be conducted before providing third-party access to the ICS network.
 Vendor Risk Assessment should be conducted for all third-party vendors. If regular third-party access is required for ICS network, it should be through the DMZ network.
 Remote access should be logged and monitored. Access logs should be reviewed regularly.
 Password for the third party should not be embedded in scripts.
 Cloud application for reporting and monitoring should be avoided, and if required, a Risk assessment should be conducted.