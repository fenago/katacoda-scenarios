
Now we're going to try to fit an 8th degree polynomial to this data, and we'll just pick the number 8 at random because I know it's a really high order and is probably overfitting.

Let's go ahead and fit our 8th degree polynomial using np.poly1d(np.polyfit(x, y, 8)), where x is an array of the training data only, and y is an array of the training data only. We are finding our model using only those 80 points that we reserved for training. Now we have this p4 function that results that we can use to predict new values:

```
x = np.array(trainX) 
y = np.array(trainY) 
 
p4 = np.poly1d(np.polyfit(x, y, 8)) 
```

Now we'll plot the polynomial this came up with against the training data. We can scatter our original data for the training data set, and then we can plot our predicted values against them:

```
import matplotlib.pyplot as plt 
 
xp = np.linspace(0, 7, 100) 
axes = plt.axes() 
axes.set_xlim([0,7]) 
axes.set_ylim([0, 200]) 
plt.scatter(x, y) 
plt.plot(xp, p4(xp), c='r') 
plt.show() 
```

You can see in the following graph that it looks like a pretty good fit, but you know that clearly it's doing some overfitting:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/11/3.jpg)
