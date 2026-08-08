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