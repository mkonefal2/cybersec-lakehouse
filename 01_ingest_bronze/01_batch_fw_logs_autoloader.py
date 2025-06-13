"""Batch ingestion of firewall logs using Auto Loader-like logic."""
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType
)

FIREWALL_SCHEMA = StructType([
    StructField("Source Port", IntegerType(), True),
    StructField("Destination Port", IntegerType(), True),
    StructField("NAT Source Port", IntegerType(), True),
    StructField("NAT Destination Port", IntegerType(), True),
    StructField("Action", StringType(), True),
    StructField("Bytes", IntegerType(), True),
    StructField("Bytes Sent", IntegerType(), True),
    StructField("Bytes Received", IntegerType(), True),
    StructField("Packets", IntegerType(), True),
    StructField("Elapsed Time (sec)", IntegerType(), True),
    StructField("pkts_sent", IntegerType(), True),
    StructField("pkts_received", IntegerType(), True),
])

def main(input_path: str, output_path: str) -> None:
    spark = SparkSession.builder.appName("firewall_batch_ingest").getOrCreate()
    df = spark.read.option("header", True).schema(FIREWALL_SCHEMA).csv(input_path)
    df.write.mode("overwrite").format("delta").save(output_path)

if __name__ == "__main__":
    main("data/firewall_logs.csv", "delta/bronze/firewall_logs")
