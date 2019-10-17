**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/CountByMovie.scala` to view scala file.

```
import org.apache.spark.util.AccumulatorV2
import scala.collection.mutable.HashMap
```

The first import is version two of Accumulator. The second import is an mutable HashMap as we will be storing our movies and total number of ratings as key and value respectively. We need to explicitly import the HashMap collection or else we would end up having an immutable HashMap when we declare one. 

**Step 3:** We now have to extend our class to inherit AccumulatorV2 and then specify the input and output. The input to our Accumulator would be a tuple (movieId and count), processed by each task (local accumulator) on executors  and the output is a HashMap which will be aggregated by the global accumulator on driver.

```
class CountByMovie extends  AccumulatorV2[(Int, Int), HashMap[Int, Int]]{
```
