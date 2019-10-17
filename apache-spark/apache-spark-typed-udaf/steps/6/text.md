
Now, that we have the required imports and case classes defined, we need to extend our object to inherit Aggregator abstract class as shown below.

```
object MyAverageAggregator extends Aggregator[Ratings, Average, Double] {
```

The Aggregator abstract class takes three parameters. They are the input, buffer and output type. The input is Ratings, the buffer is Average and the output type is Double.
