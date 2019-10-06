Hadoop files are the output of Hadoop MapReduce jobs. We can read Hadoop files with Spark and do further processing using Spark. We shall now look at both the old Hadoop API to read the output from MapReduce jobs to Spark. 


**Step 1:** Download the file part-r-00000 from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

part-r-00000 - http://bit.ly/2lSqdFy

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.

This file is the output of a Word Count MapReduce job. It contains words as keys and values as the count separated by tab

**Step 2:** Before we read the file, we first need the following imports. We need to import the datatypes for both keys and values and also the input format. The keys are of type Text, values are Text and the input format is KeyValueTextInputFormat.

```import org.apache.hadoop.io.Text
import org.apache.hadoop.mapred.KeyValueTextInputFormat```{{execute T1}}
 


