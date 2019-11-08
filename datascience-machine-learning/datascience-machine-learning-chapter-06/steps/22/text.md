
So, I just go through and build up this list of similarity candidates, recommendation candidates if you will, sort the results and print them out. Let's see what we get:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/6.jpg)

Hey, those don't look too bad, right? So, obviously The Empire Strikes Back (1980) and Star Wars (1977) come out on top, because I like those movies explicitly, I already watched them and rated them. But, bubbling up to the top of the list is Return of the Jedi (1983), which we would expect and Raiders of the Lost Ark (1981).

Let's start to refine these results a little bit more. We're seeing that we're getting duplicate values back. If we have a movie that was similar to more than one movie that I rated, it will come back more than once in the results, so we want to combine those together. If I do in fact have the same movie, maybe that should get added up together into a combined, stronger recommendation score. Return of the Jedi, for example, was similar to both Star Wars and The Empire Strikes Back. How would we do that?

Using the groupby command to combine rows
We'll go ahead and explore that. We're going to use the groupby command again to group together all of the rows that are for the same movie. Next, we will sum up their correlation score and look at the results:

```
simCandidates = simCandidates.groupby(simCandidates.index).sum() 
simCandidates.sort_values(inplace = True, ascending = False) 
simCandidates.head(10) 
```

Following is the result:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/7.jpg)

Hey, this is looking really good!

So Return of the Jedi (1983) comes out way on top, as it should, with a score of 7, Raiders of the Lost Ark (1981) a close second at 5, and then we start to get to Indiana Jones and the Last Crusade (1989), and some more movies, The Bridge on the River Kwai (1957), Back to the Future (1985),The Sting (1973). These are all movies that I would actually enjoy watching! You know, I actually do like old-school Disney movies too, so Cinderella (1950) isn't as crazy as it might seem.

The last thing we need to do is filter out the movies that I've already rated, because it doesn't make sense to recommend movies you've already seen.

Removing entries with the drop command
So, I can quickly drop any rows that happen to be in my original ratings series using the following code:

```
filteredSims = simCandidates.drop(myRatings.index) 
filteredSims.head(10) 
```

Running that will let me see the final top 10 results:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-06/steps/17/8.jpg)

And there we have it! Return of the Jedi (1983), Raiders of the Lost Ark (1981), Indiana Jones and the Last Crusade (1989), all the top results for my fictitious user, and they all make sense. I'm seeing a few family-friendly films, you know, Cinderella (1950), The Wizard of Oz (1939), Dumbo (1941), creeping in, probably based on the presence of Gone with the Wind in there, even though it was weighted downward it's still in there, and still being counted. And, there we have our results, so. There you have it! Pretty cool!

We have actually generated recommendations for a given user and we could do that for any user in our entire DataFrame. So, go ahead and play with that if you want to. I also want to talk about how you can actually get your hands dirty a little bit more, and play with these results; try to improve upon them.

There's a bit of an art to this, you know, you need to keep iterating and trying different ideas and different techniques until you get better and better results, and you can do this pretty much forever. I mean, I made a whole career out of it. So, I don't expect you to spend the next, you know, 10 years trying to refine this like I did, but there are some simple things you can do, so let's talk about that.