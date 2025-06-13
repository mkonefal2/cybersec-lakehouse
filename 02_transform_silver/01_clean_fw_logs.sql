-- Clean and normalize firewall logs into Silver layer
CREATE OR REPLACE TABLE cybersec.silver.firewall_logs_clean AS
SELECT
  CAST(`Source Port` AS INT) AS src_port,
  CAST(`Destination Port` AS INT) AS dest_port,
  CAST(`Action` AS STRING) AS action,
  CAST(`Bytes` AS INT) AS bytes,
  CAST(`Elapsed Time (sec)` AS INT) AS duration_sec,
  pkts_sent,
  pkts_received
FROM cybersec.bronze.firewall_logs;
