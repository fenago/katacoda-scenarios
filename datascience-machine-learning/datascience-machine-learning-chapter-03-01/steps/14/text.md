A scatter plot is something we'll see pretty often in this book. So, say you have a couple of different attributes you want to plot for the same set of people or things. For example, maybe we're plotting ages against incomes for each person, where each dot represents a person and the axes represent different attributes of those people.

The way you do that with a scatter plot is you call plt.scatter() using the two axes that you want to define, that is, the two attributes that contain data that you want to plot against each other.

Let's say I have a random distribution in X and Y and I scatter those on the scatter plot, and I show it:

```
from pylab import randn 
 
X = randn(500) 
Y = randn(500) 
plt.scatter(X,Y) 
plt.show() 
```

You get the following scatter plot as output:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-03-01/steps/2/13.png)


This is what it looks like, pretty cool. You can see the sort of a concentration in the center here, because of the normal distribution that's being used in both axes, but since it is random, there's no real correlation between those two.
