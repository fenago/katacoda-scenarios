Fire up the spark-shell from the terminal and create a list as shown below.
`spark-shell`{{execute}}

Let us understand this better with an example. The default behavior is that an RDD is computed every time an action is called on the RDD. Look at the following piece of code below.

`val data = sc.textFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_4/treasure_island.txt")`{{execute}} 

The above line simply loads a text file using the textFile API and stores it to an RDD called data.

