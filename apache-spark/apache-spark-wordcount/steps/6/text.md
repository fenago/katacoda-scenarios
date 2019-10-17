**Step 8:** We now have a SparkContext object created. We can now use this object and load data using the textFile API as we have done in the Spark Shell. 
 

We already have cloned a github repository which contains a text file `treasure_island.txt`. Open `apache-spark/Files/chapter_4/treasure_island.txt` to view text file. Write the following line of code to load the file to create an RDD.

```
val data = sc.textFile("chapter_4/treasure_island.txt")
```

With this we have successfully created an RDD using the text file.

This completes the process of creating a SparkContext object and creating the first RDD by loading the data using the textFile API.

Task is complete!

