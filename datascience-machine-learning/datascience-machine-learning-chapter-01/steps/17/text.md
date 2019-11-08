
```
z.sort(reverse=True)
z
```

The output of the above code is as follows:

```
[3, 2, 1]
```

If you need to do a reverse sort, you can just say reverse=True as an attribute, as a parameter in that sort function, and that will put it back to 3, 2, 1.

If you need to let that sink in a little bit, feel free to go back and read it a little bit more.

#### Tuples
Tuples are just like lists, except they're immutable, so you can't actually extend, append, or sort them. They are what they are, and they behave just like lists, apart from the fact that you can't change them, and you indicate that they are immutable and are tuple, as opposed to a list, using parentheses instead of a square bracket. So you can see they work pretty much the same way otherwise:

```
#Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
len(x)
```

The output of the previous code is as follows:

```
3
```

We can say x= (1, 2, 3). I can still use length - len on that to say that there are three elements in that tuple, and even though, if you're not familiar with the term tuple, a tuple can actually contain as many elements as you want. Even though it sounds like it's Latin based on the number three, it doesn't mean you have three things in it. Usually, it only has two things in it. They can have as many as you want, really.
