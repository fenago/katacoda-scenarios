Let’s start with the top part of the equation, the numerator. First we need to calculate the
mean value of x and y. The mean is calculated as:


Where n is the number of values (5 in this case). You can use the AVERAGE() function in
your spreadsheet. Let’s calculate the mean value of our x and y variables:

```
mean(x) = 3
mean(y) = 2.8
```

Now we need to calculate the error of each variable from the mean. Let’s do this with x first:

x | mean(x) | x - mean(x)
--- | --- | ---
1   | 3  | -2
2   |    | -1
4   |    | 1
3   |    | 0
5   |    | 2

Residual of each x value from the mean.

Now let’s do that for the y variable.

y | mean(y) | y - mean(y)
--- | --- | ---
1   |  2.8 | -1.8
3   |    |  0.2
3   |    |  0.2
2   |    |  -0.8
5   |    |  2.2

Residual of each y value from the mean.
