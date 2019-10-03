Create a List of few numbers and create an RDD from that list as shown below.

```val num = List(1, 2, 3, 4)
val numRDD = sc.parallelize(num)

Now let us write a map function which takes the numRDD and gives a squaredRDD as shown below.

`val squaredRDD = numRDD.map(x => x * x)`{{execute}} 

`squaredRDD.foreach(println)`{{execute}} 

 
 ```numRDD.map(x => x * x)```{{execute}} 

is same as

```def square(x: Int): Int = {
	x * x
}
numRDD.map(square)```{{execute}} 

**Step 5:** For the numRDD we created in the previous step, let us use the reduce function to add all the numbers.
`val sumRDD = numRDD.reduce((a, b) => (a + b))`{{execute}} 
 
Similarly, we can also use the reduce function to multiply all the numbers in numRDD.

`val mulRDD = numRDD.reduce((a, b) => (a * b))`{{execute}} 
 

These are a few basic RDD operations. We shall look at more of these operations in detail in latter scenarios. 

Task is complete!
