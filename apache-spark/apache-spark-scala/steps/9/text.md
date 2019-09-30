Scala Monadic Collections
Now that we are looking at error handling in Spark, let us discuss the Monadic Collections in Scala which are used for error handling.

There are three Monadic collections in Scala which are used in error handling in functional programming, similar to try catch blocks in Java exception handling. However, in functional programming, we have to return something while try catch blocks in Java do not return anything. So, Monadic collections help you follow the rules of functional programming while implementing error handling.

Unlike the traditional collections such as List, Map, Set etc which can contain multiple objects, Monadic collections only contain two objects and can only return one object at a time. Let us look at these collections in detail.



Option Monadic Collection
The Option Monadic Collection helps us deal with the NullPointerException. As explained earler, Option Monadic Collection also contains two objects called Some and None. Let us create a case class which stores employee information.

scala> val welcome: Option[String] = Some(“Welcome to Learning Voyage”)

You can now retrieve the value using the get method as String is wrapped into an option.

scala> welcome.get

Similarly, you can also set the None object to the variable as shown below.

scala> val welcome: Option[String] = None

Since there is no value set for our variable, we can use getOrElse method to set a value on the fly as shown below.

scala> welcome.getOrElse(“Ernesto Lee Website”)

This is a very basic example of using Option collection. You can use them in variety of cases like pattern matching, case class etc.