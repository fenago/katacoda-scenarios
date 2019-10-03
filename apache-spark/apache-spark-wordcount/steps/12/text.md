Task 5: Spark Program – Lineage Graph

Let us now check the Lineage Graph for our Word Count program.

**Step 1:** To check the Lineage Graph for our Word Count program, we should use the toDebugString method. To do so, simply replace the saveAsTextFile line from previous task with the code below.

count.toDebugString.foreach(print)

Please note that we have used print inside foreach and not println.


**Step 2:** Run the program as you did before and you should see the output as shown below.


As you can see from the screenshot above, the toDebugString method displays the Lineage Graph. The indentations in the last four lines specify the shuffle boundary. Meaning, there was no shuffle of data for these opeartions: map, flatmap, teftFile. While the reduceByKey operation involves shuffling of data.


The number inside the paranthesis is to denote the number of parallel tasks. In our case it is only 1. The higher number denotes a high level of parallelism.

Task is complete!

