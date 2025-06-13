-- Compute traffic baselines per destination IP
CREATE OR REPLACE TABLE cybersec.gold.traffic_baseline AS
SELECT
  IPV4_DST_ADDR AS dest_ip,
  AVG(IN_BYTES) AS avg_in_bytes,
  AVG(OUT_BYTES) AS avg_out_bytes
FROM cybersec.silver.netflow_logs
GROUP BY IPV4_DST_ADDR;
