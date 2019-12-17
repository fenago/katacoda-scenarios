
We want to distill that down to something we can actually look at and understand, because your mind doesn't deal with 4 dimensions very well, but you can look at 2 dimensions on a piece of paper pretty easily. Let's go ahead and load that up:

```
from sklearn.datasets import load_iris 
from sklearn.decomposition import PCA 
import pylab as pl 
from itertools import cycle 
 
iris = load_iris() 
 
numSamples, numFeatures = iris.data.shape 
print numSamples 
print numFeatures 
print list(iris.target_names) 
```

There's a handy dandy load_iris() function built into scikit-learn that will just load that up for you with no additional work; so you can just focus on the interesting part. Let's take a look at what that dataset looks like, the output of the preceding code is as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/14/1.png)

You can see that we are extracting the shape of that dataset, which means how many data points we have in it, that is 150, and how many features, or how many dimensions that dataset has, and that is 4. So, we have 150 Iris specimens in our dataset, with 4 dimensions of information. Again, that is the length and width of the sepal, and the length and width of the petal, for a total of 4 features, which we can think of as 4 dimensions.

We can also print out the list of target names in this dataset, which are the classifications,and we can see that each Iris belongs to one of three different species: Setosa, Versicolor, or Virginica. That's the data that we're working with: 150 Iris specimens, classified into one of 3 species, and we have 4 features associated with each Iris.

Let's look at how easy PCA is. Even though it's a very complicated technique under the hood, doing it is just a few lines of code. We're going to assign the entire Iris dataset and we're going to call it X. We will then create a PCA model, and we're going to keep n_components=2, because we want 2 dimensions, that is, we're going to go from 4 to 2.

We're going to use whiten=True, that means that we're going to normalize all the data, and make sure that everything is nice and comparable. Normally you will want to do that to get good results. Then, we will fit the PCA model to our Iris dataset X. We can use that model then, to transform that dataset down to 2 dimensions. Let's go ahead and run that. It happened pretty quickly!

```
X = iris.data 
pca = PCA(n_components=2, whiten=True).fit(X) 
X_pca = pca.transform(X) 
```

Please think about what just happened there. We actually created a PCA model to reduce 4 dimensions down to 2, and it did that by choosing 2 4D vectors, to create hyperplanes around, to project that 4D data down to 2 dimensions. You can actually see what those 4D vectors are, those eigenvectors, by printing out the actual components of PCA. So, PCA stands for Principal Component Analysis, those principal components are the eigenvectors that we chose to define our planes about:

```
print pca.components_ 
```

Output to the preceding code is as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/14/2.png)

You can actually look at those values, they're not going to mean a lot to you, because you can't really picture 4 dimensions anyway, but we did that just so you can see that it's actually doing something with principal components. So, let's evaluate our results:

```
print pca.explained_variance_ratio_ 
print sum(pca.explained_variance_ratio_) 
```

The PCA model gives us back something called explained_variance_ratio. Basically, that tells you how much of the variance in the original 4D data was preserved as I reduced it down to 2 dimensions. So, let's go ahead and take a look at that:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/14/3.png)

What it gives you back is actually a list of 2 items for the 2 dimensions that we preserved. This is telling me that in the first dimension I can actually preserve 92% of the variance in the data, and the second dimension only gave me an additional 5% of variance. If I sum it together, these 2 dimensions that I projected my data down into, I still preserved over 97% of the variance in the source data. We can see that 4 dimensions weren't really necessary to capture all the information in this dataset, which is pretty interesting. It's pretty cool stuff!

If you think about it, why do you think that might be? Well, maybe the overall size of the flower has some relationship to the species at its center. Maybe it's the ratio of length to width for the petal and the sepal. You know, some of these things probably move together in concert with each other for a given species, or for a given overall size of a flower. So, perhaps there are relationships between these 4 dimensions that PCA is extracting on its own. It's pretty cool, and pretty powerful stuff. Let's go ahead and visualize this.

The whole point of reducing this down to 2 dimensions was so that we could make a nice little 2D scatter plot of it, at least that's our objective for this little example here. So, we're going to do a little bit of Matplotlib magic here to do that. There is some sort of fancy stuff going on here that I should at least mention. So, what we're going to do is create a list of colors: red, green and blue. We're going to create a list of target IDs, so that the values 0, 1, and 2 map to the different Iris species that we have.

What we're going to do is zip all this up with the actual names of each species. The for loop will iterate through the 3 different Iris species, and as it does that, we're going to have the index for that species, a color associated with it, and the actual human-readable name for that species. We'll take one species at a time and plot it on our scatter plot just for that species with a given color and the given label. We will then add in our legend and show the results:

```
colors = cycle('rgb') 
target_ids = range(len(iris.target_names)) 
pl.figure() 
for i, c, label in zip(target_ids, colors, iris.target_names): 
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1], 
        c=c, label=label) 
pl.legend() 
pl.show()
```

The following is what we end up with:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/14/4.png)

That is our 4D Iris data projected down to 2 dimensions. Pretty interesting stuff! You can see it still clusters together pretty nicely. You know, you have all the Virginicas sitting together, all the Versicolors sitting in the middle, and the Setosas way off on the left side. It's really hard to imagine what these actual values represent. But, the important point is, we've projected 4D data down to 2D, and in such a way that we still preserve the variance. We can still see clear delineations between these 3 species. A little bit of intermingling going on in there, it's not perfect you know. But by and large, it was pretty effective.
