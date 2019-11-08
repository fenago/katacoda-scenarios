
**Dereferencing an element**

We can also dereference the elements of a tuple, so element number 2 again would be the third element, because we start counting from 0, and that will give me back the number 6 in the following screenshot:

```
y = (4, 5, 6)
y[2]
```

The output to the above code is as follows:

```
6
```

**List of tuples**

We can also, like we could with lists, use tuples as elements of a list.

```
listOfTuples = [x, y]
listOfTuples
```

The output to the above code is as follows:

```
[(1, 2, 3), (4, 5, 6)]
```

We can create a new list that contains two tuples. So in the preceding example, we have our x tuple of (1, 2, 3) and our y tuple of (4, 5, 6); then we make a list of those two tuples and we get back this structure, where we have square brackets indicating a list that contains two tuples indicated by parentheses, and one thing that tuples are commonly used for when we're doing data science or any sort of managing or processing of data really is to use it to assign variables to input data as it's read in. I want to walk you through a little bit on what's going on in the following example:

```
(age, income) = "32,120000".split(',')
print (age)
print (income)
```

The output to the above code is as follows:

```
32
120000
```

Let's say we have a line of input data coming in and it's a comma-separated value file, which contains ages, say 32, comma-delimited by an income, say 120000 for that age, just to make something up. What I can do is as each line comes in, I can call the split function on it to actually separate that into a pair of values that are delimited by commas, and take that resulting tuple that comes out of split and assign it to two variables-age and income-all at once by defining a tuple of age, income and saying that I want to set that equal to the tuple that comes out of the split function.

So this is basically a common shorthand you'll see for assigning multiple fields to multiple variables at once. If I run that, you can see that the age variable actually ends up assigned to 32 and income to 120,000 because of that little trick there. You do need to be careful when you're doing this sort of thing, because if you don't have the expected number of fields or the expected number of elements in the resulting tuple, you will get an exception if you try to assign more stuff or less stuff than you expect to see here.
