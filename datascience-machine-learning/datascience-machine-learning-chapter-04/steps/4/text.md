How does linear regression work? Well internally, it uses a technique called ordinary least squares; it's also known as, OLS. You might see that term tossed around as well. The way it works is it tries to minimize the squared error between each point and the line, where the error is just the distance between each point and the line that you have.

So, we sum up all the squares of those errors, which sounds a lot like when we computed variance, right, except that instead of relative to the mean, it's relative to the line that we're defining. We can measure the variance of the data points from that line, and by minimizing that variance, we can find the line that fits it the best:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/2.png)

Now you'll never have to actually do this yourself the hard way, but if you did have to for some reason, or if you're just curious about what happens under the hood, I'll now describe the overall algorithm for you and how you would actually go about computing the slope and y-intercept yourself the hard way if you need to one day. It's really not that complicated.
