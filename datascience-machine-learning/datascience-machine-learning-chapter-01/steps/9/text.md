Python itself, like any language, is fairly limited in what it can do. The real power of using Python for machine learning and data mining and data science is the power of all the external libraries that are available for it for that purpose. One of those libraries is called NumPy, or numeric Python, and, for example, here we can import the Numpy package, which is included with Canopy as np.

This means that I'll refer to the NumPy package as np, and I could call that anything I want. I could call it Fred or Tim, but it's best to stick with something that actually makes sense; now that I'm calling that NumPy package np, I can refer to it using np:

```
import numpy as np
```

In this example, I'll call the random function that's provided as part of the NumPy package and call its normal function to actually generate a normal distribution of random numbers using these parameters and print them out. Since it is random, I should get different results every time:

```
import numpy as np
A = np.random.normal(25.0, 5.0, 10)
print (A)
```

The output should look like this:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/9/1.png)

Sure enough, I get different results. That's pretty cool.