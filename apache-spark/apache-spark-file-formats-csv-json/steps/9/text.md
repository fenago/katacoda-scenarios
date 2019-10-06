
**Step 6:** Let us now write this dataframe to the filsesystem.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```multiJson.write
    .format("json")
    .save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output3")```{{execute T1}}

 
#### Output
You can check the output by running the following command from a new terminal.

**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output3/part*`{{execute T2}}

 
Task is complete!

