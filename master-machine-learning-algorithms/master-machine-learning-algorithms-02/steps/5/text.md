The goal is to find the best estimates for the coefficients to minimize the errors in predicting
y from x. Simple regression is great, because rather than having to search for values by trial
and error or calculate them analytically using more advanced linear algebra, we can estimate11.2. Simple Linear Regression 42
them directly from our data. We can start off by estimating the value for B1 as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/5/1.JPG)

Where mean() is the average value for the variable in our dataset. The xi and yi refer to
the fact that we need to repeat these calculations across all values in our dataset and i refers to
the i’th value of x or y. We can calculate B0 using B1 and some statistics from our dataset, as
follows:

```
B0 = mean(y) − B1 × mean(x)
```

Not that bad right? We can calculate these right in our spreadsheet.