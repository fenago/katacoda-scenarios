Logistic regression is a simple and powerful linear classification algorithm. It also has limitations
that suggest at the need for alternate linear classification algorithms.
- **Two-Class Problems.** Logistic regression is intended for two-class or binary classification
problems. It can be extended for multiclass classification, but is rarely used for this purpose.
- **Unstable With Well Separated Classes.** Logistic regression can become unstable
when the classes are well separated.
- **Unstable With Few Examples.** Logistic regression can become unstable when there
are few examples from which to estimate the parameters.

An unstable model here refs to the spectrum from poor results to a model that may not
reliably converge on a set of coefficients. Linear discriminant analysis does address each of these
points and is the go-to linear method for multiclass classification problems. Even with binaryclassification problems, it is a good idea to try both logistic regression and linear discriminant
analysis.