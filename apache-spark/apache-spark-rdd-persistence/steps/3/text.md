Let us understand this better with an example. The default behavior is that an RDD is computed every time an action is called on the RDD. Look at the following piece of code below.

scala> val data = sc.textFile(“/some/path/records.txt”)

The above line simply loads a text file using the textFile API and stores it to an RDD called data.

