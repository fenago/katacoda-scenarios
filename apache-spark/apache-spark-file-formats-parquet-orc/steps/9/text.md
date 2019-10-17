

**Step 3:** We can now simply write to an ORC format similar to what we have been doing with other file formats so far.

`orcData.write.format("orc").save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output6")`{{execute T1}}


#### Output
Similar to Parquet, ORC is also not human readable and you will only see gibberish data when used the cat command as shown below.

**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.


`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output6/part*`{{execute T2}}

Task is complete!
