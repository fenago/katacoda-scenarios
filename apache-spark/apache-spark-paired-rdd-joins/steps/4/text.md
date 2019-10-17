
**Step 3:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/joins.scala` to view scala file.

```
import org.apache.spark._
import org.apache.log4j._

object joins {

case class ratings(userId: Int, movieID: Int, rating: Float, timestamp: String)

case class movies(movieID: Int, movieName: String, genre:String)
```

 
