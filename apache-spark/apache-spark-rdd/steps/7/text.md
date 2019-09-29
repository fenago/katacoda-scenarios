Task 4: Basic RDD operations

Step 1: Let us start learning the basic RDD operations in Spark by creating an RDD from a collection as done in the previous task.

scala> val letters = List(f, a, g, f, c, a, b, n, d, b)

scala> val lettersRDD = sc.parallelize(letters)
