**Step 4:** Let's now use a map function on the friendsRDD and output a tuple with the first character in each element and the name itself.

`val pairs = friendsRDD.map(name => (name.charAt(0), name))`{{execute}} 

With the the pairs RDD gets created. Now let us use the foreach keyword to print each element of the pairs RDD.

`pairs.foreach(println)`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_027.png) 

As you can see from the screenshot above, we have used the map function to create a tuple with first character of the name of each element and name itself in the friendsRDD. The first character is obtained by the function called charAt which takes the number to access the position of a character from a String.

If you think this is a bit complicated to understand, let us look at an another example with a simple map function in the next step.