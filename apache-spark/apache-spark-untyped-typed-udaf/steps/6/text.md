
Now, that we have the required imports and case classes defined, we need to extend our object to inherit Aggregator abstract class as shown below.

```
object MyAverageAggregator extends Aggregator[Ratings, Average, Double] {
```

The Aggregator abstract class takes three parameters. They are the input, buffer and output type. The input is Ratings, the buffer is Average and the output type is Double.

The program should now look like the one as shown in the screenshot.

 

Please ignore the error you see for object name. This will go away once we implement all the required methods for UDAF as in the previous tasks.
