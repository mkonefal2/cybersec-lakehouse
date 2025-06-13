# Data Source Reference for Cyber Security Lakehouse

This repository utilizes two core input files for parallel data pipelines in the Databricks Lakehouse architecture. Each file is used in a distinct pipeline (batch or streaming). They are not directly joinable but can be referenced by shared dimensions (e.g., IP, port, timestamp) in advanced analytics.

---

## 1. Firewall Log Dataset (`firewall_logs.csv`)

**Purpose:**  
- Used exclusively in batch ingestion pipeline for the processing and analysis of firewall session logs.
- Suitable for ETL, compliance reporting, and historical traffic audits.

**Schema (columns):**

| Column               | Type    | Description                           |
|----------------------|---------|---------------------------------------|
| Source Port          | int     | Source port number                    |
| Destination Port     | int     | Destination port number               |
| NAT Source Port      | int     | NAT translated source port            |
| NAT Destination Port | int     | NAT translated destination port       |
| Action               | string  | Connection action (allow/deny)        |
| Bytes                | int     | Total bytes transferred               |
| Bytes Sent           | int     | Bytes sent from source                |
| Bytes Received       | int     | Bytes received by destination         |
| Packets              | int     | Number of packets                     |
| Elapsed Time (sec)   | int     | Session duration in seconds           |
| pkts_sent            | int     | Packets sent                          |
| pkts_received        | int     | Packets received                      |

---

## 2. NetFlow Dataset (`netflow_logs.csv`)

**Purpose:**  
- Used as a synthetic input for the streaming pipeline.
- The file is split into smaller chunks and delivered incrementally to simulate real-time ingestion (streaming), enabling event-driven transformations and anomaly detection.

**Schema (columns):**

| Column                   | Type    | Description                                    |
|--------------------------|---------|------------------------------------------------|
| FLOW_ID                  | string  | Unique flow identifier                         |
| PROTOCOL_MAP             | string  | Protocol (tcp/udp/icmp)                        |
| L4_SRC_PORT              | int     | Layer 4 source port                            |
| IPV4_SRC_ADDR            | string  | Source IPv4 address                            |
| L4_DST_PORT              | int     | Layer 4 destination port                       |
| IPV4_DST_ADDR            | string  | Destination IPv4 address                       |
| FIRST_SWITCHED           | int     | Flow start timestamp (epoch)                   |
| FLOW_DURATION_MILLISECONDS | int   | Flow duration in ms                            |
| LAST_SWITCHED            | int     | Flow end timestamp (epoch)                     |
| PROTOCOL                 | int     | IP protocol number                             |
| TCP_FLAGS                | int     | TCP flag aggregation                           |
| TCP_WIN_MAX_IN           | int     | Max TCP window size inbound                    |
| TCP_WIN_MAX_OUT          | int     | Max TCP window size outbound                   |
| TCP_WIN_MIN_IN           | int     | Min TCP window size inbound                    |
| TCP_WIN_MIN_OUT          | int     | Min TCP window size outbound                   |
| TCP_WIN_MSS_IN           | int     | TCP MSS inbound                                |
| TCP_WIN_SCALE_IN         | int     | TCP window scale inbound                       |
| TCP_WIN_SCALE_OUT        | int     | TCP window scale outbound                      |
| SRC_TOS                  | int     | Source Type of Service                         |
| DST_TOS                  | int     | Destination Type of Service                    |
| TOTAL_FLOWS_EXP          | int     | Expected number of flows                       |
| MIN_IP_PKT_LEN           | int     | Minimum IP packet length                       |
| MAX_IP_PKT_LEN           | int     | Maximum IP packet length                       |
| TOTAL_PKTS_EXP           | int     | Expected total number of packets               |
| TOTAL_BYTES_EXP          | int     | Expected total number of bytes                 |
| IN_BYTES                 | int     | Bytes inbound                                  |
| IN_PKTS                  | int     | Packets inbound                                |
| OUT_BYTES                | int     | Bytes outbound                                 |
| OUT_PKTS                 | int     | Packets outbound                               |
| ANALYSIS_TIMESTAMP       | int     | Analysis timestamp (epoch)                     |
| ANOMALY                  | float   | Anomaly score or flag                          |
| ID                       | int     | Row index or identifier                        |

---

**Important for Codex/LLM:**  
- Do not attempt to join these files directly; treat them as **two separate, parallel ingestion pipelines**.  
- Use the schemas above for all data import and transformation steps.
- For streaming simulation, `netflow_logs.csv` is partitioned and delivered incrementally.

---
