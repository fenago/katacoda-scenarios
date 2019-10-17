
**Step 3:** Let us write this back to the filesystem in Parquet format.

`parquetData.write.save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output4")`{{execute T1}}
 
#### Output
We can check if the save was successful by simply running the cat command from a new terminal as shown below. However, you will not be able to read the file correctly as it is not human readable.

**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output4/part*`{{execute T2}}

 

