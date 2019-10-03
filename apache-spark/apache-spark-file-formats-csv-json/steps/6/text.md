
**Step 4:** Let us now write this dataframe back to the filesystem in CSV format.

scala> dataNew.write
.format(“csv”)
.option(“sep”, “|”)
.save(“IdeaProjects/Spark/chapter_10/output2”)

Here, we have used an option called sep which replaces the delimiter from comma to a pipe.

**Step 5:** Let us check if the save was successful as we desired.

$ cat IdeaProjects/Spark/chapter_10/output2/part*

 

Task 2 is complete!