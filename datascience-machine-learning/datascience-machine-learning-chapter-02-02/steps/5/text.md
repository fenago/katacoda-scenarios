Another distribution function you see pretty often is the exponential probability distribution function, where things fall off in an exponential manner.

When you talk about an exponential fall off, you expect to see a curve, where it's very likely for something to happen, near zero, but then, as you get farther away from it, it drops off very quickly. There's a lot of things in nature that behave in this manner.

To do that in Python, just like we had a function in scipy.stats for norm.pdf, we also have an expon.pdf, or an exponential probability distribution function to do that in Python, we can do the same syntax that we did for the normal distribution with an exponential distribution here as shown in the following code block:

```
from scipy.stats import expon 
import matplotlib.pyplot as plt 
 
x = np.arange(0, 10, 0.001) 
plt.plot(x, expon.pdf(x)) 
```

So again, in the above code, we just create our x values using the NumPy arange function to create a bunch of values between 0 and 10 with a step size of `0.001`. Then, we plot those x values against the y-axis, which is defined as the function `expon.pdf(x)`. The output looks like an exponential fall off. As shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/2/4.png)

