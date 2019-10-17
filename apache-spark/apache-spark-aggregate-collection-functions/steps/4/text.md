

**Step 2:** Let us first use the built in aggregation functions. In the following piece of code, we are performing multiple aggreagations at once.

Before we use the functions we need to have the following import as shown below.

```
import org.apache.spark.sql.functions._
```

Next, we can simply use the select method and perform the multiple aggregations at once.

```
val agg = movies.select(
    avg("rating")
  , min("userId")
  , max("movieId")
  , sum("userId")
  , mean("rating")
)
```

We have used multiple aggregations such as avg, min, max etc on various columns. As the names of the functions suggest, avg computes the average, min and max compute the lowest and the highest values in the column, sum and mean computes the sum and mean of all the values in the columns respectively.
 
