Now that we have successfully written our untyped UDAF, let us use it find the average rating per user.

**Step 1:** Let us create a new object `avgRatingUDAF` within the UDAF which we have written in the previous task. Next, write the main function and also create a Spark Session object as shown below.

```
object avgRatingUDAF {

  def main(args: Array[String]) {

    val sparkSession = SparkSession.builder
      .master("local[*]")
      .appName("Average Rating UDAF")
      .getOrCreate()
```

The program should now look like the screenshot as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_025.png)
 
