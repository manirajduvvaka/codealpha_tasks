# Task 4 — Network Intrusion Detection System

A defensive Suricata-based NIDS configuration for an authorized lab network.

## Included
- `suricata/local.rules`: custom rules for ICMP, TCP SYN traffic and SSH connection attempts.
- `suricata/suricata.yaml.example`: configuration notes.
- `sample_logs/eve.json.example`: illustrative alert records.

## Run in an authorized lab
1. Install Suricata using your operating system package manager.
2. Identify the interface connected to your lab network.
3. Add/adapt `local.rules` in the Suricata rules directory.
4. Enable the rules in Suricata configuration.
5. Start Suricata in IDS mode and review `eve.json`.
6. Generate only benign test traffic in your own lab and verify alerts.

## Important
Sample alert data is illustrative, not a claim of real attack traffic. Do not deploy blocking or automated response rules on production without testing and change control.
