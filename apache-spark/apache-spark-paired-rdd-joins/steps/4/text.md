
**Step 3:** Create a new object in the IDE and name it joins. Import all the required import statements as shown below. Next, let us a declare a case class with fields according to the columns in both the files along with their data types.

```
import org.apache.spark._
import org.apache.log4j._

object joins {

case class ratings(userId: Int, movieID: Int, rating: Float, timestamp: String)

case class movies(movieID: Int, movieName: String, genre:String)
```

 
