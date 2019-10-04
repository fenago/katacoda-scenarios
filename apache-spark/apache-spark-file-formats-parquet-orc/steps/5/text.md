
**Step 3:** Let us write this back to the filesystem in Parquet format.

```parquetData
.write
.save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output4")```{{execute}}
 

We can check if the save was successful by simply running the cat command from a new terminal as shown below. However, you will not be able to read the file correctly as it is not human readable.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output4/part*`{{execute}}

 

