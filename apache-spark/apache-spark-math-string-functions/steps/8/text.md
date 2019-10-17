 

**Step 2:** Let us first use the split method to split the strings by space as below.

`val splitted = quoteDS.select(split($"value", " ").as("splits"))`{{execute}}

The split method takes two arguments. The first argument is the name of the column and the second method is the pattern to which the string should be split on.

Let us use the show method to display the dataset as shown below.

`splitted.show()`{{execute}}
 
![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_045.png)

As you can see from the screenshot above, the rows have now been splitted by whitespace.

**Step 3:** Next, let us use the explode function which we have learned in this exercise to create column for each element in the collection.

`val exploded = splitted.select(explode($"splits").as("explode"))`{{execute}} 

Let us use the show method to display the dataset as shown below.

`exploded.show()`{{execute}}

Now that we have each word as a row, let us apply some string functions.

The first function we use is to find out the length of each word using the length function as shown below.

`val strLen = exploded.select($"explode", length($"explode")).as("length")`{{execute}}

Let us use the show method to display the dataset as shown below.

`strLen.show()`{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_047.png)
