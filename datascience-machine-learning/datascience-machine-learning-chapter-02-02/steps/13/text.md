Let's compute the 20th percentile value, that would give me the point at which 20% of the values are less than that number that I come up with. Again, we just need a very simple alteration to the code:

```
np.percentile(vals, 20) 
```

This gives the following output:

```
Out[5]:-0.41810340026619164 
```

The 20th percentile point works out to be -0.4, roughly, and again I believe that. It's saying that 20% of the data lies to the left of -0.4, and conversely, 80% is greater.

If you want to get a feel as to where those breaking points are in a dataset, the percentile function is an easy way to compute them. If this were a dataset representing income distribution, we could just call np.percentile(vals, 99) and figure out what the 99th percentile is. You could figure out who those one-percenters people keep talking about really are, and if you're one of them.

Alright, now to get your hands dirty. I want you to play around with this data. This is an IPython Notebook for a reason, so you can mess with it and mess with the code, try different standard deviation values, see what effect it has on the shape of the data and where those percentiles end up lying, for example. Try using smaller dataset sizes and add a little bit more random variation in the thing. Just get comfortable with it, play around with it, and find you can actually do this stuff and write some real code that works.
