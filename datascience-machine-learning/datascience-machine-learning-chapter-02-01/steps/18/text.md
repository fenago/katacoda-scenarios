There is a little nuance to standard deviation and variance, and that's when you're talking about population versus sample variance. If you're working with a complete set of data, a complete set of observations, then you do exactly what I told you. You just take the average of all the squared variances from the mean and that's your variance.

However, if you're sampling your data, that is, if you're taking a subset of the data just to make computing easier, you have to do something a little bit different. Instead of dividing by the number of samples, you divide by the number of samples minus 1. Let's look at an example.

We'll use the sample data we were just studying for people standing in a line. We took the sum of the squared variances and divided by 5, that is the number of data points that we had, to get 5.04.

```
σ2 = (11.56 + 0.16 + 0.36 + 0.16 + 12.96) / 5 = 5.04
```

If we were to look at the sample variance, which is designated by S2, it is found by the sum of the squared variances divided by 4, that is (n - 1). This gives us the sample variance, which comes out to 6.3.

```
S2 = (11.56 + 0.16 + 0.36 + 0.16 + 12.96) / 4 = 6.3
```

So again, if this was some sort of sample that we took from a larger dataset, that's what you would do. If it was a complete dataset, you divide by the actual number. Okay, that's how we calculate population and sample variance, but what's the actual logic behind it?
