
So, how do I do that? Well, let's start by creating a series called simCandidates and I'm going to go through every movie that I rated.

```
simCandidates = pd.Series() 
for i in range(0, len(myRatings.index)): 
    print "Adding sims for " + myRatings.index[i] + "..." 
    # Retrieve similar movies to this one that I rated 
    sims = corrMatrix[myRatings.index[i]].dropna() 
    # Now scale its similarity by how well I rated this movie 
    sims = sims.map(lambda x: x * myRatings[i]) 
    # Add the score to the list of similarity candidates 
    simCandidates = simCandidates.append(sims) 
     
#Glance at our results so far: 
print "sorting..." 
simCandidates.sort_values(inplace = True, ascending = False) 
print simCandidates.head(10) 
```

For i in range 0 through the number of ratings that I have in myRatings, I am going to add up similar movies to the ones that I rated. So, I'm going to take that corrMatrix DataFrame, that magical one that has all of the movie similarities, and I am going to create a correlation matrix with myRatings, drop any missing values, and then I am going to scale that resulting correlation score by how well I rated that movie.

So, the idea here is I'm going to go through all the similarities for The Empire Strikes Back, for example, and I will scale it all by 5, because I really liked The Empire Strikes Back. But, when I go through and get the similarities for Gone with the Wind, I'm only going to scale those by 1, because I did not like Gone with the Wind. So, this will give more strength to movies that are similar to movies that I liked, and less strength to movies that are similar to movies that I did not like, okay?
