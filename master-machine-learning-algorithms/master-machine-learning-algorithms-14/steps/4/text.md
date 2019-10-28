The SVM model needs to be solved using an optimization procedure. You can use a numerical
optimization procedure to search for the coefficients of the hyperplane. This is inefficient and
is not the approach used in widely used SVM implementations like LIBSVM. If implementing
the algorithm as an exercise, you could use a variation of gradient descent called sub-gradient
descent.

There are specialized optimization procedures that re-formulate the optimization problem
to be a Quadratic Programming problem. The most popular method for fitting SVM is the
Sequential Minimal Optimization (SMO) method that is very efficient. It breaks the problem
down into sub-problems that can be solved analytically (by calculating) rather than numerically
(by searching or optimizing).