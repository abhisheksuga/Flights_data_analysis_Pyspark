from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("YourAppName") \
    .getOrCreate()

df = spark.createDataFrame([(1, "Data"), (2, "Intensive")], ["id", "value"])
print(df.show())