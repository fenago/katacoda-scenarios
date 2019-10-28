Let’s start with values of 0.0 for both coefficients.

```
B0 = 0.0
B1 = 0.0
y = 0.0 + 0.0 × x
```

We can calculate the error for a prediction as follows:

```
error = p(i) − y(i)
```

Where `p(i)` is the prediction for the i’th instance in our dataset and y(i) is the i’th output
variable for the instance in the dataset. We can now calculate the predicted value for y using
our starting point coefficients for the first training instance: **x = 1; y = 1.**

```
p(i) = 0.0 + 0.0 × 1
p(i) = 0 (12.5)
```

Using the predicted output, we can calculate our error:

```
error = (0 − 1)
error = −1
```

