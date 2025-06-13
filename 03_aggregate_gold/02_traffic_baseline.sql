-- Baseline traffic metrics per destination IP and hour
CREATE OR REPLACE TABLE cybersec.gold.traffic_baseline AS
SELECT
  IPV4_DST_ADDR AS dest_ip,
  window(TO_TIMESTAMP(FIRST_SWITCHED), '1 hour') AS time_window,
  AVG(FLOW_DURATION_MILLISECONDS) AS avg_duration_ms,
  SUM(IN_BYTES + OUT_BYTES) AS total_bytes
FROM cybersec.silver.netflow_logs
GROUP BY IPV4_DST_ADDR, window(TO_TIMESTAMP(FIRST_SWITCHED), '1 hour');
