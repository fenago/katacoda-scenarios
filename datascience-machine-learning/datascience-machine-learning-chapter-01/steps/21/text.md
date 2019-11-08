
Now there are some weird things you can do with functions in Python, that are kind of cool. One thing you can do is to pass functions around as though they were parameters. Let's take a closer look at this example:

```
#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)
print (DoSomething(SquareIt, 3))
```

The output of the preceding code is as follows:

```
9
```

Now I have a function called DoSomething, def DoSomething, and it will take two parameters,one that I'll call f and the other I'll call x, and if I happen, I can actually pass in a function for one of these parameters. So, think about that for a minute. Look at this example with a bit more sense. Here, DoSomething(f,x): will return f of x; it will basically call the f function with x as a parameter, and there's no strong typing in Python, so we have to just kind of make sure that what we are passing in for that first parameter is in fact a function for this to work properly.

For example, we'll say print DoSomething, and for the first parameter, we'll pass in SquareIt, which is actually another function, and the number 3. What this should do is to say do something with the SquareIt function and the 3 parameter, and that will return (SquareIt, 3), and 3 squared last time I checked was 9, and sure enough, that does in fact work.

This might be a little bit of a new concept to you, passing functions around as parameters,so if you need to stop for a minute there, wait and let that sink in, play around with it, please feel free to do so. Again, I encourage you to stop and take this at your own pace.
