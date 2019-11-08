Let's look at some more examples of percentiles using Python and kind of get our hands on it and conceptualize this a little bit more. Go ahead and open the Percentiles.ipynb file if you'd like to follow along.

#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for notebooks. Open and run `Percentiles.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/Percentiles.ipynb


Let's start off by generating some randomly distributed normal data, or normally distributed random data, rather, refer to the following code block:

```
%matplotlib inline 
import numpy as np 
import matplotlib.pyplot as plt 
 
vals = np.random.normal(0, 0.5, 10000) 
 
plt.hist(vals, 50) 
plt.show() 
```

In this example, what we're going to do is generate some data centered around zero, that is with a mean of zero, with a standard deviation of 0.5, and I'm going to make 10000 data points with that distribution. Then, we're going to plot a histogram and see what we come up with.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/9/3.png)

The generated histogram looks very much like a normal distribution, but because there is a random component we have a little outlier near the deviation of -2 in this example here. Things are tipped a little bit at the mean, a little bit of random variation there to make things interesting.
