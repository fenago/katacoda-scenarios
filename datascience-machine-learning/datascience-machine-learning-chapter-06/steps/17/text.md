Okay, let's actually build a full-blown recommender system that can look at all the behavior information of everybody in the system, and what movies they rated, and use that to actually produce the best recommendation movies for any given user in our dataset. Kind of amazing and you'll be surprised how simple it is. Let's go!

#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `ItemBasedCF.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/ItemBasedCF.ipynb


Let's begin using the `ItemBasedCF.ipynb` file and let's start off by importing the MovieLens dataset that we have. Again, we're using a subset of it that just contains 100,000 ratings for now. But, there are larger datasets you can get from GroupLens.org-up to millions of ratings; if you're so inclined. Keep in mind though, when you start to deal with that really big data, you're going to be pushing the limits of what you can do in a single machine and what Pandas can handle. Without further ado, here's the first block of code:

```
import pandas as pd 
 
r_cols = ['user_id', 'movie_id', 'rating'] 
ratings = pd.read_csv('e:/sundog-consult/packt/datascience/ml-100k/u.data',      
                      sep='\t', names=r_cols, usecols=range(3)) 
 
m_cols = ['movie_id', 'title'] 
movies = pd.read_csv('e:/sundog-consult/packt/datascience/ml-100k/u.item', 
                     sep='|', names=m_cols, usecols=range(2)) 
 
ratings = pd.merge(movies, ratings) 
 
ratings.head() 
```

Just like earlier, we're going to import the u.data file that contains all the individual ratings for every user and what movie they rated, and then we're going to tie that together with the movie titles, so we don't have to just work with numerical movie IDs. Go ahead and hit the run cell button, and we end up with the following DataFrame.


![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/1.jpg)

The way to read this is, for example, user_id number 308 rated Toy Story (1995) a 4 star, and user_id number 66 rated Toy Story (1995) a 3 star. And, this will contain every rating, for every user, for every movie.
