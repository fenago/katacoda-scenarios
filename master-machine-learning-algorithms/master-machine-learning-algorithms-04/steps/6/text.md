Making predictions with a logistic regression model is as simple as plugging in numbers into the
logistic regression equation and calculating a result. Let’s make this concrete with a specific
example. Let’s say we have a model that can predict whether a person is male or female based
on their height (completely fictitious). Given a height of 150 cm is the person male or female?
We have learned the coefficients of B0 = −100 and B1 = 0.6. Using the equation above we can
calculate the probability of male given a height of 150 cm or more formally P(malejheight = 150).
We will use EXP() for e, because that is what you can use if you type this example into your
spreadsheet:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-04/steps/6/1.JPG)

Or a probability of near zero that the person is a male. In practice we can use the probabilities
directly. Because this is classification and we want a crisp answer, we can snap the probabilities
to a binary class value, for example:

```
prediction = 0 IF p(male) < 0.5
prediction = 1 IF p(male) ≥ 0.5
```

Now that we know how to make predictions using logistic regression, let’s look at how we
can prepare our data to get the most from the technique.