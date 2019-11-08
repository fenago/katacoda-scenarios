
We have included the data files that you need from the GroupLens dataset with the course materials, and the first thing we need to do is import those into a Pandas DataFrame, and we're really going to see the full power of Pandas in this example. It's pretty cool stuff!

Understanding the code
The first thing we're going to do is import the u.data file as part of the MovieLens dataset, and that is a tab-delimited file that contains every rating in the dataset.

```
import pandas as pd 
 
r_cols = ['user_id', 'movie_id', 'rating'] 
ratings = pd.read_csv('e:/sundog-consult/packt/datascience/ml-100k/u.data',  
                      sep='\\t', names=r_cols, usecols=range(3)) 
```
                      
**Note:** that you'll need to add the path here to where you stored the downloaded MovieLens files on your computer. So, the way that this works is even though we're calling read_csv on Pandas, we can specify a different separator than a comma. In this case, it's a tab.

We're basically saying take the first three columns in the u.data file, and import it into a new DataFrame, with three columns: user_id, movie_id, and rating.

What we end up with here is a DataFrame that has a row for every user_id, which identifies some person, and then, for every movie they rated, we have the movie_id, which is some numerical shorthand for a given movie, so Star Wars might be movie 53 or something, and their rating, you know, 1 to 5 stars. So, we have here a database, a DataFrame, of every user and every movie they rated, okay?

Now, we want to be able to work with movie titles, so we can interpret these results more intuitively, so we're going to use their human-readable names instead.

If you're using a truly massive dataset, you'd save that to the end because you want to be working with numbers, they're more compact, for as long as possible. For the purpose of example and teaching, though, we'll keep the titles around so you can see what's going on.

```
m_cols = ['movie_id', 'title'] 
movies = pd.read_csv('e:/sundog-consult/packt/datascience/ml-100k/u.item', 
                     sep='|', names=m_cols, usecols=range(2)) 
```

There's a separate data file with the MovieLens dataset called u.item, and it is pipe-delimited, and the first two columns that we import will be the movie_id and the title of that movie. So, now we have two DataFrames: r_cols has all the user ratings and m_cols has all the titles for every movie_id. We can then use the magical merge function in Pandas to mush it all together.

```
ratings = pd.merge(movies, ratings) 
```

Let's add a ratings.head() command and then run those cells. What we end up with is something like the following table. That was pretty quick!

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/2.png)

We end up with a new DataFrame that contains the user_id and rating for each movie that a user rated, and we have both the movie_id and the title that we can read and see what it really is. So, the way to read this is user_id number 308 rated the Toy Story (1995) movie 4 stars, user_id number 287 rated the Toy Story (1995) movie 5 stars, and so on and so forth. And, if we were to keep looking at more and more of this DataFrame, we'd see different ratings for different movies as we go through it.
