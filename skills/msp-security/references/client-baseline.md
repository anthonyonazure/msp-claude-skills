# Client Security Baseline: Full Control Checklist

**Defaults you must review:** the tiers, thresholds, and targets in this file are shipped
example defaults from a working MSP. Review and replace them with your own before anything goes
client-facing (see Setup Decisions in SKILL.md).

The detailed standard behind the short list in SKILL.md. Use it for onboarding assessments,
the annual assessment, hardening work, and answering "is this client where it should be?"

Tiers: **T1** = Baseline, every managed client, delivered inside the managed service.
**T2** = Recommended, quoted per client through msp-pricing. Regulated additions live in
`compliance-overlays.md`.

For every control, the assessment records: status (in place / partial / missing / waived),
evidence, and the date verified. "We think it is on" is not evidence. A screenshot, export,
console report, or log entry is.

Mapping note: controls track CIS Controls v8.1 Implementation Group 1 closely. When a client,
insurer, or auditor asks for a CIS mapping, build it from this list rather than claiming
blanket alignment.

---

## 1. Identity and Access

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| MFA enforced for every user (the platform's tenant-wide MFA enforcement or conditional access policies) | T1 (waiver if declined) | Tenant MFA registration report; no users excluded without a documented reason | Registration report export |
| Legacy and basic authentication blocked (old mail protocols, SMTP AUTH unless a documented device needs it) | T1 | Sign-in logs show no legacy-protocol sign-ins; policy in place | Policy screenshot |
| Named admin accounts separate from daily accounts; no shared admin logins | T1 | Admin role membership review | Role export |
| Global/super admin count held to the minimum (recommended default: 2 to 4 including break-glass) | T1 | Role review | Role export |
| Client-owned break-glass admin exists, credentials sealed with the client, sign-ins alert {{COMPANY_NAME}} | T1 (inherited) | Account exists, excluded from lockout policies deliberately, alerting on | Documentation entry |
| Users cannot consent to third-party apps on their own; admin-consent workflow on | T1 | Tenant consent settings | Screenshot |
| Standard users are not local administrators on their computers | T1 | RMM report of local admin group membership | RMM report |
| Unique local admin password per machine, rotated (the operating system's built-in local admin password solution or your RMM's equivalent) | T1 | Policy applied fleet-wide | Policy and coverage report |
| Password policy: long passphrases, no forced periodic rotation without cause, banned common passwords, no reuse across work systems | T1 | Tenant password settings | Screenshot |
| Phishing-resistant MFA (security keys, passkeys, platform biometric sign-in) for admins and anyone who approves payments | T2 | Authentication methods report | Report export |
| Conditional access: block sign-ins from countries the client never operates in, require compliant devices for sensitive apps | T2 (requires the license tier that includes it) | Policy review | Policy export |
| Business password manager for staff | T2 | Deployment count versus headcount | Admin console report |

## 2. Email

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| SPF published, single record, within lookup limits | T1 | DNS lookup | Lookup output |
| DKIM signing enabled for every sending domain | T1 | Header check on a test message | Header |
| DMARC published; moving from p=none to quarantine or reject once reports are clean (target: enforcement within 90 days of onboarding) | T1 | DNS lookup; report review | Lookup and report summary |
| Automatic forwarding to external domains blocked by default; exceptions documented | T1 | Outbound policy | Screenshot |
| External-sender tagging on inbound mail | T1 | Test message | Screenshot |
| Anti-phishing, anti-malware, and safe-attachment settings at the platform's recommended level | T1 | Platform preset or security score items | Screenshot |
| Mailbox audit logging on | T1 | Tenant setting | Screenshot |
| Unused and shared mailboxes cannot sign in interactively | T1 | Account status review | Export |
| Advanced email threat protection (third-party or platform add-on) | T2 | Deployment | Console report |

## 3. Endpoints (Computers and Servers)

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| RMM agent on every managed device, reporting | T1 (inherited) | RMM device list versus asset inventory | Report |
| Endpoint protection (your platform, at the tier Setup Decision 1 sets) on every managed computer and server, tamper protection on, reporting | T1 (inherited) | Console coverage versus asset inventory | Coverage report |
| Full-disk encryption (the operating system's built-in encryption) on every laptop, desktops where practical; recovery keys escrowed | T1 | RMM or Mac MDM encryption report | Report |
| Host firewall on | T1 | RMM policy | Report |
| Screen lock after inactivity (recommended default: 15 minutes or less) | T1 | Policy | Report |
| Supported OS versions only; end-of-support devices have a replacement date or a waiver | T1 | RMM OS report | Report |
| Macs managed in your Mac device management (MDM) platform with the equivalent controls | T1 where Macs exist (inherited) | MDM inventory | Report |
| EDR capability and 24/7 managed detection and response | Not offered (shipped default, see Setup Decisions); scope case by case if a client or insurer requires it | n/a | n/a |
| Application allow-listing or blocking of unapproved software | T2 | Policy | Report |
| USB storage restricted | T2 | Policy | Report |

## 4. Patching and Software

The cadence is owned by msp-maintenance. The baseline adds:

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| OS patches current per msp-maintenance; compliance reported monthly | T1 (inherited) | RMM patch report | Report |
| Third-party apps (browsers, PDF readers, meeting clients, runtimes, etc.) patched where the RMM covers them; others tracked | T1 | RMM report | Report |
| Firmware on firewalls, switches, access points, and NAS current or on a documented schedule | T1 | Device versions versus vendor release | Documentation entry |
| Actively exploited vulnerabilities (CISA Known Exploited Vulnerabilities catalog) handled out-of-band | T1 (inherited) | Change log | Log entry |
| Software inventory kept; unauthorized or abandoned software removed | T1 | RMM software report | Report |

## 5. Backup and Recovery

The verification cadence is owned by msp-maintenance. The baseline adds:

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| 3-2-1: three copies, two media, one offsite | T1 | Backup design in documentation | Documentation |
| At least one copy immutable or offline, unreachable with the client's or {{COMPANY_NAME}}'s normal admin credentials | T1 (recommended default) | Platform setting | Screenshot |
| Cloud email and productivity data (mail, cloud file storage, team sites and shared drives, team chat) backed up by a third-party backup, not only the platform's recycle bin | T1 | Backup console | Report |
| Servers and line-of-business databases backed up | T1 | Backup console | Report |
| Backup console on its own credentials with MFA, not tied to the client's directory | T1 | Access review | Screenshot |
| Monthly test restore logged (inherited cadence) | T1 | Restore log | Log |
| Recovery time and recovery point stated in plain English and known to the owner | T1 | QBR or assessment summary | Documentation |

## 6. Network and Remote Access

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| Business-class firewall at every site, under {{COMPANY_NAME}} management | T1 | Documentation | Network map |
| No RDP, SMB, or device admin interfaces exposed to the internet | T1 | External port scan of the client's public IPs | Scan output |
| Default passwords changed on every network device, printer, camera, and NAS | T1 | Device review | Documentation |
| Remote access only through an approved path: ZTNA if sold, otherwise MFA-protected VPN | T1 | Firewall and access review | Documentation |
| Wi-Fi: WPA2 or WPA3 with a strong key; guest network isolated from business devices | T1 | Configuration review | Screenshot |
| UPnP off on the firewall | T1 | Configuration review | Screenshot |
| DNS filtering | T2 | Deployment | Report |
| Cameras, IoT, and printers on a separate network segment | T2 | Configuration | Network map |

## 7. Data Protection

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| Know where sensitive data lives (file shares, cloud drives, the line-of-business app) | T1 | Assessment interview plus review | Documentation |
| External sharing in cloud file storage set to the least that works (no "anyone with the link" by default) | T1 | Tenant sharing settings | Screenshot |
| Access to sensitive shares limited by role, reviewed yearly | T1 | Permission review | Export |
| Data loss prevention and sensitivity labels | T2 | Policy | Export |

## 8. Mobile Devices

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| Company phones and tablets enrolled in MDM with passcode, encryption, and remote wipe | T1 where mobile device management is sold (inherited, msp-pricing) | MDM inventory | Report |
| Personal devices reaching company email use app protection (company data only, wipeable) | T2 | Policy | Screenshot |

## 9. People

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| Security orientation for new staff at the help desk announcement and new hires thereafter | T1 (recommended default) | Onboarding record | Log |
| {{COMPANY_NAME}} security advisories to the client when a relevant threat is active | T1 | Sent advisories | msp-client-comms record |
| Staff know how to report something suspicious ({{SUPPORT_EMAIL}} or {{PHONE}}) and that reporting fast is never punished | T1 | Help desk announcement | Record |
| Payment and banking changes verified by a phone call to a known number, never by email alone | T1 (client process; {{COMPANY_NAME}} recommends and records) | Owner confirms | Assessment note |
| Formal training platform with phishing simulations | T2 | Platform report | Report |

## 10. Offboarding a Client's Staff Member

Same day as the departure (or the moment of an involuntary termination):

1. Block sign-in and revoke all active sessions and refresh tokens.
2. Reset the password and remove MFA methods.
3. Remove from admin roles, groups, and shared mailbox permissions.
4. Convert the mailbox to shared or set forwarding to the manager if the client asks (inside
   the organization only); reclaim the license per msp-pricing.
5. Transfer cloud file storage ownership to the manager.
6. Retire or wipe company data from mobile devices; collect hardware.
7. Remove from line-of-business apps and vendor portals {{COMPANY_NAME}} administers; flag the
   ones the client administers.
8. Rotate any shared credentials the person knew (Wi-Fi, shared accounts, alarm codes are
   the client's call).
9. Log every step in the ticket.

## 11. Logging and Monitoring

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| The email and productivity platform's unified audit logs on, retained per license | T1 | Tenant setting | Screenshot |
| Alerts for risky sign-ins, new admin role assignments, new inbox forwarding rules, and mass file deletion reach {{COMPANY_NAME}} | T1 | Alert policy review | Screenshot |
| Endpoint protection and backup alerts reach {{COMPANY_NAME}} and map into msp-maintenance triage | T1 (inherited) | Alert routing | Configuration |
| Firewall logs retained where the device allows | T1 | Device setting | Screenshot |
| Centralized log collection or SIEM | Not offered (shipped default, see Setup Decision 1); scope case by case if a client or insurer requires it | n/a | n/a |

## 12. Documentation and Governance

| Control | Tier | Verify | Evidence |
|---|---|---|---|
| Asset inventory (hardware and software) current | T1 | Documentation versus RMM | Documentation |
| Network map, admin account list, vendor contacts, and this baseline's status recorded | T1 (inherited in part) | Documentation review | Documentation |
| Last assessment date and open findings recorded | T1 | Documentation | Documentation |
| Declined controls have signed waivers on file | T1 | Waiver file | Waivers |
| Client has a written incident contact list (who at the client decides, their insurer, their attorney) | T1 | Documentation | Documentation |
| Written information security policy for the client | T2 (T1 in some regulated verticals, see compliance-overlays.md) | Policy document | Document |
