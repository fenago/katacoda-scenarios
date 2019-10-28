Linear regression is been studied at great length, and there is a lot of literature on how your
data must be structured to make best use of the model. As such, there is a lot of sophistication
when talking about these requirements and expectations which can be intimidating. In practice,
you can use these rules more as rules of thumb when using Ordinary Least Squares Regression,
the most common implementation of linear regression. Try different preparations of your data
using these heuristics and see what works best for your problem.

- **Linear Assumption.** Linear regression assumes that the relationship between your input
and output is linear. It does not support anything else. This may be obvious, but it is
good to remember when you have a lot of attributes. You may need to transform data to
make the relationship linear (e.g. log transform for an exponential relationship).
- **Remove Noise.** Linear regression assumes that your input and output variables are
not noisy. Consider using data cleaning operations that let you better expose and clarify
the signal in your data. This is most important for the output variable and you want to
remove outliers in the output variable (y) if possible.
- **Remove Collinearity.** Linear regression will overfit your data when you have highly
correlated input variables. Consider calculating pairwise correlations for your input data
and removing the most correlated.
- **Gaussian Distributions.** Linear regression will make more reliable predictions if your
input and output variables have a Gaussian distribution. You may get some benefit
using transforms (e.g. log or BoxCox) on your variables to make their distribution more
- **Rescale Inputs:** Linear regression will often make more reliable predictions if you rescale
input variables using standardization or normalization.