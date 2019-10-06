Let us now look at reading and writing CSV files to Spark. We have been reading and writing CSV files in the previous chapters. However, let us also see some of many options that can be used while reading and writing CSV files.

**Step 1:** Download the file ratings.csv from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

ratings.csv - http://bit.ly/2L8IEBS

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.

Each line of this file represents one rating of one movie by one user, and has the following format: userId, movieId, rating, timestamp

**Step 2:** Let us now read this file to Spark from Spark shell using few options.

Open the terminal and fire up the Spark shell `spark-shell`{{execute T1}}.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val data = spark
.read
.format("csv")
.option("InferSchema", "true")
.option("header", "false")
.option("nullValue", "Null")
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/ratings.csv")```{{execute T1}}

We have used a new option here which is called NullValue. This will replace all the null values with the provided string, which is Null in this case. The default is "". Please check the references section for all the options that can be used while reading or writing CSV files. All the options can be used in this way or inside a map object.

We can then call the show method as shown in the screenshot below to check if it was successful.
 
 ![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_008.png)
