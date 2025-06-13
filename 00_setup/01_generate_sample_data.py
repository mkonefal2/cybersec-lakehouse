import csv
import os
import random

FIREWALL_FIELDS = [
    "Source Port",
    "Destination Port",
    "NAT Source Port",
    "NAT Destination Port",
    "Action",
    "Bytes",
    "Bytes Sent",
    "Bytes Received",
    "Packets",
    "Elapsed Time (sec)",
    "pkts_sent",
    "pkts_received",
]

NETFLOW_FIELDS = [
    "FLOW_ID",
    "PROTOCOL_MAP",
    "L4_SRC_PORT",
    "IPV4_SRC_ADDR",
    "L4_DST_PORT",
    "IPV4_DST_ADDR",
    "FIRST_SWITCHED",
    "FLOW_DURATION_MILLISECONDS",
    "LAST_SWITCHED",
    "PROTOCOL",
    "TCP_FLAGS",
    "TCP_WIN_MAX_IN",
    "TCP_WIN_MAX_OUT",
    "TCP_WIN_MIN_IN",
    "TCP_WIN_MIN_OUT",
    "TCP_WIN_MSS_IN",
    "TCP_WIN_SCALE_IN",
    "TCP_WIN_SCALE_OUT",
    "SRC_TOS",
    "DST_TOS",
    "TOTAL_FLOWS_EXP",
    "MIN_IP_PKT_LEN",
    "MAX_IP_PKT_LEN",
    "TOTAL_PKTS_EXP",
    "TOTAL_BYTES_EXP",
    "IN_BYTES",
    "IN_PKTS",
    "OUT_BYTES",
    "OUT_PKTS",
    "ANALYSIS_TIMESTAMP",
    "ANOMALY",
    "ID",
]

def generate_firewall_logs(path: str, rows: int = 20) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    actions = ["allow", "deny"]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(FIREWALL_FIELDS)
        for _ in range(rows):
            writer.writerow([
                random.randint(1024, 65535),
                random.randint(1, 65535),
                random.randint(1024, 65535),
                random.randint(1, 65535),
                random.choice(actions),
                random.randint(100, 100_000),
                random.randint(50, 50_000),
                random.randint(50, 50_000),
                random.randint(1, 1_000),
                random.randint(1, 10_000),
                random.randint(1, 1_000),
                random.randint(1, 1_000),
            ])

def generate_netflow_logs(path: str, rows: int = 20) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    protocols = ["tcp", "udp", "icmp"]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(NETFLOW_FIELDS)
        for i in range(rows):
            writer.writerow([
                f"flow_{i}",
                random.choice(protocols),
                random.randint(1024, 65535),
                f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
                random.randint(1, 65535),
                f"10.0.{random.randint(0,255)}.{random.randint(0,255)}",
                random.randint(1_600_000_000, 1_700_000_000),
                random.randint(1, 100_000),
                random.randint(1_600_000_000, 1_700_000_000),
                random.randint(1, 255),
                random.randint(0, 255),
                random.randint(0, 65_535),
                random.randint(0, 65_535),
                random.randint(0, 65_535),
                random.randint(0, 65_535),
                random.randint(0, 65_535),
                random.randint(0, 9),
                random.randint(0, 9),
                random.randint(0, 9),
                random.randint(0, 9),
                random.randint(1, 1_000),
                random.randint(1, 1_000),
                random.randint(1, 1_500),
                random.randint(1, 1_000),
                random.randint(1_000, 1_000_000),
                random.randint(100, 100_000),
                random.randint(1, 1_000),
                random.randint(100, 100_000),
                random.randint(1, 1_000),
                random.randint(1_600_000_000, 1_700_000_000),
                round(random.random(), 2),
                i,
            ])

if __name__ == "__main__":
    generate_firewall_logs("data/firewall_logs.csv")
    generate_netflow_logs("data/netflow_logs.csv")
