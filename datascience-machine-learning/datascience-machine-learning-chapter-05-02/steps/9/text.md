
Our code figures out how many points per cluster that works out to first and stores it in pointsPerCluster. Then, it builds up list X that starts off empty. For each cluster, we're going to create some random centroid of income (incomeCentroid) between 20,000 and 200,000 dollars and some random centroid of age (ageCentroid) between the age of 20 and 70.

What we're doing here is creating a fake scatter plot that will show income versus age for N people and k clusters. So for each random centroid that we created, I'm then going to create a normally distributed set of random data with a standard deviation of 10,000 in income and a standard deviation of 2 in age. That will give us back a bunch of age income data that is clustered into some pre-existing clusters that we can chose at random. OK, let's go ahead and run that.

Now, to actually do k-means, you'll see how easy it is.

```
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import scale 
from numpy import random, float 
 
data = createClusteredData(100, 5) 
 
model = KMeans(n_clusters=5) 
 
# Note I'm scaling the data to normalize it! Important for good results. 
model = model.fit(scale(data)) 
 
# We can look at the clusters each data point was assigned to 
print model.labels_  
 
# And we'll visualize it: 
plt.figure(figsize=(8, 6)) 
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float)) 
plt.show() 
```

All you need to do is import KMeans from scikit-learn's cluster package. We're also going to import matplotlib so we can visualize things, and also import scale so we can take a look at how that works.

So we use our createClusteredData() function to say 100 random people around 5 clusters. So there are 5 natural clusters for the data that I'm creating. We then create a model, a KMeans model with k of 5, so we're picking 5 clusters because we know that's the right answer. But again, in unsupervised learning you don't necessarily know what the real value of k is. You need to iterate and converge on it yourself. And then we just call model.fit using my KMeans model using the data that we had.
