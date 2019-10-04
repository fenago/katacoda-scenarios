

**Step 3:** We can now simply write to an ORC format similar to what we have been doing with other file formats so far.

```orcData
.write
.format("orc")
.save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output5")```{{execute}}


Similar to Parquet, ORC is also not human readable and you will only see gibberish data when used the cat command as shown below.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output5/part*`{{execute}}

 
Task is complete!
