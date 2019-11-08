What we're going to do is create some fake income data, getting back to our example from the previous section. We're going to create some fake data where the typical American makes around $27,000 a year in this example, we're going to say that's distributed with a normal distribution and a standard deviation of 15,000. All numbers are completely made up, and if you don't know what normal distribution and standard deviation means yet, don't worry. I'm going to cover that a little later in the chapter, but I just want you to know what these different parameters represent in this example. It will make sense later on.

In our Python notebook, remember to import the NumPy package into Python, which makes computing mean, median, and mode really easy. We're going to use the import numpy as np directive, which means we can use np as a shorthand to call numpy from now on.

Then we're going to create a list of numbers called incomes using the np.random.normal function.

```
import numpy as np 
 
incomes = np.random.normal(27000, 15000, 10000) 
np.mean(incomes) 
```

The three parameters of the np.random.normal function mean I want the data centered around 27000, with a standard deviation of 15000, and I want python to make 10000 data points in this list.

Once I do that, I compute the average of those data points, or the mean by just calling np.mean on incomes which is my list of data. It's just that simple.

Let's go ahead and run that. Make sure you selected that code block and then you can hit the play button to actually execute it, and since there is a random component to these income numbers, every time I run it, I'm going to get a slightly different result, but it should always be pretty close to 27000.

```
Out[1]: 27173.098561362742
```

OK, so that's all there is to computing the mean in Python, just using NumPy (np.mean) makes it super easy. You don't have to write a bunch of code or actually add up everything and count up how many items you had and do the division. NumPy mean, does all that for you.