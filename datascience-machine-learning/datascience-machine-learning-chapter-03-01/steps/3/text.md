#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for notebooks. Open and run `MatPlotLib.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/MatPlotLib.ipynb


```
%matplotlib inline 
 
from scipy.stats import norm 
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(-3, 3, 0.001) 
 
plt.plot(x, norm.pdf(x)) 
plt.show() 
```

So in this example, I import matplotlib.pyplot as plt, and with this, we can refer to it as plt from now on in this notebook. Then, I use np.arange(-3, 3, 0.001) to create an x-axis filled with values between -3 and 3 at increments of 0.001, and use pyplot's plot() function to plot x. The y function will be norm.pdf(x). So I'm going to create a probability density function with a normal distribution based on the x values, and I'm using the scipy.stats norm package to do that.

So tying it back into last chapter's look at probability density functions, here we are plotting a normal probability density function using matplotlib. So we just call pyplot's plot() method to set up our plot, and then we display it using plt.show(). When we run the previous code, we get the following output:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-03-01/steps/2/1.png)

That's what we get: a pretty little graph with all the default formatting.
