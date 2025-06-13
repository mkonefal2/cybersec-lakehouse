-- Aggregate threat indicators from cleaned logs
CREATE OR REPLACE TABLE cybersec.gold.threat_indicator AS
SELECT
  IPV4_DST_ADDR AS dest_ip,
  COUNT(*) AS hit_count,
  MAX(ANOMALY) AS max_anomaly
FROM cybersec.silver.netflow_logs
GROUP BY IPV4_DST_ADDR;
