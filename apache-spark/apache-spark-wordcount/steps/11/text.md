The output displayed in the console is useful while developing but in the real time we would want the output to be saved. 

**Step 1:** We shall be using the saveAsTextFile API to save the output of our program to the disk. Simply replace the collect statement from the previous task with this line of code.

```
count.saveAsTextFile("chapter_4/word_count/output")
```

**Important:** You need to uncomment above line in `wordCount.scala` using **vscode** editor before running program again.

We shall be saving the output to the following path IdeaProjects/Spark/chapter_4/word_count/output. You need not create the directories word_count and output. They will be automatically created. In fact the compiler will throw an error if the output directory is already present.


**Step 2:** Now run the program as you did in the previous task and check the output directory. You should see two files: part-00000 and a _SUCCESS file. The output is saved in part-00000 file.
 
`sbt "runMain training.wordCount"`{{execute}} 

Open the `part-00000` file and you should see the result as shown below.

`ls ~/apache-spark/chapter_4/word_count/output`{{execute}} 

`cat ~/apache-spark/chapter_4/word_count/output/part-00000`{{execute}} 

