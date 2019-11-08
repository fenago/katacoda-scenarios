Here's a little example of how you might use the map function in your work:

```
rdd = sc.parallelize([1, 2, 3, 4]) 
rdd.map(lambda x: x*x) 
```

Let's say I created an RDD just from the list 1, 2, 3, 4. I can then call rdd.map() with a lambda function of x that takes in each row, that is, each value of that RDD, calls it x, and then it applies the function x multiplied by x to square it. If I were to then collect the output of this RDD, it would be 1, 4, 9 and 16, because it would take each individual entry of that RDD and square it, and put that into a new RDD.

If you don't remember what lambda functions are, we did talk about it a little bit earlier in this book, but as a refresher, the lambda function is just a shorthand for defining a function in line. So rdd.map(lambda x: x*x) is exactly the same thing as a separate function def squareIt(x): return x*x, and saying rdd.map(squareIt).

It's just a shorthand for very simple functions that you want to pass in as a transformation. It eliminates the need to actually declare this as a separate named function of its own. That's the whole idea of functional programming. So you can say you understand functional programming now, by the way! But really, it's just shorthand notation for defining a function inline as part of the parameters to a map() function, or any transformation for that matter.
