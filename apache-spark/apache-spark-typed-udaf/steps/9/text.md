
**Step 8:** Let us now use this typed UDAF. Create a new object within the program as shown in the screenshot and name it avgTypedUDAF. Define the main function and also create the Spark Session.



```
object avgTypedUDAF {

  def main(args: Array[String]) {

    val sparkSession = SparkSession.builder
      .master("local[*]")
      .appName("Average ratings Typed UDAF")
      .getOrCreate()
```

next, load the file.

```
val ds = sparkSession.read
	.format("csv")
	.options(Map("InferSchema" -> "true", "header" -> "true"))
  	.load("chapter_9/ratings_head.csv")
	.as[Ratings]
```

The program should look like the screenshot below.
![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_033.png) 
 

 
