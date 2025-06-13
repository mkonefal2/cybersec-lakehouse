from pyspark.sql import SparkSession
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: stream_netflow_autoloader.py <input_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    spark = SparkSession.builder.appName("StreamNetflowIngestion").getOrCreate()

    df = (spark.readStream.format("cloudFiles")
                         .option("cloudFiles.format", "csv")
                         .option("cloudFiles.schemaLocation", f"{input_path}/_schema")
                         .option("header", "true")
                         .load(input_path))

    query = (df.writeStream
               .option("checkpointLocation", f"{input_path}/_checkpoint")
               .toTable("cybersec.bronze.netflow_logs"))

    query.awaitTermination()
