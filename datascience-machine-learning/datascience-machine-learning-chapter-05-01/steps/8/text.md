
You can then measure quantitatively how well it did using r-squared or some other metric, like root-mean-square error, for example. You can use that to test one model versus another and see what the best model is for a given problem. You can tune the parameters of that model and use train/test to maximize the accuracy of that model on your testing data. So this is a great way to prevent overfitting.

There are some caveats to supervised learning. need to make sure that both your training and test datasets are large enough to actually be representative of your data. You also need to make sure that you're catching all the different categories and outliers that you care about, in both training and testing, to get a good measure of its success, and to build a good model.

You have to make sure that you've selected from those datasets randomly, and that you're not just carving your dataset in two and saying everything left of here is training and right here is testing. You want to sample that randomly, because there could be some pattern sequentially in your data that you don't know about.

Now, if your model is overfitting, and just going out of its way to accept outliers in your training data, then that's going to be revealed when you put it against unset scene of testing data. This is because all that gyrations for outliers won't help with the outliers that it hasn't seen before.

Let's be clear here that train/test is not perfect, and it is possible to get misleading results from it. Maybe your sample sizes are too small, like we already talked about, or maybe just due to random chance your training data and your test data look remarkably similar, they actually do have a similar set of outliers - and you can still be overfitting. As you can see in the following example, it really can happen:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/8/1.jpg)
