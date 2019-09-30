
Step 2: Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter window as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions._

Next, we need to write a case class so that we can specify the schema for our fields. 

case class Employee(name: String, number: Int, dept: String, pay: Double, manager: String)


We have created a case class and named it Employee by specifying the fields and its types.
