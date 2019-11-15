
And again, just like earlier, we use the wonderful pivot_table command in Pandas to construct a new DataFrame based on the information:

```
userRatings = ratings.pivot_table(index=['user_id'],
                                  columns=['title'],values='rating') 
userRatings.head() 
```

Here, each row is the user_id, the columns are made up of all the unique movie titles in my dataset, and each cell contains a rating:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/2.jpg)

What we end up with is this incredibly useful matrix shown in the preceding output, that contains users for every row and movies for every column. And we have basically every user rating for every movie in this matrix. So, user_id number 1, for example, gave 101 Dalmatians (1996) a 2-star rating. And, again all these NaN values represent missing data. So, that just indicates, for example, user_id number 1 did not rate the movie 1-900 (1994).

Again, it's a very useful matrix to have. If we were doing user-based collaborative filtering, we could compute correlations between each individual user rating vector to find similar users. Since we're doing item-based collaborative filtering, we're more interested in relationships between the columns. So, for example, doing a correlation score between any two columns, which will give us a correlation score for a given movie pair. So, how do we do that? It turns out that Pandas makes that incredibly easy to do as well.

It has a built-in corr function that will actually compute the correlation score for every column pair found in the entire matrix-it's almost like they were thinking of us.

```
corrMatrix = userRatings.corr() 
corrMatrix.head() 
```

Let's go ahead and run the preceding code. It's a fairly computationally expensive thing to do, so it will take a moment to actually come back with a result. But, there we have it!

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/3.jpg)

So, what do we have in the preceding output? We have here a new DataFrame where every movie is on the row, and in the column. So, we can look at the intersection of any two given movies and find their correlation score to each other based on this userRatings data that we had up here originally. How cool is that? For example, the movie 101 Dalmatians (1996) is perfectly correlated with itself of course, because it has identical user rating vectors. But, if you look at 101 Dalmatians (1996) movie's relationship to the movie 12 Angry Men (1957), it's a much lower correlation score because those movies are rather dissimilar, makes sense, right?