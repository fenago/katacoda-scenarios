I have this wonderful matrix now that will give me the similarity score of any two movies to each other. It's kind of amazing, and very useful for what we're going to be doing. Now just like earlier, we have to deal with spurious results. So, I don't want to be looking at relationships that are based on a small amount of behavior information.

It turns out that the Pandas corr function actually has a few parameters you can give it. One is the actual correlation score method that you want to use, so I'm going to say use pearson correlation.

```
corrMatrix = userRatings.corr(method='pearson', min_periods=100) 
corrMatrix.head() 
```

You'll notice that it also has a min_periods parameter you can give it, and that basically says I only want you to consider correlation scores that are backed up by at least, in this example, 100 people that rated both movies. Running that will get rid of the spurious relationships that are based on just a handful of people. The following is the matrix that we get after running the code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/4.jpg)

It's a little bit different to what we did in the item similarities exercise where we just threw out any movie that was rated by less than 100 people. What we're doing here, is throwing out movie similarities where less than 100 people rated both of those movies, okay? So, you can see in the preceding matrix that we have a lot more NaN values.

In fact, even movies that are similar to themselves get thrown out, so for example, the movie 1-900 (1994) was, presumably, watched by fewer than 100 people so it just gets tossed entirely. The movie, 101 Dalmatians (1996) however, survives with a correlation score of 1, and there are actually no movies in this little sample of the dataset that are different from each other that had 100 people in common that watched both. But, there are enough movies that survive to get meaningful results.
