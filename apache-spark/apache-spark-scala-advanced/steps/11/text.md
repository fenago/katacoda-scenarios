**Step 3:** Let us now create a tuple and see how we can access its elements.

`val showInfo = (1994, "Friends", 8.8, 2011, "Game Of Thrones", 9.4, 2010, "Sherlock", 9.1)`{{execute}} 

As you can see from the screenshot above, a tuple can contain different types of elements. Also, you need not explicitly specify the data types for the elements. Scala can infer data types automatically.

Let us now access the elements of the tuple based on its index. Remember, the index of a tuple starts with 1 and NOT with 0.

`println(showInfo._1)`{{execute}} 

`println(showInfo._5)`{{execute}} 

We can also access the elements of a tuple and print it out to the console as shown below.

`println(s"${showInfo._5} is the highest rated show with ${showInfo._6} rating.")`{{execute}} 

Task is complete!
