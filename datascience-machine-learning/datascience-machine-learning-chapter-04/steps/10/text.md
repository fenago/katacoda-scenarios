
Now let's see if we can tease that out and find the best fit line using ordinary least squares. We talked about how to do ordinary least squares and linear regression, but you don't have to do any of that math yourself because the SciPy package has a stats package that you can import:

```
from scipy import stats

slope, intercept, r_value, p_value, std_err =     
stats.linregress(pageSpeeds, purchaseAmount) 
```

You can import stats from scipy, and then you can just call stats.linregress() on your two features. So, we have a list of page speeds (pageSpeeds) and a corresponding list of purchase amounts (purchaseAmount). The linregress() function will give us back a bunch of stuff, including the slope, the intercept, which is what I need to define my best fit line. It also gives us the r_value, from which we can get r-squared to measure the quality of that fit, and a couple of things that we'll talk about later on. For now, we just need slope, intercept, and r_value, so let's go ahead and run these. We'll begin by finding the linear regression best fit:

```
r_value ** 2
```

This is what your output should look like:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/5-0.png)

Now the r-squared value of the line that we got back is 0.99, that's almost 1.0. That means we have a really good fit, which isn't too surprising because we made sure there was a real linear relationship between this data. Even though there is some variance around that line, our line captures that variance. We have roughly the same amount of variance on either side of the line, which is a good thing. It tells us that we do have a linear relationship and our model is a good fit for the data that we have.

Let's plot that line:

```
import matplotlib.pyplot as plt
def predict(x):
return slope * x + intercept
fitLine = predict(pageSpeeds)
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()
```

The following is the output to the preceding code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/5.png)

This little bit of code will create a function to draw the best fit line alongside the data. There's a little bit more Matplotlib magic going on here. We're going to make a fitLine list and we're going to use the predict() function we wrote to take the pageSpeeds,which is our x-axis, and create the Y function from that. So instead of taking the observations for amount spent, we're going to find the predicted ones just using the slope times x plus the intercept that we got back from the linregress() call above. Essentially here, we're going to do a scatter plot like we did before to show the raw data points, which are the observations.

Then we're also going to call plot on that same pyplot instance using our fitLine that we created using the line equation that we got back, and show them all both together. When we do that, it looks like the following graph:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/6.png)

You can see that our line is in fact a great fit for our data! It goes right smack down the middle, and all you need to predict new values is this predict function. Given a new previously unseen page speed, we could predict the amount spent just using the slope times the page speed plus the intercept. That's all there is to it, and I think it's great!
