Parquet is Spark's default file format. Let us read and write Parquet files in Spark.

**Step 1:** Download the file userdata1.parquet from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

userdata1.parquet - http://bit.ly/2kfIhJ4

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.


**Step 2:** Let us no read this Parquet file to Spark using the code below.

Open the terminal and fire up the Spark shell `spark-shell`{{execute T1}}.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

 ```val parquetData = spark
.read
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/userdata1.parquet")```{{execute T1}}

Please see that we need not mention the format here as Parquet is default file format in Spark. However, you may explicitly mention the format as we did in the previous tasks if you desire so.

`parquetData.show()`{{execute T1}} 

You should see the following output when you call the show method on the dataframe.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_015.png)

