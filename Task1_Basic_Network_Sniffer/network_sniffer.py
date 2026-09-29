#!/usr/bin/env python3
"""Basic Network Sniffer - CodeAlpha Cyber Security Internship.
Use only on systems/networks you own or are authorized to monitor.
"""
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_handler(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not packet.haslayer(IP):
        return
    ip = packet[IP]
    protocol = "OTHER"
    details = f"{ip.src} -> {ip.dst}"
    if packet.haslayer(TCP):
        protocol = "TCP"
        details = f"{ip.src}:{packet[TCP].sport} -> {ip.dst}:{packet[TCP].dport}"
    elif packet.haslayer(UDP):
        protocol = "UDP"
        details = f"{ip.src}:{packet[UDP].sport} -> {ip.dst}:{packet[UDP].dport}"
    elif packet.haslayer(ICMP):
        protocol = "ICMP"
    payload = ""
    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)[:80].hex(" ")
    print(f"[{timestamp}] {protocol:<5} {details}")
    if payload:
        print(f"  Payload (first 80 bytes): {payload}")

def main():
    print("Basic Network Sniffer")
    print("Press Ctrl+C to stop.")
    sniff(filter="ip", prn=packet_handler, store=False)

if __name__ == "__main__":
    main()
