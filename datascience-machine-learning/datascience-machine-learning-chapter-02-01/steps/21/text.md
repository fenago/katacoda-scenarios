
```
%matplotlib inline 
import numpy as np 
import matplotlib.pyplot as plt 
incomes = np.random.normal(100.0, 20.0, 10000) 
plt.hist(incomes, 50) 
plt.show() 
```

We use matplotlib to plot a histogram of some normally distributed random data, and we call it incomes. We're saying it's going to be centered around 100 (hopefully that's an hourly rate or something and not annual, or some weird denomination), with a standard deviation of 20 and 10,000 data points.

Let's go ahead and generate that by executing that above code block and plotting it as shown in the following graph:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/21/1.png)

We have 10,000 data points centered around 100. With a normal distribution and a standard deviation of 20, a measure of the spread of this data, you can see that the most common occurrence is around 100, and as we get further and further from that, things become less and less likely. The standard deviation point of 20 that we specified is around 80 and around 120. You can see in the histogram that this is the point where things start to fall off sharply, so we can say that things beyond that standard deviation boundary are unusual.