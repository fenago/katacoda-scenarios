Let's play around in Python and actually compute these moments and see how you do that. To play around with this, go ahead and open up the `Moments.ipynb`, and you can follow along with me here.

#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `Moments.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/Moments.ipynb

Let's again create that same normal distribution of random data. Again, we're going to make it centered around zero, with a 0.5 standard deviation and 10,000 data points, and plot that out:

```
import numpy as np 
import matplotlib.pyplot as plt 
 
vals = np.random.normal(0, 0.5, 10000) 
 
plt.hist(vals, 50) 
plt.show()
```

So again, we get a randomly generated set of data with a normal distribution around zero.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/9/7.png)

Now, we find the mean and variance. We've done this before; NumPy just gives you a mean and var function to compute that. So, we just call np.mean to find the first moment, which is just a fancy word for the mean, as shown in the following code:

```
np.mean(vals)
```

This gives the following output in our example:

```
Out [2]:-0.0012769999428169742
```

The output turns out to be very close to zero, just like we would expect for normally distributed data centered around zero. So, the world makes sense so far.

Now we find the second moment, which is just another name for variance. We can do that with the following code, as we've seen before:

```
np.var(vals)
```

Providing the following output:

```
Out[3]:0.25221246428323563
```

That output turns out to be about 0.25, and again, that works out with a nice sanity check. Remember that standard deviation is the square root of variance. If you take the square root of 0.25, it comes out to 0.5, which is the standard deviation we specified while creating this data, so again, that checks out too.
