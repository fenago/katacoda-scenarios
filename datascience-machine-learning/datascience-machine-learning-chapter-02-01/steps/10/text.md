Let's visualize this data to make it make a little more sense. So there's another package called matplotlib, and again we're going to talk about that a lot more in the future as well, but it's a package that lets me make pretty graphs in IPython Notebooks, so it's an easy way to visualize your data and see what's going on.

In this example, we are using matplotlib to create a histogram of our income data broken up into 50 different buckets. So basically, we're taking our continuous data and discretizing it, and then we can call show on matplotlib.pyplot to actually display this histogram in line. Refer to the following code:

```
%matplotlib inline 
import matplotlib.pyplot as plt 
plt.hist(incomes, 50) 
plt.show()
```

Go ahead and select the code block and hit play. It will actually create a new graph for us as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/10/1.jpg)

If you're not familiar with histograms or you need a refresher, the way to interpret this is that for each one of these buckets that we've discretized our data into is showing the frequency of that data.

So, for example, around 27,000-ish we see there's about 600 data points in that neighborhood for each given range of values. There's a lot of people around the 27,000 mark, but when you get over to outliers like 80,000, there is not a whole lot, and apparently there's some poor souls that are even in debt at -40,000, but again, they're very rare and not probable because we defined a normal distribution, and this is what a normal probability curve looks like. Again, we're going to talk about that more in detail later, but I just want to get that idea in your head if you don't already know it.
