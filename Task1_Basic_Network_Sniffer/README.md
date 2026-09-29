# Task 1 — Basic Network Sniffer

A Python/Scapy packet sniffer that captures authorized IP traffic and displays source/destination IPs, protocols, ports and a small hexadecimal payload preview.

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

Run with administrator/root privileges where required:
```bash
python network_sniffer.py
```

## Expected output
```text
[2026-09-29 14:00:00] TCP   192.168.1.10:52144 -> 142.250.72.14:443
[2026-09-29 14:00:01] UDP   192.168.1.10:5353 -> 224.0.0.251:5353
[2026-09-29 14:00:02] ICMP  192.168.1.10 -> 192.168.1.1
```

The example is illustrative. Replace it with your own authorized lab output/screenshot before submission.

## Ethics
Capture traffic only on systems/networks you own or have explicit permission to monitor.
