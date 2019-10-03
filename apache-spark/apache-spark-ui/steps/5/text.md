**Step 3:** Let us run a job. Create a List of few numbers and create an RDD from that list as shown below.

`val num = List(1, 2, 3, 4)`{{execute}} 

`val numRDD = sc.parallelize(num)`{{execute}} 

Now let us write a map function which takes the numRDD and gives a squaredRDD as shown below.

`val squaredRDD = numRDD.map(x => x * x)`{{execute}} 

`squaredRDD.foreach(println)`{{execute}} 

After you see the output in the console, navigate back to the browser and refresh the Spark web interface. You should see a completed job as shown in the screenshot below.


![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 4/Selection_026.png)