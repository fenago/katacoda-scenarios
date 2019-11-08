Now, NumPy can actually compute correlation for you using the corrcoef() function. Let's look at the following code:

```
np.corrcoef(pageseeds, purchaseAmount) 
```

This single line gives the following output:

```
array([(1.         ,-046728788], 
      [-0.46728788], 1.       ]) 
```

So, if we wanted to do this the easy way, we could just use np.corrcoef(pageSpeeds, purchaseAmount), and what that gives you back is an array that gives you the correlation between every possible combination of the sets of data that you pass in. The way to read the output is: the 1 implies there is a perfect correlation between comparing pageSpeeds to itself and purchaseAmount to itself, which is expected. But when you start comparing pageSpeeds to purchaseAmount or purchaseAmount to the pageSpeeds, you end up with the -0.4672 value, which is roughly what we got when we did it the hard way. There's going to be little precision errors, but it's not really important.
