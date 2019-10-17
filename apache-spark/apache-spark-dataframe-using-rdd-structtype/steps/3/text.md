We can also create a Data Frame from an RDD. Let us see how to achieve this.

**Step 1:** Download the mlb_players.csv file from the URL below. This file contains six columns: name, team, position, height, weight, age.

mlb_players.csv - http://bit.ly/2JhzVJj

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_7` to view file.

**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/rddToDf.scala` to view scala file.


```
import org.apache.spark.sql.SparkSession
```



