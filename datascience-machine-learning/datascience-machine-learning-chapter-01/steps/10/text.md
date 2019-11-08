Let's move on to data structures. If you need to pause and let things sink in a little bit, or you want to play around with these a little bit more, feel free to do so. The best way to learn this stuff is to dive in and actually experiment, so I definitely encourage doing that, and that's why I'm giving you working IPython/Jupyter Notebooks, so you can actually go in, mess with the code, do different stuff with it.

For example, here we have a distribution around 25.0, but let's make it around 55.0:

```
import numpy as np
A = np.random.normal(55.0, 5.0, 10)
print (A)
```

Hey, all my numbers changed, they're closer to 55 now, how about that?

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/10/1.png)

Alright, let's talk about data structures a little bit here. As we saw in our first example, you can have a list, and the syntax looks like this.