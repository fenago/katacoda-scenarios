
**Step 2:** Create a new Scala object and name it averageTypedUDAF. Next, we will need the following imports to implement a UADF. We haven't used some of these imports so far. We shall learn about them as we continue with our program.

```
import org.apache.spark.sql.expressions.Aggregator
import org.apache.spark.sql.{Encoder, Encoders, SparkSession}
```

Next we have to declare the case classes to specify schema for both input and buffer. However, we need not use StructType here as we did with Untyped UDAF. As we will be loading the input as Dataset and not DataFrame, the schema is associated with the case class.

```
case class Ratings(userId: Int, movieID: Int, rating: Double, timeStamp: String)
case class Average(var sum: Double, var count: Long)
```
The first case class Ratings specifies the input schema and the second case class Average specifies the buffer schema. Please not that we have used var keyword to define mutable fields in Average buffer as the buffer keeps on updated when task process each row as explained in previous tasks.
