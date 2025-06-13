-- Clean firewall logs and cast fields
CREATE OR REPLACE TABLE cybersec.silver.firewall_logs_clean AS
SELECT
  CAST(`Source Port` AS INT) AS source_port,
  CAST(`Destination Port` AS INT) AS dest_port,
  CAST(`NAT Source Port` AS INT) AS nat_source_port,
  CAST(`NAT Destination Port` AS INT) AS nat_dest_port,
  Action AS action,
  Bytes AS bytes,
  `Bytes Sent` AS bytes_sent,
  `Bytes Received` AS bytes_received,
  Packets AS packets,
  `Elapsed Time (sec)` AS duration_sec,
  pkts_sent,
  pkts_received
FROM cybersec.bronze.firewall_logs;
