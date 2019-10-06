
Let's have a look and currying functions. We shall be working in the Scala shell for this and the next task.

**Step 1:** Open the terminal and fire up the Scala shell by simply typing in Scala in the terminal. You should see the Scala prompt.

`scala`{{execute}}

 

**Step 2:** Let us now define a simple currying function with two parameter groups as shown below to understand the concept of curried functions.

```def sum(x: Int) (y: Int): Int = {
| x + y
| }```{{execute}}

 
We have defined a function called sum which adds two numbers. Instead of passing the parameters as one group, we have curried the parameters in two parameter groups. This will help us with partially applied functions.






