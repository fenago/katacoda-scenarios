

**Step 3:** Let us now write our main method and create a SparkSession object so that we can access Spark functionality. Please note that we haven't covered this topic but just think this as if we are creating a SparkContext object.

```
def main(args: Array[String]) {

val sparkSession = SparkSession.builder
.master("local[*]")
.appName("Bad record counter V2")
.getOrCreate()
```

We have created a SparkSession object using the SparkSession.builder method, specified the execution environment as local using all the cores in our CPU and finally named our application as Bad record counter V2. The getOrCreate method gets an instance of SparkSession if it is already available or it creates one.

 
