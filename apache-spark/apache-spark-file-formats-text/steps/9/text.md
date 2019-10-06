
**Step 3:** Let us write this back to the filesystem as shown below.

`ratings.write.text("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output1")`{{execute T1}} 

Please make sure that you only have one string column while you save the text file successfully. Also, make sure the output directory (in this case, output1) doesn't exist before you perform the write action.

**Step 4:** Use the following command to check if the save was successful. You will have to use the new terminal to run this command, as this won't be executed in Spark shell.


**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output1/part*`{{execute T2}}

You should see the file saved as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_007.png)

Task is complete!


