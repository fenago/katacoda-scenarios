Let's talk about regression analysis, a very popular topic in data science and statistics. It's all about trying to fit a curve or some sort of function, to a set of observations and then using that function to predict new values that you haven't seen yet. That's all there is to linear regression!

So, linear regression is fitting a straight line to a set of observations. For example, let's say that I have a bunch of people that I measured and the two features that I measured of these people are their weight and their height:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/1.png)

I'm showing the weight on the x-axis and the height on the y-axis, and I can plot all these data points, as in the people's weight versus their height, and I can say, "Hmm, that looks like a linear relationship, doesn't it? Maybe I can fit a straight line to it and use that to predict new values", and that's what linear regression does. In this example, I end up with a slope of 0.6 and a y-intercept of 130.2 which define a straight line (the equation of a straight line is y=mx+b, where m is the slope and b is the y-intercept). Given a slope and a y-intercept, that fits the data that I have best, I can use that line to predict new values.
