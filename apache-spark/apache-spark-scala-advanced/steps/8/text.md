Let us now look at few collections in Scala.

**Step 1:** Let us create a list and apply various transformations or operations over it.

`val shows: List[String] = List("F.R.I.E.N.D.S", "The Big Bang Theory", "Game of Thrones", "Breaking Bad", "The Mentalist")`{{execute}} 

Mentioning the type of list is optional as Scala can infer the type automatically. We can simply type "val shows = " and continue with the list.

Let us now print the list.

`println(s"Some of the popular TV shows are: $shows")`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_045.png) 

We can also access the individual items in the list using their index.

`println(s"The TV show at position 0 is ${shows(0)}")`{{execute}} 

`println(s"The TV show at position 1 is ${shows(1)}")`{{execute}} 

`println(s"The TV show at position 4 is ${shows(4)}")`{{execute}} 
 

