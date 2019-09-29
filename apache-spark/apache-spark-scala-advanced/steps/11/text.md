Step 3: Let us now create a tuple and see how we can access its elements.

scala> val showInfo = (1994, “Friends”, 8.8, 2011, “Game Of Thrones”, 9.4, 2010, “Sherlock”, 9.1)



 
Loops

Functions
Collections

 

As you can see from the screenshot above, a tuple can contain different types of elements. Also, you need not explicitly specify the data types for the elements. Scala can infer data types automatically.

Let us now access the elements of the tuple based on its index. Remember, the index of a tuple starts with 1 and NOT with 0.

scala> println(showInfo._1)

scala> println(showInfo._5)

 

We can also access the elements of a tuple and print it out to the console as shown below.

scala> println(s“${showInfo._5} is the highest rated show with “${showInfo._6} rating.”)
 
 
Loops

Functions
Collections


 

As always, play around with tuples and practice as much as possible.

Task 6 is complete!
