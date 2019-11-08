If, for example, you want to take the first three elements of a list, everything before element number 3, we can say :3 to get the first three elements, 1, 2, and 3, and if you think about what's going on there, as far as indices go, like in most languages, we start counting from 0. So element 0 is 1, element 1 is 2, and element 2 is 3. Since we're saying we want everything before element 3, that's what we're getting.

**Note:**

So, you know, never forget that in most languages, you start counting at 0 and not 1.

Now this can confuse matters, but in this case, it does make intuitive sense. You can think of that colon as meaning I want everything, I want the first three elements, and I could change that to four just again to make the point that we're actually doing something real here:

```
x[:4]
```

The output of the above code example is as follows:

```
[1, 2, 3, 4]
```
