Now typically, we talk about standard deviation more than variance, and it turns out standard deviation is just the square root of the variance. It's just that simple.

So, if I had this variance of 5.04, the standard deviation is 2.24. So you see now why we said that the variance = (σ)2. It's because σ itself represents the standard deviation. So,if I take the square root of (σ)2, I get sigma. That ends up in this example to be 2.24.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/17/1.png)

#### Identifying outliers with standard deviation
Here's a histogram of the actual data we were looking at in the preceding example for calculating variance.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/17/2.png)

Now we see that the number 4 occurred twice in our dataset, and then we had one 1, one 5, and one 8.

The standard deviation is usually used as a way to think about how to identify outliers in your dataset. If I say if I'm within one standard deviation of the mean of 4.4, that's considered to be kind of a typical value in a normal distribution. However, you can see in the preceding diagram, that the numbers 1 and 8 actually lie outside of that range. So if I take 4.4 plus or minus 2.24, we end up around 7 and 2, and 1 and 8 both fall outside of that range of a standard deviation. So we can say mathematically, that 1 and 8 are outliers. We don't have to guess and eyeball it. Now there is still a judgment call as to what you consider an outlier in terms of how many standard deviations a data point is from the mean.


You can generally talk about how much of an outlier a data point is by how many standard deviations (or sometimes how many-sigmas) from the mean it is.

So that's something you'll see standard deviation used for in the real world.