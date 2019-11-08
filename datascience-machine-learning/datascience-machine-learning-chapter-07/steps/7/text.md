
Every movie in our MovieLens dataset has additional information on what genre it belongs to. A movie can belong to more than one genre, a genre being something like science fiction, or drama, or comedy, or animation. We will also look at the overall popularity of the movie, given by the number of people who rated it, and we also know the average rating of each movie. I can combine all this information together to basically create a metric of distance between two movies just based on rating information and genre information. Let's see what we get.

We'll use pandas again to make life simple, and if you are following along, again make sure to change the path to the MovieLens dataset to wherever you installed it, which will almost certainly not be what is in this Python notebook.

Please go ahead and change that if you want to follow along. As before, we're just going to import the actual ratings data file itself, which is u.data using the read_csv() function in pandas. We're going to tell that it actually has a tab-delimiter and not a comma. We're going to import the first 3 columns, which represent the user_id, movie_id, and rating, for every individual movie rating in our dataset:

```
import pandas as pd 
 
r_cols = ['user_id', 'movie_id', 'rating'] 
ratings = pd.read_csv('C:\DataScience\ml-100k\u.data', sep='\t', names=r_cols, usecols=range(3)) 
ratings.head()ratings.head() 
```

If we go ahead and run that and look at the top of it, we can see that it's working, here's how the output should look like:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/6/1.png)

We end up with a DataFrame that has user_id, movie_id, and rating. For example, user_id 0 rated movie_id 50, which I believe is Star Wars, 5 stars, and so on and so forth.
