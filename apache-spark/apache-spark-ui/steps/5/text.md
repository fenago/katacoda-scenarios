**Step 3:** Let us run a job. Create a List of few numbers and create an RDD from that list as shown below.

scala> val num = List(1, 2, 3, 4)
scala> val numRDD = sc.parallelize(num)

Now let us write a map function which takes the numRDD and gives a squaredRDD as shown below.

scala> val squaredRDD = numRDD.map(x => x * x)

scala> squaredRDD.foreach(println)

After you see the output in the console, navigate back to the browser and refresh the Spark web interface. You should see a completed job as shown in the screenshot below.