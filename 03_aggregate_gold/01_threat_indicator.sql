-- Aggregate threat indicators from cleaned NetFlow data
CREATE OR REPLACE TABLE cybersec.gold.threat_indicator AS
SELECT
  IPV4_DST_ADDR AS dest_ip,
  COUNT(*) AS total_flows,
  SUM(CASE WHEN ANOMALY > 0.5 THEN 1 ELSE 0 END) AS anomaly_count
FROM cybersec.silver.netflow_logs
GROUP BY IPV4_DST_ADDR;
