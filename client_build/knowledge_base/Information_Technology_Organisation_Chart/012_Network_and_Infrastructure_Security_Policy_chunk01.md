---
Department: Information Technology Organisation Chart
Section: Network and Infrastructure Security Policy
Section_Kind: core
Section_Priority: normal
Chunk: 1 of 1
Chunk_Name: Network and Infrastructure Security Policy
Source: Information Security Procedure.docx
Document_Class: section_chunk
Is_Full_Document: false
Images: 1
---

## Network and Infrastructure Security Policy

#### Purpose
The purpose of this policy is to establish comprehensive security standards for Arabian Mills' network infrastructure and datacentre facilities. These standards are designed to protect information assets from cybersecurity threats, unauthorised access, and environmental hazards. By defining clear protocols and procedures, Arabian Mills aims to ensure the integrity, confidentiality, and availability of its critical systems and data, supporting the organisation's operational efficiency and business continuity.
#### Scope
This policy applies to all network infrastructure and datacentre facilities under the control of Arabian Mills. It encompasses:
1. Network Infrastructure: Includes routers, switches, firewalls, cabling, VPNs, email gateways, PBX systems, IP printers, and network diagrams. It covers both on-premise and cloud-hosted environments, ensuring secure access and communication protocols are enforced.
2. Datacentre Security: Addresses physical security, environmental controls, cabling, and power management for datacentres located at Riyadh HQ, Hail, and Jizan. It includes measures for fire suppression, access control, and maintenance of critical systems within the datacentre environment.
#### Objectives
The objectives of this policy are to:
1. Enhance Security Measures:
 Implement robust security controls to protect network infrastructure and datacentre facilities from cyber threats and unauthorised access.
 Ensure physical security and environmental protection within datacentres to safeguard assets from damage.
2. Ensure Operational Continuity:
 Maintain the reliability and availability of IT systems by preventing disruptions caused by security breaches or environmental hazards.
 Ensure redundancy and failover mechanisms are in place to support business continuity.
3. Protect Sensitive Data:
 Safeguard the confidentiality and integrity of data processed and transmitted within network and datacentre environments.
 Implement encryption and secure access protocols to prevent data breaches and unauthorised access.
4. Compliance with Standards:
 Align security practices with international standards and best practices for network and infrastructure security.
 Ensure compliance with regulatory requirements and internal policies to mitigate risks and enhance security posture.
#### Responsibility
The responsibility for implementing and maintaining the security standards outlined in this policy is shared among several key roles within Arabian Mills:
IT Network and Server Team:
 Responsible for the day-to-day implementation of security measures across network infrastructure and datacentre facilities.
 Conduct regular assessments, develop security protocols, and deploy security measures as needed.
IT & Cybersecurity Manager:
 Oversees compliance with security standards and reviews the effectiveness of security measures.
 Monitors security performance identifies areas for improvement, and ensures protocols are up to date with emerging threats.
 Approves changes to security protocols and procedures, ensuring alignment with organisational objectives and regulatory requirements.
 Reports security outcomes and improvements to senior management, facilitating informed decision-making.
#### Network Security Standard
1. Segregation of Duties:
 Roles and responsibilities must be assigned, implemented, and reviewed for critical activities.
 Due care must be exercised to segregate roles and responsibilities, with appropriate supervision where segregation is not feasible.
2. Access to Network:
 Access to applications and rights must be granted only after approval from the IT & Cybersecurity Manager (branch), IT & Cybersecurity Manager (HQ), and Asset Owner.
 Logging must be enabled on network devices, and logs must be monitored and reviewed periodically.
 Unused LAN ports must be secured by disabling them on the switch.
 Vendors requesting internet access must fill an Access request form and obtain approval before access is provided.
 A separate firewall rule for allowing the MAC address of the requested laptop should be created and removed after the requested time expires.
 Access to system configurations and documentation must be restricted on a "need to know" basis.
 Access to internet sites for business purposes, which are otherwise blocked, must be granted only after approval from the IT & Cybersecurity Manager (HQ) and CFO.
 The internet connection must have redundancy built into the network to ensure business continuity.
 Remote access to diagnostic ports must be protected.
 All remote access sessions must be authorised by the IT & Cybersecurity Manager (HQ) and CFO.
 System administrators must supervise remote access for troubleshooting IT systems.
 Systems that are remotely accessed must be audited for configuration every quarter.
 Employees connecting to Arabian Mills information systems from an external network must connect through a VPN with an inactivity session timeout of 5 minutes on servers and network devices.
 A Remote Access form must be filled, maintained, and approved before access is provided.
 All remote access connections must be logged, and the logs must be monitored and reviewed.
3. Segregation of Network:
 Network external to Arabian Mills must be segregated from the internal network using secured perimeter devices.
 Rules on secured perimeter devices must deny any unauthorised access to or from the internal network.
 Users working on the Arabian Mills IT network must be educated about the acceptable use of the internet.
4. Network Change Management and Monitoring:
 Any change to secured network devices and configurations must follow the Change Management Procedure.
 Configurations must be backed up before and after changes.
 Logs of critical network devices must be monitored daily.
5. Cabling Security
 Grounding: Power cables must be properly grounded to prevent electrical hazards.
 Segregation: Power cables must be segregated from communication cables to prevent interference.
 Shielding: Electromagnetic shielding must be implemented for data cables to protect against external interference.
 Storage: Unused cables must be stored centrally in a locked location to prevent unauthorised access.
 Removal: Unused data cables attached to network points must be removed to maintain security.
 Inspection: Conduct regular technical sweeps and visual inspections to verify unwanted devices connected to network cables.
 Separation: Power cables and data cables used in racks must be physically separated from each other to prevent interference.
6. Router Security Standard
 Default Credentials: Default username and password for routers must not be used for login.
 Secure Configuration: Network administrators must prepare secure configuration and implementation documents.
 Service Management: Disable unused services on the WAN interface and unused interfaces.
 Security Features: Disable BOOTP server, source routing, Proxy ARP, and AUX port.
 Access Control: Restrict insecure HTTP services and define interface descriptions for all active interfaces.
 Authentication: Each administrator must use their username and password for access.
 Access Lists: Configure access lists to deny all incoming connections by default, using explicit rules to allow incoming connections.
 Encryption: Router passwords must be encrypted.
 Time Synchronisation: NTP protocol must be set.
 Firmware Updates: Router firmware must be updated regularly after testing.
 Port Management: Unsecure ports and protocols must not be used unless there is a business requirement.
 Port Scanning: Use a port scanner to ensure unwanted ports are closed.
 Password Management: Maintain router administrator password in a safe location with the IT & Cybersecurity Manager (HQ).
 Login Banner: Configure a login banner for the router.
7. Network Switch Security Standard
 Secure Configuration: Network administrators must prepare secure configuration and implementation documents.
 Network Segregation: Segregate networks based on risk analysis and asset criticality.
 Service Management: Review all available terminal and management ports and services.
 Time Synchronisation: Configure NTP.
 User Accounts: Assign unique, per-user accounts.
 Default Credentials: Default username and password for switches must not be used for login.
 Password Policies: Force users to periodically change their passwords and only grant minimum access privileges.
 Port Management: Disable all terminal and management ports that are not explicitly required or actively being used.
 Access Protocols: Permit device access through required and supported services and protocols, using only secure access protocols such as SSH and HTTPS.
 Service Management: Deny unused and unnecessary terminal and management services and protocols, e.g., telnet, HTTP.
 Session Management: Enforce idle and active session timeouts to detect and close inactive sessions.
 Password Policies: Enforce strong password guidelines and restrict the frequency of login attempts.
 Lockout Policies: Enforce a lockout period and restrict the maximum number of concurrent sessions.
 Legal Notification: Display a legal notification banner.
 Web Access: Disable HTTP/HTTPS access if not required and permit web access only from authorised originators.
 SNMP Configuration: Use SNMP v3.0 and delete default community strings.
8. Firewall Security Standard
 Default Credentials: Default username and password for firewalls must not be used for login.
 Secure Configuration: Firewall administrators must prepare secure configuration and implementation documents.
 Web Application Firewall: Enable Web Application Firewall (WAF) or implement a separate WAF for online services.
 Change Management: Firewall rule changes must follow the Change Management Procedure.
 Firewall Rule Review: Firewall rule sets must be reviewed quarterly by the IT & Cybersecurity Manager.
 Service Management: Maintain a list of all services, ports, and IP addresses used in firewall rules.
 Login Banner: Configure a login banner for the firewall.
 Authentication: Each administrator must use their username and password for access.
 Policy Enforcement: Firewall policies must be based on risk analysis and block all inbound and outbound traffic, with exceptions made for desired traffic.
 VPN Traffic: VPN traffic must be scanned with antivirus, anti-malware, and Intrusion Prevention System (IPS) before entering the network.
 Traffic Management: Policies must consider the source and destination of traffic in addition to the content.
 Invalid Addresses: Block network traffic with invalid or private addresses by default.
 Time Synchronisation: Enable timestamp and time sync.
 Application Control: Determine which applications may send traffic into or out of the network and create firewall policies to block traffic for other applications.
 Management Protocols: Manage firewalls using HTTPS or other secure protocols only.
 Password Management: Maintain firewall administrator password in a safe location with the IT & Cybersecurity Manager (HQ).
 Network Diagram: Always maintain updated network connection diagrams.
9. DMZ Security Standard
 Implementation: DMZ (Demilitarised Zone) must be implemented behind the corporate firewall.
 Address Translation: All servers or devices in the DMZ must use NAT/PAT (Network Address Translation/Port Address Translation).
 Traffic Direction: Network traffic from the internet to the server or device in the DMZ must be directed to specific IPs and ports.
 IP Range: Use a different IP range for DMZ servers or devices, distinct from the LAN IP range.
 Traffic Control: Network traffic from the DMZ to the internal LAN must be disabled by default. If required, direct traffic to specific IPs and ports.
 Server Security: Servers placed in the DMZ must follow the "Server Security Standard."
 Switch Configuration: Switches used in the DMZ must be configured according to the "Network Switch Security Standard."
 LAN to DMZ Traffic: Network traffic from the LAN to the DMZ must be specific to the IP and port that needs to be connected.
10. Internet Security Standard
 Monitoring: The IT Department must monitor internet use from all computers and devices connected to the corporate network.
 Logging: Record the source IP address, date, time, protocol, and destination site or server for all traffic.
 User Identification: Record the User ID of the person or account initiating the traffic.
 Blocking: Block access to internet websites and protocols deemed inappropriate for Arabian Mills' corporate environment.
 Blocked Categories: Block the following categories of websites:
 Adult/Sexually Explicit Material
 Advertisements & Pop-Ups
 Chat and Instant Messaging
 Gambling
 Hacking
 Illegal Drugs
 Intimate Apparel and Swimwear
 Peer-to-Peer File Sharing
 Personals and Dating
 Social Network Services
 SPAM, Phishing, and Fraud
 Spyware
 Offensive Content
 Violence, Intolerance, and Hate
 Web-Based Email (Hotmail, Yahoo, etc.)
 Review: Periodically review and recommend changes to web and protocol filtering rules.
 Access Permission: Employees may access blocked sites with permission if appropriate and necessary for business purposes.
 Prohibited Activities: Prohibit ordering items or services on the internet and participating in online contests, promotions, and games.
11. Email Gateway Security Standard
 Deployment: Deploy email gateway in the DMZ of the corporate firewall.
 Connection Security: Ensure connections to the web interface for email gateways are through SSL/HTTPS.
 Web Interface: Disable email gateway web interface via the internet.
 Scanning: Scan all inbound and outbound emails with antivirus and antimalware filters.
 Default Credentials: Change default username and password immediately.
 Anti-Spoofing: Configure the email gateway to prevent spoofing, phishing, and spear-phishing attacks.
 Protocols: Configure DKIM and SPF protocols for the Arabian Mills email domain.
 Sender Authentication: Authenticate sender ID through the email gateway.
 Logging: Enable logging for administrative access to the email gateway and maintain logs for at least three months.
12. VPN Security Standard
 Connection Security: All connections to Arabian Mills network from outside for accessing resources must be made through VPN.
 Real-Time Enforcement: Enforce VPN security policy in "real-time" for VPN client connections.
 Firewall Integration: VPN client connection must be through the corporate firewall.
 Access Control: Provide VPN client access to specific IPs, not the entire network.
 Data Inspection: Inspect VPN client data for antivirus, anti-malware, IPS/IDS.
 User Authentication: Do not use generic usernames for VPN client access.
 Risk Analysis: Approve all VPN access after proper risk analysis.
 Timeout: Inactive VPN client connections must time out after five minutes.
 Tunnelling Mode: Use tunnelling mode for all VPN client connections to ensure all traffic from the system goes through the VPN.
 Site-to-Site VPN: Use IPSec (Transport mode) for site-to-site VPN between branches.
 Login Banner: Configure a login banner for VPN connections, including a confidentiality clause and implications for not following it.
13. PBX Security Standard
 Administrative Interface: Protect the administrative interface by using a strong password.
 Default Credentials: Change the default IP PBX password.
 User Authentication: Choose strong and unique passwords for IP phone access. Do not use IP phone extension as the access password.
 Network Configuration: Use a separate network (VLAN) for IP phones.
 Static IPs: Use static IPs for IP phones to avoid connections with the corporate DHCP server.
 Emergency Calls: Allow direct emergency calls to civil services like ambulance, police, and fire service from IP phones.
 Software Updates: Regularly update PBX and IP phone software and firmware.
 Voice Message Access: Access voice messages on IP phones through a password.
14. IP Printer Security Standard
 Admin Password: Set strong admin passwords, as most manufacturers do not set any password.
 IP Range: Select a separate IP range for printers and use a different VLAN if possible.
 Service Management: Disable any unnecessary services running on printers.
 Firmware Updates: Regularly check for and implement firmware updates.
 Wireless Printing: Disable the wireless printing option if not required.
 Access Control: Use complex PINs for printing access. Individual users must use their PINs to access the print option.
 Physical Protection: Physically protect unused physical ports on printers by locking or covering them with sticky tape.
15. Network Diagram Standard
1. High-Level Network Diagram (Physical):
 Represent all connections in and out of the network.
 Include all network devices in use, such as routers, firewalls, and switches.
 Clearly mark the DMZ with servers and applications.
 Show connections to any external cloud service providers, branches, and other networks.
2. Low-Level Network Diagram (Logical):
 Detail ISP connection specifics.
 Illustrate how devices communicate and how information flows through the network.
 Depict IP addresses on each connected interface, subnets, network devices, and routing protocols.
 Appropriately label devices.
 Specify server farms with server roles.
 Include power supply connections inside the rack.
16. Approved Protocols List (Standard Ports)

| Port | Service Name | Transport Protocol |
| --- | --- | --- |
| 20, 21 | Secure File Transfer Protocol (SFTP) | TCP |
| 22 | Secure Shell (SSH) | TCP and UDP |
| 23 | Telnet | TCP |
| 25 | Simple Mail Transfer Protocol (SMTP) | TCP |
| 50, 51 | IPSec | TCP |
| 53 | Domain Name System (DNS) | TCP and UDP |
| 67, 68 | Dynamic Host Configuration Protocol (DHCP) | UDP |
| 69 | Trivial File Transfer Protocol (TFTP) | UDP |
| 80 | Hypertext Transfer Protocol (HTTP) | TCP |
| 110 | Post Office Protocol (POP3) | TCP |
| 119 | Network News Transport Protocol (NNTP) | TCP |
| 123 | Network Time Protocol (NTP) | UDP |
| 135-139 | NetBIOS | TCP and UDP |
| 143 | Internet Message Access Protocol (IMAP4) | TCP and UDP |
| 161, 162 | Simple Network Management Protocol (SNMP) | TCP and UDP |
| 389 | Lightweight Directory Access Protocol (LDAP) | TCP and UDP |
| 443 | HTTP with Secure Sockets Layer (SSL) | TCP and UDP |
| 3389 | Remote Desktop Protocol (RDP) | TCP and UDP |

Note: For any other protocol use, permission must be taken from the IT & Cybersecurity Manager using the Change Request Form.
Authorization Matrix (Segregation of Duties)

| Infrastructure Component | Activity | Authorized By | Implementor | Verifier |
| --- | --- | --- | --- | --- |
| Network Device (Firewall, Switches, Router) | Change Management (changes implemented) | IT & Cybersecurity Manager , BU Head, CFO | System Admin 1 | System Admin 2 |
| Network Device (Firewall, Switches, Router) | Maintain Change Management document | Not Applicable | System Admin 1 | IT & Cybersecurity Manager |
| Network Device (Firewall, Switches, Router) | Firmware Upgrade, Patching | IT & Cybersecurity Manager | System Admin 1 | System Admin 2 |
| Network Device (Firewall, Switches, Router) | Configuration backup | Not Applicable | System Admin 1 | IT & Cybersecurity Manager |
| Infrastructure Component | Activity | Authorized By | Implementor | Verifier |

#### Datacentre Security Standards
1. Physical Security
 Access Control: Implement biometric access for datacentre entry, connected to an Uninterrupted Power Supply (UPS) for backup power.
 Fail-Safe Mechanisms: Ensure access doors fail safe during power blackouts and connect to fire alarm systems for fail-safe activation.
 Visitor Management: Maintain a visitor entry register at the datacentre entry point. Visitors are allowed only for official business purposes.
 Emergency Communication: Install a direct phone line at the datacentre entry for emergency use.
 Surveillance: Install CCTV cameras to monitor entry and exit points, as well as rack doors. Maintain recordings for three months in archive and one month on Digital Video Recorder.
2. Environmental Controls
 Server and Equipment Placement: Place all production servers and network equipment inside locked racks when not in use.
 Anti-Static Measures: Use anti-static bands tied to racks or anti-static mats on the datacentre floor.
 Evacuation Plans: Display emergency evacuation plans at the entry point, including contact details for emergency response.
 Power Management: Design datacentres with separate wiring for AC units and servers/network equipment, avoiding overloaded power cables and outlets.
 Fireproofing: Use fireproof paints for datacentre walls, made of concrete with alternate fire exits.
 Fire Suppression: Use FM 200 as the primary fire suppression system, with CO2 cylinders placed at the entry point. Maintain FM 200 in a controlled environment outside the datacentre.
3. Cabling and Power Management
 Cabling Standards: Lay cables neatly in conduits or cable trays, properly labelled to match wiring diagrams.
 Diagram Maintenance: Maintain cabling diagrams and check periodically, especially before maintenance work.
 Cable Separation: Separate power and data cables inside conduits.
 Cable Capacity: Use high-capacity electrical cables to prevent heating from overload.
#### Annexure

**[Diagram — Visio-EMF→PNG]:**

Data Center Security  
Standard Forms.pdf