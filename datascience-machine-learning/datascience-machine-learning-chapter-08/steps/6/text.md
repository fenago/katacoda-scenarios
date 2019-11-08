Earlier in the book, we talked about train and test as a good way of preventing overfitting and actually measuring how well your model can perform on data it's never seen before. We can take that to the next level with a technique called k-fold cross-validation. So, let's talk about this powerful tool in your arsenal for fighting overfitting; k-fold cross-validation and learn how that works.

To recall from train/test, the idea was that we split all of our data that we're building a machine learning model based off of into two segments: a training dataset, and a test dataset. The idea is that we train our model only using the data in our training dataset, and then we evaluate its performance using the data that we reserved for our test dataset. That prevents us from overfitting to the data that we have because we're testing the model against data that it's never seen before.

However, train/test still has its limitations: you could still end up overfitting to your specific train/test split. Maybe your training dataset isn't really representative of the entire dataset, and too much stuff ended up in your training dataset that skews things. So, that's where k-fold cross-validation comes in, it takes train/test and kicks it up a notch.

The idea, although it sounds complicated, is fairly simple:

- Instead of dividing our data into two buckets, one for training and one for testing, we divide it into K buckets.
- We reserve one of those buckets for testing purposes, for evaluating the results of our model.
- We train our model against the remaining buckets that we have, K-1, and then we take our test dataset and use that to evaluate how well our model did amongst all of those different training datasets.
- We average those resulting error metrics, that is, those r-squared values, together to get a final error metric from k-fold cross-validation.

That's all it is. It is a more robust way of doing train/test, and that's one way of doing it.

Now, you might think to yourself well, what if I'm overfitting to that one test dataset that I reserved? I'm still using the same test dataset for every one of those training datasets. What if that test dataset isn't really representative of things either?

There are variations of k-fold cross-validation that will randomize that as well. So, you could randomly pick what the training dataset is as well each time around, and just keep randomly assigning things to different buckets and measuring the results. But usually, when people talk about k-fold cross-validation, they're talking about this specific technique where you reserve one bucket for testing, and the remaining buckets for training, and you evaluate all of your training datasets against the test dataset when you build a model for each one.
