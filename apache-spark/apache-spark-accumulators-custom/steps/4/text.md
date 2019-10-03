**Step 2:** Open IDE if not already, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter CountByMovie as the name of the Class. Please see that this is a class we are creating for this task and not an object. Enter the imports as shown below.

```
import org.apache.spark.util.AccumulatorV2
import scala.collection.mutable.HashMap
```

The first import is version two of Accumulator. The second import is an mutable HashMap as we will be storing our movies and total number of ratings as key and value respectively. We need to explicitly import the HashMap collection or else we would end up having an immutable HashMap when we declare one. 

**Step 3:** We now have to extend our class to inherit AccumulatorV2 and then specify the input and output. The input to our Accumulator would be a tuple (movieId and count), processed by each task (local accumulator) on executors  and the output is a HashMap which will be aggregated by the global accumulator on driver.

```
class CountByMovie extends  AccumulatorV2[(Int, Int), HashMap[Int, Int]]{
```

You may ignore the red error asking to implement merge method under the class name for now. This error will be gone once we implement all the methods in the code.




