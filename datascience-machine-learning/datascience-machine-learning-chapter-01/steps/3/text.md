Let's take a quick look at this code while we're here. We are setting up a little income distribution in this code. We're simulating the distribution of income in a population of people, and to illustrate the effect that an outlier can have on that distribution, we're simulating Donald Trump entering the mix and messing up the mean value of the income distribution. By the way, I'm not making a political statement, this was all done before Trump became a politician. So you know, full disclosure there.

We can select any code block in the notebook by clicking on it. So if you now click in the code block that contains the code we just looked at above, we can then hit the run button at the top to run it. Here's the area at the top of the screen where you'll find the Run button:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/3/1.png)

Hitting the Run button with the code block selected, will cause this graph to be regenerated:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-01/steps/3/2.png)

Similarly, we can click on the next code block a little further down, you'll spot the one which has the following single line of code :

```
incomes.mean() 
```

If you select the code block containing this line, and hit the Run button to run the code, you'll see the output below it, which ends up being a very large value because of the effect of that outlier, something like this:

```
127148.50796177129
```

