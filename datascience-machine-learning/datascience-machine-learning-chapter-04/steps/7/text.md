
So how do I know how good my regression is? How well does my line fit my data? That's where r-squared comes in, and r-squared is also known as the coefficient of determination. Again, someone trying to sound smart might call it that, but usually it's called r-squared.

It is the fraction of the total variation in Y that is captured by your models. So how well does your line follow that variation that's happening? Are we getting an equal amount of variance on either side of your line or not? That's what r-squared is measuring.

Computing r-squared
To actually compute the value, take 1 minus the sum of the squared errors over the sum of the squared variations from the mean:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/3.png)

So, it's not very difficult to compute, but again, Python will give you functions that will just compute that for you, so you'll never have to actually do that math yourself.
