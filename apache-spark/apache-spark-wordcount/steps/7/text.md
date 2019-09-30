
Task 3: Spark Program – Performing Operations


In the previous task, we have successfully created an RDD. Now let us use the RDD and apply operations to achieve our goal of counting number of words in a file.

Step 1: We have an RDD which contains text in lines. Let us split the lines to words using the flatMap function. The flatMap function is used to remove a level of nesting. The flatMap function is basically a combination map function and flatten function where the map function is applied first and then flatten function is applied.

val words = data.flatMap(line => line.split(" "))

The above piece of code splits each line into a seperate word. The logic we apply to split the line is by a white space character. The flatMap function takes the data RDD and splits each line of word by a space character.

As a lab challenge, apply a map function to see how the output looks like instead of flatMap function. After you see the output from map function, apply flatten function to compare the result of flatMap function and the result of map and flatten function.
