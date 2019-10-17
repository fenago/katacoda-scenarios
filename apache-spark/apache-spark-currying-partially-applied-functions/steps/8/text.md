Let us now see how we can use the curried function and apply them partially.

**Step 1:** We have created a sum function in step 1 of previous exercise. Let us use that function and partially apply the parameters for that function.

`val sumObj = sum(6)_ `{{execute}}

This will return us a function object as shown in the screenshot below.
 
 ![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_007.png)

The _ is used as a placeholder for the parameter we are holding back. It indicates the compiler that we are partially applying a function. 

**Step 2:** We can then use the function object later to pass the parameter which we held back as shown below.

`sumObj(5)`{{execute}}

 



