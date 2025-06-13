-- Unity Catalog setup for cyber security lakehouse
CREATE CATALOG IF NOT EXISTS cybersec;
USE CATALOG cybersec;

CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;

-- Sample bronze tables
CREATE TABLE IF NOT EXISTS bronze.firewall_logs (
    Source_Port INT,
    Destination_Port INT,
    NAT_Source_Port INT,
    NAT_Destination_Port INT,
    Action STRING,
    Bytes INT,
    Bytes_Sent INT,
    Bytes_Received INT,
    Packets INT,
    Elapsed_Time_sec INT,
    pkts_sent INT,
    pkts_received INT
);

CREATE TABLE IF NOT EXISTS bronze.netflow_logs (
    FLOW_ID STRING,
    PROTOCOL_MAP STRING,
    L4_SRC_PORT INT,
    IPV4_SRC_ADDR STRING,
    L4_DST_PORT INT,
    IPV4_DST_ADDR STRING,
    FIRST_SWITCHED BIGINT,
    FLOW_DURATION_MILLISECONDS INT,
    LAST_SWITCHED BIGINT,
    PROTOCOL INT,
    TCP_FLAGS INT,
    TCP_WIN_MAX_IN INT,
    TCP_WIN_MAX_OUT INT,
    TCP_WIN_MIN_IN INT,
    TCP_WIN_MIN_OUT INT,
    TCP_WIN_MSS_IN INT,
    TCP_WIN_SCALE_IN INT,
    TCP_WIN_SCALE_OUT INT,
    SRC_TOS INT,
    DST_TOS INT,
    TOTAL_FLOWS_EXP INT,
    MIN_IP_PKT_LEN INT,
    MAX_IP_PKT_LEN INT,
    TOTAL_PKTS_EXP INT,
    TOTAL_BYTES_EXP INT,
    IN_BYTES INT,
    IN_PKTS INT,
    OUT_BYTES INT,
    OUT_PKTS INT,
    ANALYSIS_TIMESTAMP BIGINT,
    ANOMALY DOUBLE,
    ID INT
);
