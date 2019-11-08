#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `CovarianceCorrelation.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/CovarianceCorrelation.ipynb

I'm going to start by doing this the hard way. NumPy does have a method to just compute the covariance for you, and we'll talk about that later, but for now I want to show that you can actually do this from first principles:

```
%matplotlib inline 
 
import numpy as np 
from pylab import * 
 
def de_mean(x): 
    xmean = mean(x) 
    return [xi - xmean for xi in x] 
 
def covariance(x, y): 
    n = len(x) 
    return dot(de_mean(x), de_mean(y)) / (n-1) 
```

Covariance, again, is defined as the dot product, which is a measure of the angle between two vectors, of a vector of the deviations from the mean for a given set of data and the deviations from the mean for another given set of data for the same data's data points. We then divide that by n - 1 in this case, because we're actually dealing with a sample.

So de_mean(), our deviation from the mean function is taking in a set of data, x, actually a list, and it's computing the mean of that set of data. The return line contains a little bit of Python trickery for you. The syntax is saying, I'm going to create a new list, and go through every element in x, call it xi, and then return the difference between xi and the mean, xmean, for that entire dataset. This function returns a new list of data that represents the deviations from the mean for each data point.

My covariance() function will do that for both sets of data coming in, divided by the number of data points minus 1. Remember that thing about sample versus population in the previous chapter? Well, that's coming into play here. Then we can just use those functions and see what happens.
