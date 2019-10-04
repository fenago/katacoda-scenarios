**Step 1:** Let us start learning the basic RDD operations in Spark by creating an RDD from a collection as done in the previous task.

`val letters = List('f', 'a', 'g', 'f', 'c', 'a', 'b', 'n', 'd', 'b')`{{execute}} 

`val lettersRDD = sc.parallelize(letters)`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_021.png)