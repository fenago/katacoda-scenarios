We usually refer to variance as sigma squared, and you'll find out why momentarily, but for now, just know that variance is the average of the squared differences from the mean.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/16/1.png)

Let's look at what happens there, so (-3.4)2 is a positive 11.56 and (-0.4)2 ends up being a much smaller number, that is 0.16, because that's much closer to the mean of 4.4. Also (0.6)2 turned out to be close to the mean, only 0.36. But as we get up to the positive outlier, (3.6)2 ends up being 12.96. That gives us: (11.56, 0.16, 0.36, 0.16, 12.96).

To find the actual variance value, we just take the average of all those squared differences. So we add up all these squared variances, divide the sum by 5, that is number of values that we have, and we end up with a variance of 5.04.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/16/2.png)

OK, that's all variance is.