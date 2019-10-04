
**Step 6:** Let us now write this dataframe to the filsesystem.

```multiJson.write
.format("json")
.save("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/output3")```{{execute}}

 

You can check the output by running the following command from a new terminal.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/output3/part*`{{execute}}

 
Task is complete!

