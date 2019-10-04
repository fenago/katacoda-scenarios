**Step 1:** Download the file userdata1_orc from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

userdata1.orc - http://bit.ly/2kfQi0J

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.

**Step 2:** Reading an ORC file is similar to what we have been doing so far through out this exercise.

```val orcData = spark
.read
.format("orc")
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/userdata1_orc")```{{execute}}


 `orcData.show()`{{execute}} 

You should see the following output when you call the show method on the dataframe.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_017.png)