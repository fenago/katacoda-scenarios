**Step 4:** Now that we have the SparkContext object created, let us load our file using the textFile API.

```
val data = sc.textFile("chapter_6/ratings-malformed.csv")
```
 
The aim of this task is to count the number of malformed records. But how do we decide which records are good and which are malformed? We need to have a look at our input file to answer this question. Open the file which you have downloaded in the step 1 for this task.

You will be able to see that the file contains four fields as explained in step 1. However, there are a bunch of records which are missing some fields as shown in the screenshot below.


In order to count and separate the good records with bad records we make use of Accumulators.