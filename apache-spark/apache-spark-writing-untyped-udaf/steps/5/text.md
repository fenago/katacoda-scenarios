
**Step 2:** Create a new Scala object and name it averageUDAF. Next, we will need the following imports to implement a UADF. We haven't used some of these imports so far. We shall learn about them as we continue with our program.

```
import org.apache.spark.sql.expressions.{MutableAggregationBuffer, UserDefinedAggregateFunction}
import org.apache.spark.sql.types._
import org.apache.spark.sql.{Row, SparkSession}
```

Now, that we have the required imports, we need to extend our object to inherit UserDefinedAggregateFunction as shown below.

```
object averageUDAF extends UserDefinedAggregateFunction {
```

We have used the import org.apache.spark.sql.expressions. UserDefinedAggregateFunction so that we can inhert it's methods in our program.

The program at this point should now look like the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_021.png)