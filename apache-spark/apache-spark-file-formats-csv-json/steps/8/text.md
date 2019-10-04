

**Step 3:** Let us check if we were able to load the JSON file successfully.

```jsonData.show()```{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_011.png

**Step 4:** Let us now load the multi line JSON file. Download the file example_2.json from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

example_2.json - http://bit.ly/2lL3IST

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.


**Step 5:** The following code is used to read the single line JSON file.

```val multiJson = spark.read
.format("json")
.option("multiLine", "true")
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/example_2.json")```{{execute}}
