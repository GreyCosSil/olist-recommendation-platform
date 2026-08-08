# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


# ============================================================
# Parâmetros recebidos do Terraform / Databricks Job
# ============================================================

dbutils.widgets.text("schema_name", "")
dbutils.widgets.text("table_name", "")

schema_name = dbutils.widgets.get("schema_name")
table_name = dbutils.widgets.get("table_name")

print(f"schema_name = {schema_name}")
print(f"table_name = {table_name}")

df = spark.createDataFrame(
    [
        (1, "Greyce"),
        (2, "Databricks"),
        (3, "Terraform")
    ],
    ["id", "name"]
)

df.show()

# Verifica os schemas disponíveis.
spark.sql("SHOW SCHEMAS IN ml_training_dev").show(truncate=False)

table_full_name = f"ml_training_dev.{schema_name}.{table_name}"

# Salva a tabela no schema criado.
df.write.mode("overwrite").format("delta").option("mergeSchema", "true").saveAsTable(
        table_full_name
    )