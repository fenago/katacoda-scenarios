NumPy provides a very handy percentile function that will compute the percentile values of this distribution for you. So, we created our vals list of data using np.random.normal, and I can just call the np.percentile function to figure out the 50th percentile value in using the following code:

```
np.percentile(vals, 50) 
```

The following is the output of the preceding code:

```
0.0053397035195310248
```

The output turns out to be 0.005. So remember, the 50th percentile is just another name for the median, and it turns out the median is very close to zero in this data. You can see in the graph that we're tipped a little bit to the right, so that's not too surprising.

I want to compute the 90th percentile, which gives me the point at which 90% of the data is less than that value. We can easily do that with the following code:

```
np.percentile(vals, 90)
```

Here is the output of that code:

```
Out[4]: 0.64099069837340827 
```

The 90th percentile of this data turns out to be 0.64, so it's around here, and basically, at that point less than 90% of the data is less than that value. I can believe that. 10% of the data is greater than 0.64, 90% of it, less than 0.65.
