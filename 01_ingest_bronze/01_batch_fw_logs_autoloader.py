from pyspark.sql import SparkSession
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: batch_fw_logs_autoloader.py <input_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    spark = SparkSession.builder.appName("BatchFirewallIngestion").getOrCreate()

    df = (spark.read.format("cloudFiles")
                 .option("cloudFiles.format", "csv")
                 .option("header", "true")
                 .load(input_path))

    (df.write
       .mode("append")
       .option("mergeSchema", "true")
       .saveAsTable("cybersec.bronze.firewall_logs"))

    print("Firewall batch ingestion completed")
    spark.stop()
