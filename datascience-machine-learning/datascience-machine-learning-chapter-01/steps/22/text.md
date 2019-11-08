One more thing that's kind of a Python-ish sort of a thing to do, which you might not see in other languages is the concept of lambda functions, and it's kind of called functional programming. The idea is that you can include a simple function into a function. This makes the most sense with an example:

```
#Lambda functions let you inline simple functions
print (DoSomething(lambda x: x * x * x, 3))
```

The output of the above code is as follows:

```
27
```

We'll print `DoSomething`, and remember that our first parameter is a function, so instead of passing in a named function, I can declare this function inline using the lambda keyword. Lambda basically means that I'm defining an unnamed function that just exists for now. It's transitory, and it takes a parameter x. In the syntax here, lambda means I'm defining an inline function of some sort, followed by its parameter list. It has a single parameter, x, and the colon, followed by what that function actually does. I'll take the x parameter and multiply it by itself three times to basically get the cube of a parameter.

In this example, `DoSomething` will pass in this lambda function as the first parameter, which computes the cube of x and the `3` parameter. So what's this really doing under the hood? This lambda function is a function of itself that gets passed into the f in DoSomething in the previous example, and x here is going to be 3. This will return f of x, which will end up executing our lambda function on the value 3. So that 3 goes into our x parameter, and our lambda function transforms that into 3 times 3 times 3, which is, of course, 27.

Now this comes up a lot when we start doing MapReduce and Spark and things like that. So if we'll be dealing with Hadoop sorts of technologies later on, this is a very important concept to understand. Again, I encourage you to take a moment to let that sink in and understand what's going on there if you need to.
