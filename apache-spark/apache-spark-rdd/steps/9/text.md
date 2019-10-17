**Step 3:** Let us now use filter function using the contains method and filter out an RDD which satisfies the filter criteria. Create a new list as shown below and then filter out a string.

`val friends = List("Monica", "Chandler", "Ross", "Phoebe", "Rachel", "Joey")`{{execute}} 

`val friendsRDD = sc.parallelize(friends)`{{execute}} 

`val chandler = friendsRDD.filter(name=> name.contains("Chandler"))`{{execute}} 

`chandler.collect`{{execute}} 


The filter function we used above is a higher order function which takes another function as parameter and returns an RDD of type String. The name => name.contains("chandler") is similar to a function in Scala as shown below.

```def find(name: List[String]): Boolean = {
	name.contains("Chandler")
	}```{{execute}} 

Let's call the function with the parameter friends which is a List of type String.

`find(friends)`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_026.png)


