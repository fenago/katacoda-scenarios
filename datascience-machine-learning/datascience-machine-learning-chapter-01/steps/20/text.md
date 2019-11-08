In addition to Python Basics - Part 1, let us now try to grasp more Python concepts in detail.

**Functions in Python**

Let's talk about functions in Python. Like with other languages, you can have functions that let you repeat a set of operations over and over again with different parameters. In Python, the syntax for doing that looks like this:

```
def SquareIt(x):
    return x * x
print (SquareIt(2))
```

The output of the above code is as follows:

```
4
```

You declare a function using the def keyword. It just says this is a function, and we'll call this function SquareIt, and the parameter list is then followed inside parentheses. This particular function only takes one parameter that we'll call x. Again, remember that whitespace is important in Python. There's not going to be any curly brackets or anything enclosing this function. It's strictly defined by whitespace. So we have a colon that says that this function declaration line is over, but then it's the fact that it's tabbed by one or more tabs that tells the interpreter that we are in fact within the SquareIt function.

So def SquareIt(x): tab returns x * x, and that will return the square of x in this function. We can go ahead and give that a try. print squareIt(2) is how we call that function. It looks just like it would be in any other language, really. This should return the number 4; we run the code, and in fact it does. Awesome! That's pretty simple, that's all there is to functions. Obviously, I could have more than one parameter if I wanted to, even as many parameters as I need.
