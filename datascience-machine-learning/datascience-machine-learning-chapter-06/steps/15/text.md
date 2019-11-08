
We can say that we want to aggregate specifically on the rating, and we want to show both the size, the number of ratings for each movie, and the mean average score, the mean rating for that movie. So, when we do that, we end up with something like the following:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/14/1.jpg)

This is telling us, for example, for the movie 101 Dalmatians (1996), 109 people rated that movie and their average rating was 2.9 stars, so not that great of a score really! So, if we just eyeball this data, we can say okay well, movies that I consider obscure, like 187 (1997), had 41 ratings, but 101 Dalmatians (1996), I've heard of that, you know 12 Angry Men (1957), I've heard of that. It seems like there's sort of a natural cutoff value at around 100 ratings, where maybe that's the magic value where things start to make sense.

Let's go ahead and get rid of movies rated by fewer than 100 people, and yes, you know I'm kind of doing this intuitively at this point. As we'll talk about later, there are more principled ways of doing this, where you could actually experiment and do train/test experiments on different threshold values, to find the one that actually performs the best. But initially, let's just use our common sense and filter out movies that were rated by fewer than 100 people. Again, Pandas makes that really easy to do. Let's figure it out with the following example:

```
popularMovies = movieStats['rating']['size'] >= 100 
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15] 
```

We can just say popularMovies, a new DataFrame, is going to be constructed by looking at movieStats and we're going to only take rows where the rating size is greater than or equal to 100, and I'm then going to sort that by mean rating, just for fun, to see the top rated, widely watched movies.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/14/2.jpg)

What we have here is a list of movies that were rated by more than 100 people, sorted by their average rating score, and this in itself is a recommender system. These are highly-rated popular movies. A Close Shave (1995), apparently, was a really good movie and a lot of people watched it and they really liked it.

So again, this is a very old dataset, from the late 90s, so even though you might not be familiar with the film A Close Shave (1995), it might be worth going back and rediscovering it; add it to your Netflix! Schindler's List (1993) not a big surprise there,that comes up on the top of most top movies lists. The Wrong Trousers (1993), another example of an obscure film that apparently was really good and was also pretty popular. So,some interesting discoveries there already, just by doing that.
