
In reality, you often need to choose between bias and variance. It comes down to over fitting Vs underfitting your data. Let's take a look at the following example:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-08/steps/3/2.png)

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-08/steps/3/3.png)

It's a little bit of a different way of thinking of bias and variance. So, in the left graph, we have a straight line, and you can think of that as having very low variance, relative to these observations. So, there's not a lot of variance in this line, that is, there is low variance. But the bias, the error from each individual point, is actually high.

Now, contrast that to the overfitted data in the graph at the right, where we've kind of gone out of our way to fit the observations. The line has high variance, but low bias, because each individual point is pretty close to where it should be. So, this is an example of where we traded off variance for bias.

At the end of the day, you're not out to just reduce bias or just reduce variance, you want to reduce error. That's what really matters, and it turns out you can express error as a function of bias and variance:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-08/steps/3/4.png)

Looking at this, error is equal to bias squared plus variance. So, these things both contribute to the overall error, with bias actually contributing more. But keep in mind, it's error you really want to minimize, not the bias or the variance specifically, and that an overly complex model will probably end up having a high variance and low bias, whereas a too simple model will have low variance and high bias. However, they could both end up having similar error terms at the end of the day. You just have to find the right happy medium of these two things when you're trying to fit your data. We'll talk about some more principled ways of actually avoiding overfitting in our forthcoming sections. But, it's just the concept of bias and variance that I want to get across, because people do talk about it and you're going to be expected to know what means.
