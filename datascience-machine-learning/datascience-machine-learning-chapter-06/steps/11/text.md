Let's apply the concept of item-based collaborative filtering. To start with, movie similarities-figure out what movies are similar to other movies. In particular, we'll try to figure out what movies are similar to Star Wars, based on user rating data, and we'll see what we get out of it. Let's dive in!

#### Open Notebook
The Notebook opens in a new browser window. You can create a new notebook or open a local one. Check out the local folder `work` for several notebooks. Open and run `SimilarMovies.ipynb` in the `work` folder.

You can also open the Jupyter Notebook at https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/notebooks/work/SimilarMovies.ipynb

Okay so, let's go ahead and compute the first half of item-based collaborative filtering, which is finding similarities between items.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/11/1.png)

In this case, we're going to be looking at similarities between movies, based on user behavior. And, we're going to be using some real movie rating data from the GroupLens project. GroupLens.org provides real movie ratings data, by real people who are using the MovieLens.org website to rate movies and get recommendations back for new movies that they want to watch.
