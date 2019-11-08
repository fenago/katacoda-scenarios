
**The if statement**

```
print (1 is 3)
```

The output of the previous code is as follows:

```
False
```

The other thing we can do is use is, which is sort of the same thing as equal. It's a more Python-ish representation of equality, so 1 == 3 is the same thing as 1 is 3, but this is considered the more Pythonic way of doing it. So 1 is 3 comes back as False because 1 is not 3.

**The if-else loop**

```
if 1 is 3:
    print "How did that happen?"
elif 1 > 3:
    print ("Yikes")
else:
    print ("All is well with the world")
```

The output of the above code is as follows:

```
All is well with the world
```

We can also do if-else and else-if blocks here too. Let's do something a little bit more complicated here. If 1 is 3, I would print How did that happen? But of course 1 is not 3, so we will fall back down to the else-if block, otherwise, if 1 is not 3, we'll test if 1 > 3. Well that's not true either, but if it did, we print Yikes, and we will finally fall into this catch-all else clause that will print All is well with the world.

In fact, 1 is not 3, nor is 1 greater than 3, and sure enough, All is well with the world. So, you know, other languages have very similar syntax, but these are the peculiarities of Python and how to do an if-else or else-if block. So again, feel free to keep this notebook around. It might be a good reference later on.
