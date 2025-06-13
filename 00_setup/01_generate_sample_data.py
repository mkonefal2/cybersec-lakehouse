import argparse
import pandas as pd
import numpy as np


def generate_firewall_logs(num_records: int) -> pd.DataFrame:
    """Create sample firewall log records."""
    df = pd.DataFrame({
        "Source Port": np.random.randint(1024, 65535, num_records),
        "Destination Port": np.random.randint(1024, 65535, num_records),
        "NAT Source Port": np.random.randint(1024, 65535, num_records),
        "NAT Destination Port": np.random.randint(1024, 65535, num_records),
        "Action": np.random.choice(["allow", "deny"], num_records),
        "Bytes": np.random.randint(0, 1000000, num_records),
        "Bytes Sent": np.random.randint(0, 500000, num_records),
        "Bytes Received": np.random.randint(0, 500000, num_records),
        "Packets": np.random.randint(1, 1000, num_records),
        "Elapsed Time (sec)": np.random.randint(1, 3600, num_records),
        "pkts_sent": np.random.randint(1, 1000, num_records),
        "pkts_received": np.random.randint(1, 1000, num_records),
    })
    return df


def generate_netflow_logs(num_records: int) -> pd.DataFrame:
    """Create sample NetFlow v9 records."""
    df = pd.DataFrame({
        "FLOW_ID": np.arange(num_records).astype(str),
        "PROTOCOL_MAP": np.random.choice(["tcp", "udp", "icmp"], num_records),
        "L4_SRC_PORT": np.random.randint(1024, 65535, num_records),
        "IPV4_SRC_ADDR": [f"192.168.1.{i%255}" for i in range(num_records)],
        "L4_DST_PORT": np.random.randint(1024, 65535, num_records),
        "IPV4_DST_ADDR": [f"10.0.0.{i%255}" for i in range(num_records)],
        "FIRST_SWITCHED": np.random.randint(1_600_000_000, 1_700_000_000, num_records),
        "FLOW_DURATION_MILLISECONDS": np.random.randint(1, 10000, num_records),
        "LAST_SWITCHED": np.random.randint(1_600_000_000, 1_700_000_000, num_records),
        "PROTOCOL": np.random.randint(0, 255, num_records),
        "TCP_FLAGS": np.random.randint(0, 255, num_records),
        "TCP_WIN_MAX_IN": np.random.randint(0, 65535, num_records),
        "TCP_WIN_MAX_OUT": np.random.randint(0, 65535, num_records),
        "TCP_WIN_MIN_IN": np.random.randint(0, 65535, num_records),
        "TCP_WIN_MIN_OUT": np.random.randint(0, 65535, num_records),
        "TCP_WIN_MSS_IN": np.random.randint(0, 65535, num_records),
        "TCP_WIN_SCALE_IN": np.random.randint(0, 255, num_records),
        "TCP_WIN_SCALE_OUT": np.random.randint(0, 255, num_records),
        "SRC_TOS": np.random.randint(0, 255, num_records),
        "DST_TOS": np.random.randint(0, 255, num_records),
        "TOTAL_FLOWS_EXP": np.random.randint(0, 1000, num_records),
        "MIN_IP_PKT_LEN": np.random.randint(0, 1500, num_records),
        "MAX_IP_PKT_LEN": np.random.randint(0, 1500, num_records),
        "TOTAL_PKTS_EXP": np.random.randint(0, 10000, num_records),
        "TOTAL_BYTES_EXP": np.random.randint(0, 1000000, num_records),
        "IN_BYTES": np.random.randint(0, 1000000, num_records),
        "IN_PKTS": np.random.randint(0, 10000, num_records),
        "OUT_BYTES": np.random.randint(0, 1000000, num_records),
        "OUT_PKTS": np.random.randint(0, 10000, num_records),
        "ANALYSIS_TIMESTAMP": np.random.randint(1_600_000_000, 1_700_000_000, num_records),
        "ANOMALY": np.random.random(num_records),
        "ID": np.arange(num_records),
    })
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate sample cyber security datasets")
    parser.add_argument("--output", required=True, help="Output directory for CSV files")
    parser.add_argument("--records", type=int, default=1000, help="Number of records per dataset")
    args = parser.parse_args()

    out = args.output.rstrip("/")
    records = args.records

    fw_df = generate_firewall_logs(records)
    nf_df = generate_netflow_logs(records)

    fw_df.to_csv(f"{out}/firewall_logs.csv", index=False)
    nf_df.to_csv(f"{out}/netflow_logs.csv", index=False)
    print(f"Sample data written to {out}")
