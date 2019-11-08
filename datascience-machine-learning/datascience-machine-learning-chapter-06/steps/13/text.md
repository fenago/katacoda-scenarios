
Now the real magic of Pandas comes in. So, what we really want is to look at relationships between movies based on all the users that watched each pair of movies, so we need, at the end, a matrix of every movie, and every user, and all the ratings that every user gave to every movie. The pivot_table command in Pandas can do that for us. It can basically construct a new table from a given DataFrame, pretty much any way that you want it. For this, we can use the following code:

```
movieRatings = ratings.pivot_table(index=['user_id'],
                                   columns=['title'],values='rating') 
movieRatings.head() 
```

So, what we're saying with this code is-take our ratings DataFrame and create a new DataFrame called movieRatings and we want the index of it to be the user IDs, so we'll have a row for every user_id, and we're going to have every column be the movie title. So, we're going to have a column for every title that we encounter in that DataFrame, and each cell will contain the rating value, if it exists. So, let's go ahead and run it.

And, we end up with a new DataFrame that looks like the following table:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/3.png)

It's kind of amazing how that just put it all together for us. Now, you'll see some NaN values, which stands for Not a Number, and its just how Pandas indicates a missing value. So, the way to interpret this is, user_id number 1, for example, did not watch the movie 1-900 (1994), but user_id number 1 did watch 101 Dalmatians (1996) and rated it 2 stars. The user_id number 1 also watched 12 Angry Men (1957) and rated it 5 stars, but did not watch the movie 2 Days in the Valley (1996), for example, okay? So, what we end up with here is a sparse matrix basically, that contains every user, and every movie, and at every intersection where a user rated a movie there's a rating value.

So, you can see now, we can very easily extract vectors of every movie that our user watched, and we can also extract vectors of every user that rated a given movie, which is what we want. So, that's useful for both user-based and item-based collaborative filtering, right? If I wanted to find relationships between users, I could look at correlations between these user rows, but if I want to find correlations between movies, for item-based collaborative filtering, I can look at correlations between columns based on the user behavior. So, this is where the real flipping things on its head for user versus item-based similarities comes into play.

Now, we're going with item-based collaborative filtering, so we want to extract columns, to do this let's run the following code:

```
starWarsRatings = movieRatings['Star Wars (1977)'] 
starWarsRatings.head() 
```

Now, with the help of that, let's go ahead and extract all the users who rated Star Wars (1977):

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/4.png)

And, we can see most people have, in fact, watched and rated Star Wars (1977) and everyone liked it, at least in this little sample that we took from the head of the DataFrame. So, we end up with a resulting set of user IDs and their ratings for Star Wars (1977). The user ID 3 did not rate Star Wars (1977) so we have a NaN value, indicating a missing value there, but that's okay. We want to make sure that we preserve those missing values so we can directly compare columns from different movies. So, how do we do that?

The corrwith function
Well, Pandas keeps making it easy for us, and has a corrwith function that you can see in the following code that we can use:

```
similarMovies = movieRatings.corrwith(starWarsRatings) 
similarMovies = similarMovies.dropna() 
df = pd.DataFrame(similarMovies) 
df.head(10) 
```

That code will go ahead and correlate a given column with every other column in the DataFrame, and compute the correlation scores and give that back to us. So, what we're doing here is using corrwith on the entire movieRatings DataFrame, that's that entire matrix of user movie ratings, correlating it with just the starWarsRatings column, and then dropping all of the missing results with dropna. So, that just leaves us with items that had a correlation, where there was more than one person that viewed it, and we create a new DataFrame based on those results and then display the top 10 results. So again, just to recap:

We're going to build the correlation score between Star Wars and every other movie.
Drop all the NaN values, so that we only have movie similarities that actually exist, where more than one person rated it.
And, we're going to construct a new DataFrame from the results and look at the top 10 results.
And here we are with the results shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/5.png)

We ended up with this result of correlation scores between each individual movie for Star Wars and we can see, for example, a surprisingly high correlation score with the movie 'Til There Was You (1997), a negative correlation with the movie 1-900 (1994), and a very weak correlation with 101 Dalmatians (1996).

Now, all we should have to do is sort this by similarity score, and we should have the top movie similarities for Star Wars, right? Let's go ahead and do that.

```
similarMovies.sort_values(ascending=False)
```

Just call sort_values on the resulting DataFrame, again Pandas makes it really easy, and we can say ascending=False, to actually get it sorted in reverse order by correlation score. So, let's do that:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/6.png)

Okay, so Star Wars (1977) came out pretty close to top, because it is similar to itself, but what's all this other stuff? What the heck? We can see in the preceding output, some movies such as: Full Speed (1996), Man of the Year (1995), The Outlaw (1943). These are all, you know, fairly obscure movies, that most of them I've never even heard of, and yet they have perfect correlations with Star Wars. That's kinda weird! So, obviously we're doing something wrong here. What could it be?

Well, it turns out there's a perfectly reasonable explanation, and this is a good lesson in why you always need to examine your results when you're done with any sort of data science task-question the results, because often there's something you missed, there might be something you need to clean in your data, there might be something you did wrong. But you should also always look skeptically at your results, don't just take them on faith, okay? If you do so, you're going to get in trouble, because if I were to actually present these as recommendations to people who liked Star Wars, I would get fired. Don't get fired! Pay attention to your results! So, let's dive into what went wrong in our next section.

