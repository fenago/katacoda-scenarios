
**Step 4:** Let us now write this dataframe back to the filesystem in CSV format.

```dataNew.write
.format("csv")
.option("sep", "|")
.save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output2")```{{execute}}

Here, we have used an option called sep which replaces the delimiter from comma to a pipe.

**Step 5:** Let us check if the save was successful as we desired.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output2/part*`{{execute}}


Task is complete!
