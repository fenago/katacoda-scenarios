Loops are an essential part of any programming language and it is no different with Scala. Let us now look at the loops concept and write some code to get familiar with them.

**Step 1:** Let us start the loops concept with the if loop. Fire up the Scala console if you haven't already and type in the following code.

`val numOfKids = 3`{{execute}}

`if (numOfKids > 2) println ("They are Phoebe Buffay's kids.") else println ("Parent unknown!")`{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_031.png)

As you can see from the screenshot, the console only prints out the statement which is true based on the condition.

You can also write the if loop in the REPL in multiple lines using the paste mode as shown below. From the Scala prompt enter the following command and hit enter.

`:paste`{{execute}}

This will take you to the paste mode with a prompt to enter your code as shown in the screenshot.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_032.png)

You can now enter Scala code in multiple lines. Once you are done with your code press Ctrl + D to come out of the paste mode and execute the code.

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val numOfKids = 3
if (numOfKids > 2) {
println("They are Phoebe Buffay's kids.")
} else {
println("Parent unknown!")
}
```{{execute}}

The code is executed as soon as you have exited from the paste mode and result is displayed.
