Alright, so computing the median is just as simple as computing the mean. Just like we had NumPy mean, we have a NumPy median function as well.

We can just use the median function on incomes, which is our list of data, and that will give us the median. In this case, that came up to $26,911, which isn't very different from the mean of $26988. Again, the initial data was random, so your values will be slightly different.

```
np.median(incomes) 
```

The following is the output of the preceding code:

```
Out[4]: 26911.948365056276
```

We don't expect to see a lot of outliers because this is a nice normal distribution. Median and mean will be comparable when you don't have a lot of weird outliers.
