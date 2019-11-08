
Let's talk about probability density functions, and we've used one of these already in the book. We just didn't call it that. Let's formalize some of the stuff that we've talked about. For example, we've seen the normal distribution a few times, and that is an example of a probability density function. The following figure is an example of a normal distribution curve

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/25/1.png)


It's conceptually easy to try to think of this graph as the probability of a given value occurring, but that's a little bit misleading when you're talking about continuous data. Because there's an infinite number of actual possible data points in a continuous data distribution. There could be 0 or 0.001 or 0.00001 so the actual probability of a very specific value happening is very, very small, infinitely small. The probability density function really tells the probability of a given range of values occurring. So that's the way you've got to think about it.

So, for example, in the normal distribution shown in the above graph, between the mean (0) and one standard deviation from the mean (1σ) there's a 34.1% chance of a value falling in that range. You can tighten this up or spread it out as much as you want, figure out the actual values, but that's the way to think about a probability density function. For a given range of values it gives you a way of finding out the probability of that range occurring.

- You can see in the graph, as you get close to the mean (0), within one standard deviation (**-1σ** and **1σ**), you're pretty likely to land there. I mean, if you add up 34.1 and 34.1, which equals to 68.2%, you get the probability of landing within one standard deviation of the mean.
- However, as you get between two and three standard deviations (-3σ to -2σ and 2σ to 3σ), we're down to just a little bit over **4%** (4.2%, to be precise).
- As you get out beyond three standard deviations (-3σ and 3σ) then we're much less than 1%.

So, the graph is just a way to visualize and talk about the probabilities of the given data point happening. Again, a probability distribution function gives you the probability of a data point falling within some given range of a given value, and a normal function is just one example of a probability density function. We'll look at some more in a moment.
