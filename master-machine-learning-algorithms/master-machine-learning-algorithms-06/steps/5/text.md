LDA makes some simplifying assumptions about your data
- That your data is Gaussian, that each variable is shaped like a bell curve when plotted.
- That each attribute has the same variance, that values of each variable vary around the
mean by the same amount on average.
With these assumptions, the LDA model estimates the mean and variance from your data
for each class. It is easy to think about this in the univariate (single input variable) case with
two classes. The mean (mean) value of each input (x) for each class (k) can be estimated in
the normal way by dividing the sum of values by the total number of values.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/5/1.JPG)

Where sigma2 is the variance across all inputs (x), n is the number of instances, K is the
number of classes and meank is the mean of x for the class to which xi belongs. Put another
way, we calculate the squared difference of each value from the mean within the class groups but
average these differences across all class groups. Remember that when we talk about variance that the units are squared units, not that we need to square the
variance value.
