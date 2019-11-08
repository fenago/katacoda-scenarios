
**The append function**

If you want to just add one more thing to that list, you can use the append function. So I just want to stick the number 9 at the end, there we go:

```
x.append(9)
x
```

The output of the above code is as follows:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Complex data structures**

You can also have complex data structures with lists. So you don't have to just put numbers in it; you can actually put strings in it. You can put numbers in it. You can put other lists in it. It doesn't matter. Python is a weakly-typed language, so you can pretty much put whatever kind of data you want, wherever you want, and it will generally be an OK thing to do:

```
y = [10, 11, 12]
listOfLists = [x, y]
listOfLists
```

In the preceding example, I have a second list that contains 10, 11, 12, that I'm calling y. I'll create a new list that contains two lists. How's that for mind blowing? Our listofLists list will contain the x list and the y list, and that's a perfectly valid thing to do. You can see here that we have a bracket indicating the listofLists list, and within that, we have another set of brackets indicating each individual list that is in that list:

```
[[ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [10, 11, 12]]
```

So, sometimes things like these will come in handy.
