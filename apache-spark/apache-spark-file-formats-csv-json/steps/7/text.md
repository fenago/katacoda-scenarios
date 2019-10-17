


Similar to previous taks, let us read and write JSON files. We shall be reading two kinds of JSON files. One is a single line JSON and other is the multi line JSON.

JSON is also one of the popular file formats around which stands for JavaScrit Object Notation. JSON is compressable, splittable and human readable. It is also nested and supports complex data structures. With Spark, we can load a single line JSON and also a multi-line JSON. All we need to do is specify an option for multi-line JSON. However, it is recommend to use single line JSON whenever possible.

**Step 1:** Download the file example_1.json from the URL below and save it to the /home/scrapbook/tutorial/apache-spark/Files/chapter_10 folder.

example_1.json - http://bit.ly/2lRFI06

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_10` to view file.


**Step 2:** The following code is used to read the single line JSON file.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val jsonData = spark.read
.format("json")
.option("multiLine", "false")
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/example_1.json")```{{execute T1}}

