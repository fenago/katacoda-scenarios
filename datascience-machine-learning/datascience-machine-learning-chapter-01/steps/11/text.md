
```
x = [1, 2, 3, 4, 5, 6]
print (len(x))
```

You can say, call a list x, for example, and assign it to the numbers 1 through 6, and these square brackets indicate that we are using a Python list, and those are immutable objects that I can actually add things to and rearrange as much as I want to. There's a built-in function for determining the length of the list called len, and if I type in len(x), that will give me back the number 6 because there are 6 numbers in my list.

Just to make sure, and again to drive home the point that this is actually running real code here, let's add another number in there, such as 4545. If you run this, you'll get 7 because now there are 7 numbers in that list:

```
x = [1, 2, 3, 4, 5, 6, 4545]
print (len(x))
```

The output of the previous code example is as follows:

```
7
```

Go back to the original example there. Now you can also slice lists. If you want to take a subset of a list, there's a very simple syntax for doing so:

```
x[3:]
```

The output of the above code example is as follows:

```
[1, 2, 3]
```
