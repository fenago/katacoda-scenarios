**Step 2:** Let us now look at map collection. Let us first create a map of elements.

```val couples = Map("Chandler" -> "Monica", "Ross" -> "Rachel", "Phoebe" -> "Mike")

Now that we have a map collection, let us try to access the value by the key.

```println(couples("Chandler")

 

As you can see from the screenshot above, we were able to access the value based on it’s key.

But if we try to access a value for a non existing key, an exception is thrown as shown in the screenshot. 

```println(couples("Joey")

 

To overcome this problem, we use the getOrElse method and specify a default value when the key does not exist.

```val unknown = util.Try(couples("Joey")) getOrElse "Not Known"


```println(unknown)

 

Play around with Map as you did with lists and explore all the transformations and operations you can perform on the map objects.
