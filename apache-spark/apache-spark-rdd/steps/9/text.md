Step 3: Let us now use filter function using the contains method and filter out an RDD which satisfies the filter criteria. Create a new list as shown below and then filter out a string.

scala> val friends = (“Monica”, “Chandler”, “Ross”, “Phoebe”, “Rachel”, “Joey”)

scala> val friendsRDD = sc.parallelize(friends)

scala> val chandler = friendsRDD.filter(name=> name.contains(“Chandler”))

scala> chandler.collect







 
RDD op.

IntelliJ D/l & Ins
Configure IntelliJ

 

The filter function we used above is a higher order function which takes another function as parameter and returns an RDD of type String. The name => name.contains(“chandler”) is similar to a function in Scala as shown below.

scala> def find(name: List[String]): Boolean = {
	name.contains(“Chandler”)
	}

Let’s call the function with the parameter friends which is a List of type String.

scala> find(friends)


The code below 

friendsRDD.filter(name=> name.contains(“Chandler”))

is same as

def find(name: List[String]): Boolean = {
	name.contains(“Chandler”)
}
friendsRDD.filter(find)

