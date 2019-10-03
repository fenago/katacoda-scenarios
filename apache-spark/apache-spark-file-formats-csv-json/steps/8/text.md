

**Step 3:** Let us check if we were able to load the JSON file successfully.

```jsonData.show()
 


 

**Step 4:** Let us now load the multi line JSON file. Download the file example_2.json from the URL below and save it to the IdeaProjects/Spark/chapter_10 folder.

example_2.json - http://bit.ly/2lL3IST

**Step 5:** The following code is used to read the single line JSON file.

```val multiJson = spark.read
.format("json")
.option("multiLine", "true")
.load("IdeaProjects/Spark/chapter_10/example_2.json")

