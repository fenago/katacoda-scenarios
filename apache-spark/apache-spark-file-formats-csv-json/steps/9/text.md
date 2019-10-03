
**Step 6:** Let us now write this dataframe to the filsesystem.

scala> multiJson.write
.format(“json”)
.save(“IdeaProjects/Spark/chapter_10/output3”)

 

You can check the output by running the following command from a new terminal.

$ cat IdeaProjects/Spark/chapter_10/output3/part*

 

Task 3 is complete!
