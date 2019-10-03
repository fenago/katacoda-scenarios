**Step 8:** We now have a SparkContext object created. We can now use this object and load data using the textFile API as we have done in the Spark Shell. 
 

Download a text file from the URL below and save it in the path IdeaProjects/Spark/chapter_4/treasure_island.txt. Please create new directories as required. The IdeaProjects folder is present in your Home folder.

treasure_island.txt - http://bit.ly/2LBFLtt

Once you have the file downloaded and saved in the desired location, write the following line of code to load the file to create an RDD.

val data = sc.textFile("chapter_4/treasure_island.txt")

With this we have successfully created an RDD using the text file.

 

This completes the process of creating a SparkContext object and creating the first RDD by loading the data using the textFile API.

Task is complete!

