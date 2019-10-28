The optimization algorithm to find the coefficients can be stated as a quadratic programming
problem. This is a type of constraint optimization where fast solvers can be used. We will not
be using this approach in this tutorial. Another approach that can be used to discover the
coefficient values for Linear SVM is sub-gradient descent. In this method a random training27.3. Learn an SVM Model from Training Data 122
pattern is selected each iteration and used to update the coefficients. After a large number
of iterations (thousands or hundreds of thousands) the algorithm will settle on a stable set of
coefficients. The coefficient update equation works as follows. First an output value is calculated
as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/8/1.JPG)

Two different update procedures are used depending on the output value. If the output
value is greater than 1 it suggests that the training pattern was not a support vector. This
means that the instance was not directly involved in calculating the output, in which case the
weights are slightly decreased:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/8/2.JPG)

Where b is the weight that is being updated (such as B1 or B2), t is the current iteration
(e.g. 1 for the first update, 2 for the second and so on). If the output is less than 1 then it is
assumed that the training instance is a support vector and must be updated to better explain
the data.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/8/3.JPG)

Where b is the weight that is being updated, t is the current iteration and lambda is a
parameter to the learning algorithm. The lambda is a learning parameter and is often set to
very small values such as 0.0001 or smaller. The procedure is repeated until the error rate drops
to a desirable level or for a very large fixed number of iterations. Smaller learning rates ofter
require much longer training times. The number of iterations is a downside to this learning
algorithm.