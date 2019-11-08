Let's talk about a few data mining and machine learning techniques that employers expect you to know about. We'll start with a really simple one called KNN for short. You're going to be surprised at just how simple a good supervised machine learning technique can be. Let's take a look!

KNN sounds fancy but it's actually one of the simplest techniques out there! Let's say you have a scatter plot and you can compute the distance between any two points on that scatter plot. Let's assume that you have a bunch of data that you've already classified, that you can train the system from. If I have a new data point, all I do is look at the KNN based on that distance metric and let them all vote on the classification of that new point.

Let's imagine that the following scatter plot is plotting movies. The squares represent science fiction movies, and the triangles represent drama movies. We'll say that this is plotting ratings versus popularity, or anything else you can dream up:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/3/1.jpg)

Here, we have some sort of distance that we can compute based on rating and popularity between any two points on the scatter plot. Let's say a new point comes in, a new movie that we don't know the genre for. What we could do is set K to 3 and take the 3 nearest neighbors to this point on the scatter plot; they can all then vote on the classification of the new point/movie.
