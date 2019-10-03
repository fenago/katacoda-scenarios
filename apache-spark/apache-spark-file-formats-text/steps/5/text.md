
 

**Step 3:** Now, let us see how we can load multiple files in a directory using the wholeTextFiles method. For this please download the files available in the URL below.

books - http://bit.ly/2kupo5v

The folder should contain a total of 6 files. Please save them all in the IdeaProjects/Spark/chapter_10/ folder. You should now have the 6 files in this path IdeaProjects/Spark/chapter_10/books.

**Step 4:** Let us read these files using the wholeTextFiles method. This will read all the files present in books folder. Please switch back to Spark-shell and read the files using the code below.

```val textFiles = sc.wholeTextFiles("IdeaProjects/Spark/chapter_10/books")

This will return you a RDD[String, String] which is a paired RDD as shown below.

 

This paired RDD contains the name of the files as keys and the entire content of files as values.


