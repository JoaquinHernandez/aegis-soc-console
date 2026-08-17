# aegis-soc-console
# 🛡️ AEGIS-SOC: Next-Gen Autonomous Security Operations Console

A lightweight, high-impact Blue Team incident detection and autonomous containment simulator designed to parse streaming threat telemetry, correlate against real-world MITRE ATT&CK indicators, and trigger automated quarantine playbooks.

---

## ✨ Features
- **Interactive Cyberpunk TUI**: Richly styled terminal operations dashboard with live status indicators and real-time event streaming.
- **Threat Intelligence Correlation**: Maps incoming attacker IP infrastructure directly to known Advanced Persistent Threat (APT) groups (e.g., APT29, Lazarus, FIN7).
- **MITRE ATT&CK Tagging**: Automatically tags security incidents with technique identifiers (e.g., `T1071`, `T1486`).
- **Autonomous Playbook Containment**: Simulates immediate zero-trust host isolation and dynamic firewall blocking.
- **Zero Third-Party Dependencies**: Runs purely on Python standard libraries with zero installation friction.

---

## 🚀 Quick Start
```bash
python3 aegis_soc.py
