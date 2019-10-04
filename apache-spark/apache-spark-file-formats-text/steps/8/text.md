
**Step 2:** Let us now load this file to Spark using the Spark Shell with the following code.

```val ratings = spark
.read
.text("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/ratings.txt")```{{execute}} 

Let us now check if the read was successful by calling the show method on the ratings dataframe.

`ratings.show()`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_006.png)

We can also use the textFile method as shown below.

```val ratings = spark
.read
.textFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/ratings.txt")```{{execute}} 

Using textFile ignores the partition directory names.
