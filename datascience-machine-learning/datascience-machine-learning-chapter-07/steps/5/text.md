
But let's do something a little bit more complicated with it and actually play around with movies, just based on their metadata. Let's see if we can actually figure out the nearest neighbors of a movie based on just the intrinsic values of those movies, for example, the ratings for it, the genre information for it:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/3/2.jpg)

In theory, we could recreate something similar to Customers Who Watched This Item Also Watched (the above image is a screenshot from Amazon) just using k-nearest Neighbors. And, I can take it one step further: once I identify the movies that are similar to a given movie based on the k-nearest Neighbors algorithm, I can let them all vote on a predicted rating for that movie.

That's what we're going to do in our next example. So you now have the concepts of KNN, k-nearest neighbors. Let's go ahead and apply that to an example of actually finding movies that are similar to each other and using those nearest neighbor movies to predict the rating for another movie we haven't seen before.

