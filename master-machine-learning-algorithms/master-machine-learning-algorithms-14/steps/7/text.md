This section describes the form of the SVM model and how it can be learned using a variant of
the gradient descent optimization procedure.

#### Form of Linear SVM Model
The Linear SVM model is a line and the goal of the learning algorithm is to find values for the
coefficients that best separates the classes. The line is typically in the form (grouping the terms
for readability):

```
B0 + (B1 × X1) + (B2 × X2) = 0
```

Where B0, B1 and B2 are the coefficients and X1 and X2 are the input variables. This
will be the form of the equation that we will be using with one small modification, we will drop
the bias term (B0) also called the offset or the intercept. For example B0 = 0.

```
(B1 × X1) + (B2 × X2) = 0
```

This means that the line will pass through the origin (X1 = 0 and X2 = 0). This is just to
make the tutorial easier to follow and because our simple problem does not really need it, you
can add the bias term back in if you like.
