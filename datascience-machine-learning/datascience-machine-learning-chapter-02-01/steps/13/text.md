Calculating mode using the SciPy package
Finally, let's look at mode. We will just generate a bunch of random integers, 500 of them to be precise, that range between 18 and 90. We're going to create a bunch of fake ages for people.

```
ages = np.random.randint(18, high=90, size=500) 
ages 
```

Your output will be random, but should look something like the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/13/1.png)

Now, SciPy, kind of like NumPy, is a bunch of like handy-dandy statistics functions, so we can import stats from SciPy using the following syntax. It's a little bit different than what we saw before.

```
from scipy import stats 
stats.mode(ages) 
```

The code means, from the scipy package import stats, and I'm just going to refer to the package as stats, Tha means that I don't need to have an alias like I did before with NumPy, just different way of doing it. Both ways work. Then, I used the stats.mode function on ages, which is our list of random ages. When we execute the above code, we get the following output:

```
Out[11]: ModeResult(mode=array([39]), count=array([12])) 
```

So in this case, the actual mode is 39 that turned out to be the most common value in that array. It actually occurred 12 times.

Now if I actually create a new distribution, I would expect a completely different answer because this data really is completely random what these numbers are. Let's execute the above code blocks again to create a new distribution.

```
ages = np.random.randint(18, high=90, size=500) 
ages

from scipy import stats 
stats.mode(ages) 
```

The output for randomizing the equation is as distribution is as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-02-01/steps/13/2.png)

Make sure you selected that code block and then you can hit the play button to actually execute it.

In this case, the mode ended up being the number 29, which occurred 14 times.

```
Out[11]: ModeResult(mode=array([29]), count=array([14]))
```

So, it's a very simple concept. You can do it a few more times just for fun. It's kind of like rolling the roulette wheel. We'll create a new distribution again.

There you have it, mean, median, and mode in a nutshell. It's very simple to do using the SciPy and NumPy packages.