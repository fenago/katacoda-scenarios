Let us now save the file using the code below.

```
 userCountByState.write
    .format("csv")
    .save("chapter_7/output")
```

Similar to reading the file using read and load methods, we use write and save methods to save the file to file system.

 

Now run the program as you did in the previous task and check the output directory. You should see two files: part-00000 and a _SUCCESS file. The output is saved in part-00000 file.
 
`sbt "runMain training.sqlQueries"`{{execute}} 

#### Output Files

`ls ~/apache-spark/Files/chapter_7/output`{{execute}} 

`cat ~/apache-spark/Files/chapter_7/output/part-*`{{execute}} 

Open the `part-00000-<guid>` file and you should see the result.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_034.png)

This way you can perform any operations using the SQL data manipulation language. 

Task is complete!


