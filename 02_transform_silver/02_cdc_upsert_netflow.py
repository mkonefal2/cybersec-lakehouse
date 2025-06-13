"""Merge NetFlow logs using Change Data Feed semantics."""
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

def main(source_path: str, target_path: str) -> None:
    spark = SparkSession.builder.appName("netflow_cdc_upsert").getOrCreate()
    source_df = spark.read.format("delta").load(source_path)
    (
        source_df.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(target_path)
    )

    # Example MERGE command for incremental upserts
    spark.sql(f"""
    MERGE INTO {target_path} t
    USING {source_path} s
    ON t.ID = s.ID
    WHEN MATCHED THEN UPDATE SET *
    WHEN NOT MATCHED THEN INSERT *
    """)

if __name__ == "__main__":
    main("delta/bronze/netflow_logs", "delta/silver/netflow_logs")
