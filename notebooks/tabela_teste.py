# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.createDataFrame(
    [
        (1, "Greyce"),
        (2, "Databricks"),
        (3, "Terraform")
    ],
    ["id", "name"]
)

df.show()

spark.sql("CREATE SCHEMA IF NOT EXISTS teste_schema")

# Exemplo com PySpark
df.write.mode("overwrite").format("delta").option("mergeSchema", "true").saveAsTable("teste_schema.tabela_teste")