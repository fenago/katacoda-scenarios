Step 4: We can also save a parquet file using compression as shown below.

scala> parquetData
.write
.option(“codec”, “gzip”)
.save(“IdeaProjects/Spark/chapter_10/output5”)

Task 4 is complete!

