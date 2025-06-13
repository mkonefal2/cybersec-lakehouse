-- Unity Catalog object creation for Cyber Security Lakehouse
CREATE CATALOG IF NOT EXISTS cybersec;

CREATE SCHEMA IF NOT EXISTS cybersec.bronze;
CREATE SCHEMA IF NOT EXISTS cybersec.silver;
CREATE SCHEMA IF NOT EXISTS cybersec.gold;

-- Bronze tables
CREATE TABLE IF NOT EXISTS cybersec.bronze.firewall_logs (
  source_port INT,
  destination_port INT,
  nat_source_port INT,
  nat_destination_port INT,
  action STRING,
  bytes INT,
  bytes_sent INT,
  bytes_received INT,
  packets INT,
  elapsed_time_sec INT,
  pkts_sent INT,
  pkts_received INT
) USING DELTA;

CREATE TABLE IF NOT EXISTS cybersec.bronze.netflow_logs (
  flow_id STRING,
  protocol_map STRING,
  l4_src_port INT,
  ipv4_src_addr STRING,
  l4_dst_port INT,
  ipv4_dst_addr STRING,
  first_switched INT,
  flow_duration_milliseconds INT,
  last_switched INT,
  protocol INT,
  tcp_flags INT,
  in_bytes INT,
  in_pkts INT,
  out_bytes INT,
  out_pkts INT,
  analysis_timestamp INT,
  anomaly FLOAT,
  id INT
) USING DELTA;
