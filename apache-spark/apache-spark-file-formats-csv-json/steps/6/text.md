
**Step 4:** Let us now write this dataframe back to the filesystem in CSV format.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

`dataNew.write.format("csv").option("sep", "|").save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output2")`{{execute T1}}

Here, we have used an option called sep which replaces the delimiter from comma to a pipe.

**Step 5:** Let us check if the save was successful as we desired.

**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output2/part*`{{execute T2}}


Task is complete!
