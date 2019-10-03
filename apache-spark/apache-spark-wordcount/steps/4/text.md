**Step 5:** Once we have the required imports, we need to write the main function similar to that of Java. This is the starting point for the compiler to execute our program. 

```
def main(args: Array[String]): Unit = {
```

The main function takes an argument args which is an Array of String type and does not return anything. Unit represents no return value similar to void in Java. It is optional to mention the return type.


**Step 6:** Let us declare the level of logging to only log the error and fatal messages.

```
Logger.getLogger("Org").setLevel(Level.ERROR)
```

This step is not mandatory and you may skip this if you want all the logs.