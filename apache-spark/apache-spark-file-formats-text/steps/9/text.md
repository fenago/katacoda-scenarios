
Step 3: Let us write this back to the filesystem as shown below.

scala> ratings
.write
.text(“IdeaProjects/Spark/chapter_10/output1”)

Please make sure that you only have one string column while you save the text file successfully. Also, make sure the output directory (in this case, output1) doesn’t exist before you perform the write action.

Step 4: Use the following command to check if the save was successful. You will have to use the new terminal to run this command, as this won’t be executed in Spark shell.

$ cat IdeaProjects/Spark/chapter_10/output1/part*

You should see the file saved as shown below.

 


Task 1 is complete!

