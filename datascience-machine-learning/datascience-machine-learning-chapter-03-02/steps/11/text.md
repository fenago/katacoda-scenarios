
Now this time, if I compute the P(E|F), that is, the probability of buying something given that you're in your 30s, I come up with about 40%.

```
PEF = float(purchases[30]) / float(totals[30]) 
print ("P(purchase | 30s): ", PEF) 
 
P(purchase | 30s):  0.398760454901 
If I compare that to the overall probability of purchasing, that too is about 40%.

```
PE = float(totalPurchases) / 100000.0 
print ("P(Purchase):", PE) 
 
P(Purchase): 0.4003 
```

I can see here that the probability of purchasing something given that you're in your 30s is about the same as the probability of purchasing something irrespective of your age (that is, P(E|F) is pretty close to P(E)). That suggests that there's no real relationship between those two things, and in fact, I know there isn't from this data.

Now in practice, you could just be seeing random chance, so you'd want to look at more than one age group. You'd want to look at more than one data point to see if there really is a relationship or not, but this is an indication that there's no relationship between age and probability of purchase in this sample data that we modified.

So, that's conditional probability in action. Hopefully your solution was fairly close and had similar results. If not, go back and study my solution. It's right there in the data files for this book, ConditionalProbabilitySolution.ipynb, if you need to open it up and study it and play around with it. Obviously, the random nature of the data will make your results a little bit different and will depend on what choice you made for the overall purchase probability, but that's the idea.

And with that behind us, let's move on to Bayes' theorem.

