
Step 2: Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter rddToDs as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.
 


import org.apache.spark.sql.SparkSession

Step 3: Let us now create a case class so that we can define schema to our dataset as we did with DataFrame in the previous exercise. The names which we specify for attributes of case class object will get mapped as column names for our dataset. 

case class Players(player_name: String, team: String, position: String, height: Int, weight: Int, age: Double)
