
What the createClusteredData() function does here, is to create a bunch of random data for people that are clustered around k points, based on age and income, and it returns two arrays. The first array is the feature array, that we're calling X, and then we have the array of the thing we're trying to predict for, which we're calling y. A lot of times in scikit-learn when you're creating a model that you can predict from, those are the two inputs that it will take, a list of feature vectors, and the thing that you're trying to predict, that it can learn from. So, we'll go ahead and run that.

So now we're going to use the createClusteredData() function to create 100 random people with 5 different clusters. We will just create a scatter plot to illustrate those, and see where they land up:

```
%matplotlib inline 
from pylab import * 
 
(X, y) = createClusteredData(100, 5) 
 
plt.figure(figsize=(8, 6)) 
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float)) 
plt.show() 
```

The following graph shows our data that we're playing with. Every time you run this you're going to get a different set of clusters. So, you know, I didn't actually use a random seed... to make life interesting.

A couple of new things here--I'm using the figsize parameter on plt.figure() to actually make a larger plot. So, if you ever need to adjust the size in matplotlib, that's how you do it. I'm using that same trick of using the color as the classification number that I end up with. So the number of the cluster that I started with is being plotted as the color of these data points. You can see, it's a pretty challenging problem, there's definitely some intermingling of clusters here:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-03/steps/9/1.jpg)
