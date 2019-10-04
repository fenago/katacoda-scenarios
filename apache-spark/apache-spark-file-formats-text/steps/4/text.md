
**Step 2:** Open the terminal and fire up the Spark shell. Let us load the text file using the code below.

`val textData = sc.textFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/treasure_island.txt")`{{execute}} 

This will read the data and create an RDD[String] as shown below. We can read data from any filesystem such as HDFS, AWS, Azure etc, this way just by providing the complete path or fully qualified URL of that purticular filesystem. We can then perform all the RDD operations or convert to a DataFrame or Dataset as required.

**Step 2:** Let us now write this back to the file system as shown below.

`textData.saveAsTextFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output")`{{execute}} 


Let us now check if the save was successful. For that open a new terminal and check the contents using the command below.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output/part-00000`{{execute}} 
