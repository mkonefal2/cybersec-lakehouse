"""Streaming ingestion of NetFlow logs using PySpark Structured Streaming."""
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, FloatType
)

NETFLOW_SCHEMA = StructType([
    StructField("FLOW_ID", StringType(), True),
    StructField("PROTOCOL_MAP", StringType(), True),
    StructField("L4_SRC_PORT", IntegerType(), True),
    StructField("IPV4_SRC_ADDR", StringType(), True),
    StructField("L4_DST_PORT", IntegerType(), True),
    StructField("IPV4_DST_ADDR", StringType(), True),
    StructField("FIRST_SWITCHED", IntegerType(), True),
    StructField("FLOW_DURATION_MILLISECONDS", IntegerType(), True),
    StructField("LAST_SWITCHED", IntegerType(), True),
    StructField("PROTOCOL", IntegerType(), True),
    StructField("TCP_FLAGS", IntegerType(), True),
    StructField("TCP_WIN_MAX_IN", IntegerType(), True),
    StructField("TCP_WIN_MAX_OUT", IntegerType(), True),
    StructField("TCP_WIN_MIN_IN", IntegerType(), True),
    StructField("TCP_WIN_MIN_OUT", IntegerType(), True),
    StructField("TCP_WIN_MSS_IN", IntegerType(), True),
    StructField("TCP_WIN_SCALE_IN", IntegerType(), True),
    StructField("TCP_WIN_SCALE_OUT", IntegerType(), True),
    StructField("SRC_TOS", IntegerType(), True),
    StructField("DST_TOS", IntegerType(), True),
    StructField("TOTAL_FLOWS_EXP", IntegerType(), True),
    StructField("MIN_IP_PKT_LEN", IntegerType(), True),
    StructField("MAX_IP_PKT_LEN", IntegerType(), True),
    StructField("TOTAL_PKTS_EXP", IntegerType(), True),
    StructField("TOTAL_BYTES_EXP", IntegerType(), True),
    StructField("IN_BYTES", IntegerType(), True),
    StructField("IN_PKTS", IntegerType(), True),
    StructField("OUT_BYTES", IntegerType(), True),
    StructField("OUT_PKTS", IntegerType(), True),
    StructField("ANALYSIS_TIMESTAMP", IntegerType(), True),
    StructField("ANOMALY", FloatType(), True),
    StructField("ID", IntegerType(), True),
])

def main(input_path: str, output_path: str) -> None:
    spark = SparkSession.builder.appName("netflow_stream_ingest").getOrCreate()

    df = (
        spark.readStream.option("header", True)
        .schema(NETFLOW_SCHEMA)
        .csv(input_path)
    )

    query = (
        df.writeStream.format("delta")
        .outputMode("append")
        .option("checkpointLocation", f"{output_path}_checkpoint")
        .start(output_path)
    )
    query.awaitTermination()

if __name__ == "__main__":
    main("data/netflow_logs.csv", "delta/bronze/netflow_logs")
