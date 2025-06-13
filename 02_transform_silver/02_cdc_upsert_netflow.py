from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cdc_upsert_netflow.py <input_table>")
        sys.exit(1)

    source_table = sys.argv[1]
    spark = SparkSession.builder.appName("CDCUpsertNetflow").getOrCreate()

    source_df = spark.table(source_table)
    target_table = "cybersec.silver.netflow_logs"

    if DeltaTable.isDeltaTable(spark, target_table):
        delta_tbl = DeltaTable.forName(spark, target_table)
        (delta_tbl.alias("t")
                 .merge(source_df.alias("s"), "t.FLOW_ID = s.FLOW_ID")
                 .whenMatchedUpdateAll()
                 .whenNotMatchedInsertAll()
                 .execute())
    else:
        source_df.write.format("delta").saveAsTable(target_table)

    print("Netflow upsert completed")
    spark.stop()
