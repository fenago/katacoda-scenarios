As for why there is difference between population and sample variance, it gets into really weird things about probability that you probably don't want to think about too much, and it requires some fancy mathematical notation, I try to avoid notation in this book as much as possible because I think the concepts are more important, but this is basic enough stuff and that you will see it over and over again.

As we've seen, population variance is usually designated as sigma squared (σ2), with sigma (σ) as standard deviation, and we can say that is the summation of each data point X minus the mean, mu, squared, that's the variance of each sample squared over N, the number of data points , and we can express it with the following equation:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/19/1.png)

- X denotes each data point
- µ denotes the mean
- N denotes the number of data points

Sample variance similarly is designated as S2, with the following equation:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/19/2.png)

- X denotes each data point
- M denotes the mean
- N-1 denotes the number of data points minus 1

That's all there is to it.