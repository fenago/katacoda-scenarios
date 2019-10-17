In the previous task, we have created a dataFrame from an RDD. We have used a case class and toDF method to achieve the same. However, there are some limitations using case class method. The case class cannot have more than 22 arguments. If our data has more than 22 fields, it becomes hard to crearte a dataFrame from RDD using case class and toDF method.

To overcome this limitation, we have a createDataFrame method, which takes an RDD and schema as parameters to create a dataFrame. Let us create a dataFrame using createDataFrame method.

We shall be using the same input file `mlb_players.csv` for this task as well. 

**Step 1:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/createDf.scala` to view scala file.

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{DoubleType, IntegerType, StringType, StructField, StructType}

