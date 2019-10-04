
**Step 3:** Let us write this back to the filesystem as shown below.

```ratings
.write
.text("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output1")```{{execute}} 

Please make sure that you only have one string column while you save the text file successfully. Also, make sure the output directory (in this case, output1) doesn't exist before you perform the write action.

**Step 4:** Use the following command to check if the save was successful. You will have to use the new terminal to run this command, as this won't be executed in Spark shell.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output1/part*`{{execute}}

You should see the file saved as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_007.png)

Task is complete!


