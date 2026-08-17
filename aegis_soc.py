import os
import sys
import time
import json
import random
from datetime import datetime, timezone

# ANSI Color & Styling Tokens
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[38;5;196m"
GREEN   = "\033[38;5;48m"
BLUE    = "\033[38;5;39m"
CYAN    = "\033[38;5;51m"
AMBER   = "\033[38;5;214m"
MAGENTA = "\033[38;5;201m"
GRAY    = "\033[38;5;244m"

BANNER = f"""{CYAN}{BOLD}
   █████╗ ███████╗ ██████╗ ██╗███████╗      ███████╗ ██████╗  ██████╗
  ██╔══██╗██╔════╝██╔════╝ ██║██╔════╝      ██╔════╝██╔═══██╗██╔════╝
  ███████║█████╗  ██║  ███╗██║███████╗█████╗███████╗██║   ██║██║     
  ██╔══██║██╔══╝  ██║   ██║██║╚════██║╚════╝╚════██║██║   ██║██║     
  ██║  ██║███████╗╚██████╔╝██║███████║      ███████║╚██████╔╝╚██████╗
  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝      ╚══════╝ ╚═════╝  ╚═════╝
{RESET}{DIM}  [ Next-Generation Autonomous Blue Team Incident Operations Console ]{RESET}
"""

class AegisSOCEngine:
    def __init__(self, config_path="config.json", threat_path="threat_feed.json"):
        if not os.path.exists(config_path) or not os.path.exists(threat_path):
            print(f"{RED}[-] Error: Missing config.json or threat_feed.json{RESET}")
            sys.exit(1)

        with open(config_path, "r") as f:
            self.config = json.load(f)

        with open(threat_path, "r") as f:
            self.threat_intel = json.load(f)

        self.ioc_list = self.threat_intel.get("ioc_blacklist", [])
        self.endpoints = self.threat_intel.get("monitored_endpoints", [])
        self.log_file = self.config.get("log_output", "soc_audit_trail.log")

    def print_status_bar(self, text, state="RUNNING"):
        print(f"\r  {CYAN}▸{RESET} {text:<45} [{BOLD}{GREEN}{state}{RESET}]", end="", flush=True)
        time.sleep(0.3)
        print()

    def boot_sequence(self):
        print(BANNER)
        print(f"{BOLD}Initializing Security Telemetry Matrix...{RESET}\n")
        self.print_status_bar("Loading MITRE ATT&CK Knowledge Base...", "LOADED")
        self.print_status_bar("Connecting to Global Threat Intel Feeds...", "CONNECTED")
        self.print_status_bar("Hooking Kernel EDR File Integrity Watchers...", "ACTIVE")
        self.print_status_bar(f"Enforcing Host Containment Policies ({len(self.endpoints)} Endpoints)...", "ONLINE")
        print("\n" + "=" * 80 + "\n")

    def run_live_console(self):
        self.boot_sequence()
        max_events = self.config.get("max_events_per_session", 5)

        print(f"{BOLD}{GREEN}● LIVE INCIDENT MONITOR ENGAGED{RESET} {DIM}(Streaming Event Ingestion){RESET}\n")

        for event_num in range(1, max_events + 1):
            time.sleep(self.config.get("telemetry_stream_speed_seconds", 1.2))
            
            # Select random target and threat data
            endpoint = random.choice(self.endpoints)
            ioc = random.choice(self.ioc_list)
            timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

            print(f"{AMBER}{'─' * 80}{RESET}")
            print(f"{BOLD}{RED}[🚨 INCIDENT #{event_num:03d} DETECTED]{RESET} at {DIM}{timestamp}{RESET}")
            print(f"  {BOLD}Target Asset:{RESET}       {endpoint['hostname']} ({endpoint['ip']}) - {endpoint['role']}")
            print(f"  {BOLD}External Threat IP:{RESET} {RED}{ioc['ip']}{RESET}")
            print(f"  {BOLD}Attributed Actor:{RESET}   {MAGENTA}{ioc['threat_actor']}{RESET} (Confidence: {ioc['confidence']})")
            print(f"  {BOLD}Classification:{RESET}     {ioc['threat_type']}")
            print(f"  {BOLD}MITRE ATT&CK ID:{RESET}    {CYAN}{ioc['mitre_id']}{RESET}")

            # Simulated automated containment action
            if self.config.get("auto_containment", True):
                time.sleep(0.4)
                print(f"\n  {BOLD}{BLUE}[⚡ AUTONOMOUS CONTAINMENT ACTION]{RESET}")
                print(f"  └── Host Firewall Rule Injected: {RED}DROP IN/OUT from {ioc['ip']}{RESET}")
                print(f"  └── Network Interface for {endpoint['hostname']}: {GREEN}ISOLATED (VLAN 999 Quarantine){RESET}")
                print(f"  └── SOC Audit Status: {GREEN}TRIAGED & MITIGATED{RESET}")

            # Write event to audit log
            with open(self.log_file, "a") as log:
                log.write(f"[{timestamp}] INCIDENT #{event_num:03d} | TARGET={endpoint['hostname']} | IOC={ioc['ip']} | ACTOR={ioc['threat_actor']} | MITRE={ioc['mitre_id']} | STATUS=CONTAINED\n")

        print(f"\n{AMBER}{'─' * 80}{RESET}")
        print(f"{GREEN}{BOLD}[✓] SIMULATION RUN COMPLETE:{RESET} All high-severity incidents successfully identified and isolated.")
        print(f"Audit log saved to: {BOLD}{self.log_file}{RESET}\n")

if __name__ == "__main__":
    engine = AegisSOCEngine()
    engine.run_live_console()
