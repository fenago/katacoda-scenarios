
 

**Step 3:** Now, let us see how we can load multiple files in a directory using the wholeTextFiles method. For this please download the files available in the URL below.

books - http://bit.ly/2kupo5v

**Note:** We already have cloned a github repository which contains a required files. Open `apache-spark/Files/chapter_10` to view file.

**Step 4:** Let us read these files using the wholeTextFiles method. This will read all the files present in books folder. Please switch back to Spark-shell and read the files using the code below.

`val textFiles = sc.wholeTextFiles("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/books")`{{execute T1}} 

This will return you a RDD[String, String] which is a paired RDD as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_004.png)

This paired RDD contains the name of the files as keys and the entire content of files as values.


