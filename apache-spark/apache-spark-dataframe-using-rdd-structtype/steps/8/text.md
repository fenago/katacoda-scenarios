
**Step 2:** Let us now write the main function and create SparkSession as created in previous tasks.

```
def main(args: Array[String]): Unit = {

  val ss = SparkSession
    .builder()
    .appName("Rdd to DataFrame")
    .master("local[*]")
    .getOrCreate()
```
 

**Step 3:** The next step is similar to what we have done in the previous task. We load the input file using the textFile API, extract the header and filter it out using the filter method. Next, we split the fields based on comma delimiter.

```
val input = ss.sparkContext.textFile("chapter_7/mlb_players.csv")
val header = input.first()
val records = input.filter(x => x != header)
val fields = records.map(record => record.split(","))
```

 
