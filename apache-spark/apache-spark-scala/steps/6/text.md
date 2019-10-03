Task 3: Scala Basics
Let us now get familiar and start writing some Scala code to get acquainted with Scala syntax and basic programming constructs.

**Step 1:** Fire up your terminal and go into the Scala console by entering scala and hitting enter. Once you see the scala prompt, enter the following piece of code and hit enter

scala> val name: String = “Learning Voyage”


 
Loops

Functions
Collections

 

The above line of code is used to declare an immutable variable named name of type String which has a value of Learning Voyage. The keyword val is used to declare a variable which is immutable. When val is used, the created variable can no longer be changed or modified. Scala encourages to use immutability whenever possible. This will help you track your code easily and the values do not get modified accidentally when referring them programmatically. Unlike other languages, the name of the variable is declared first and then the data type is declared separated by a colon (:) in Scala. 

You can now use the variable name and use it inside the println function as shown below. This will print the value (String) associated with the variable (which is Learning Voyage in this case) to the console.

scala> println(name)

 
