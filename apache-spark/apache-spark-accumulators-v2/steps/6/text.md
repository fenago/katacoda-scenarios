
**Step 5:** The next step is to read the input data. Please note that this is a different API in Spark 2.x to read the data and we have not covered it yet. For now, just see this as a way to read the input data. We will also need an import for implicits.

```
import sparkSession.implicits._

val options = Map("header" -> "false", "InferSchema" -> "true")

val data = sparkSession.read.text("chapter_6/ratings-malformed.csv").as[String]
```

