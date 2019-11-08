
Things look a little bit better now, so let's go ahead and basically make our new DataFrame of Star Wars recommendations, movies similar to Star Wars, where we only base it on movies that appear in this new DataFrame. So, we're going to use the join operation, to go ahead and join our original similarMovies DataFrame to this new DataFrame of only movies that have greater than 100 ratings, okay?

```
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity'])) 
df.head() 
```

In this code, we create a new DataFrame based on similarMovies where we extract the similarity column, join that with our movieStats DataFrame, which is our popularMovies DataFrame, and we look at the combined results. And, there we go with that output!

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/14/3.jpg)

Now we have, restricted only to movies that are rated by more than 100 people, the similarity score to Star Wars. So, now all we need to do is sort that using the following code:

```
df.sort_values(['similarity'], ascending=False)[:15] 
```

Here, we're reverse sorting it and we're just going to take a look at the first 15 results. If you run that now, you should see the following:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/14/4.jpg)

This is starting to look a little bit better! So, Star Wars (1977) comes out on top because it's similar to itself, The Empire Strikes Back (1980) is number 2, Return of the Jedi (1983) is number 3, Raiders of the Lost Ark (1981), number 4. You know, it's still not perfect, but these make a lot more sense, right? So, you would expect the three Star Wars films from the original trilogy to be similar to each other, this data goes back to before the next three films, and Raiders of the Lost Ark (1981) is also a very similar movie to Star Wars in style, and it comes out as number 4. So, I'm starting to feel a little bit better about these results. There's still room for improvement, but hey! We got some results that make sense, whoo-hoo!

Now, ideally, we'd also filter out Star Wars, you don't want to be looking at similarities to the movie itself that you started from, but we'll worry about that later! So, if you want to play with this a little bit more, like I said 100 was sort of an arbitrary cutoff for the minimum number of ratings. If you do want to experiment with different cutoff values, I encourage you to go back and do so. See what that does to the results. You know, you can see in the preceding table that the results that we really like actually had much more than 100 ratings in common. So, we end up with Austin Powers: International Man of Mystery (1997) coming in there pretty high with only 130 ratings so maybe 100 isn't high enough! Pinocchio (1940) snuck in at 101, not very similar to Star Wars, so, you might want to consider an even higher threshold there and see what it does.

**Note:**

Please keep in mind too, this is a very small, limited dataset that we used for experimentation purposes, and it's based on very old data, so you're only going to see older movies. So, interpreting these results intuitively might be a little bit challenging as a result, but not bad results.

Now let's move on and actually do full-blown item-based collaborative filtering where we recommend movies to people using a more complete system, we'll do that next.