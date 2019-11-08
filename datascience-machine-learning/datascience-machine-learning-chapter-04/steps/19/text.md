Now we can measure the r-squared error. By taking the y and the predicted values (p4(x)) in the r2_score() function that we have in sklearn.metrics, we can compute that.

```
from sklearn.metrics import r2_score
r2 = r2_score(y, p4(x))

print r2
```

The output is as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-04/9-0.png)

Our code compares a set of observations to a set of predictions and computes r-squared for you, and with just one line of code! Our r-squared for this turns out to be 0.829, which isn't too bad. Remember, zero is bad, one is good. 0.82 is to pretty close to one, not perfect, and intuitively, that makes sense. You can see that our line is pretty good in the middle section of the data, but not so good out at the extreme left and not so good down at the extreme right. So, 0.82 sounds about right.

