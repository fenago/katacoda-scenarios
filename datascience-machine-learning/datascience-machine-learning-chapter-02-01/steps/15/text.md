Let's look at a histogram, because variance and standard deviation are all about the spread of the data, the shape of the distribution of a dataset. Take a look at the following histogram:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/15/1.png)

Let's say that we have some data on the arrival frequency of airplanes at an airport, for example, and this histogram indicates that we have around 4 arrivals per minute and that happened on around 12 days that we looked at for this data. However, we also have these outliers. We had one really slow day that only had one arrival per minute, we only had one really fast day where we had almost 12 arrivals per minute. So, the way to read a histogram is look up the bucket of a given value, and that tells you how frequently that value occurred in your data, and the shape of the histogram could tell you a lot about the probability distribution of a given set of data.

We know from this data that our airport is very likely to have around 4 arrivals per minute, but it's very unlikely to have 1 or 12, and we can also talk specifically about the probabilities of all the numbers in between. So not only is it unlikely to have 12 arrivals per minute, it's also very unlikely to have 9 arrivals per minute, but once we start getting around 8 or so, things start to pick up a little bit. A lot of information can be had from a histogram.

**Note:** Variance measures how spread-out the data is.