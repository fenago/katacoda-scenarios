So, what we do with this data? Well, what we want to do is recommend movies for people. The way we do that is we look at all the ratings for a given person, find movies similar to the stuff that they rated, and those are candidates for recommendations to that person.

Let's start by creating a fake person to create recommendations for. I've actually already added a fake user by hand, ID number 0, to the MovieLens dataset that we're processing. You can see that user with the following code:

```
myRatings = userRatings.loc[0].dropna() 
myRatings 
```

This gives the following output:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/5.jpg)


That kind of represents someone like me, who loved Star Wars and The Empire Strikes Back, but hated the movie Gone with the Wind. So, this represents someone who really loves Star Wars, but does not like old style, romantic dramas, okay? So, I gave a rating of 5 star to The Empire Strikes Back (1980) and Star Wars (1977), and a rating of 1 star to Gone with the Wind (1939). So, I'm going to try to find recommendations for this fictitious user.
