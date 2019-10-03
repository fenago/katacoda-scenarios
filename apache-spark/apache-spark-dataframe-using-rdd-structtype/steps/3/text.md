Task 2: Creating Data Frame from an RDD

We can also create a Data Frame from an RDD. Let us see how to achieve this.

**Step 1:** Download the mlb_players.csv file from the URL below. This file contains six columns: name, team, position, height, weight, age.

mlb_players.csv - http://bit.ly/2JhzVJj

We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_7` to view file.

**Step 2:** Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter rddToDf as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.

import org.apache.spark.sql.SparkSession



