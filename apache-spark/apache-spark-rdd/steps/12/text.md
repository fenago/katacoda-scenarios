**Step 5:** For the numRDD we created in the previous step, let us use the reduce function to add all the numbers.
`val sumRDD = numRDD.reduce((a, b) => (a + b))`{{execute}} 
 
Similarly, we can also use the reduce function to multiply all the numbers in numRDD.

`val mulRDD = numRDD.reduce((a, b) => (a * b))`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_030.png)

These are a few basic RDD operations. Task is complete!


#### SUMMARY

Resilient Distributed Dataset also known as `RDD` is the basic data structure of Spark which is immutable and fault tolerant collection of elements that can be computed in parallel over a cluster of machines.

Spark is a `master-slave` architecture. Spark consists of a Driver Program as the master and executors as slaves. A cluster manager is used to manage resources across the cluster.

In the lab, we have installed Spark and learned RDD basic operations.
