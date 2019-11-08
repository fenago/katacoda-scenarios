Now there is a way around this problem, called k-fold cross-validation, and we'll look at an example of this later in the book, but the basic concept is you train/test many times. So you actually split your data not into just one training set and one test set, but into multiple randomly assigned segments, k segments. That's where the k comes from. And you reserve one of those segments as your test data, and then you start training your model on the remaining segments and measure their performance against your test dataset. Then you take the average performance from each of those training sets' models' results and take their r-squared average score.

So this way, you're actually training on different slices of your data, measuring them against the same test set, and if you have a model that's overfitting to a particular segment of your training data, then it will get averaged out by the other ones that are contributing to k-fold cross-validation.

Here are the K-fold cross validation steps:

- Split your data into K randomly-assigned segments
- Reserve one segment as your test data
- Train on each of the remaining K-1 segments and measure their performance against the test set
- Take the average of the K-1 r-squared scores

This will make more sense later in the book, right now I would just like for you to know that this tool exists for actually making train/test even more robust than it already is. So let's go and actually play with some data and actually evaluate it using train/test next.

