
**Step 2:** Let us now load this file to Spark using the Spark Shell with the following code.

scala> val ratings = spark
.read
.text(“IdeaProjects/Spark/chapter_10/ratings.txt”)
 

Let us now check if the read was successful by calling the show method on the ratings dataframe.

scala> ratings.show()

 

We can also use the textFile method as shown below.

scala> val ratings = spark
.read
.textFile(“IdeaProjects/Spark/chapter_10/ratings.txt”)

Using textFile ignores the partition directory names.
