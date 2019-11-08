
If you want to take a second to kind of work through that code in your head and figure out how it works, you've got the IPython Notebook. You can go back into that later too. Let's take a look what we ended up with.


Our totals dictionary is telling us how many people are in each age bracket, and it's pretty evenly distributed, just like we expected. The amount purchased by each age group is in fact increasing by age, so 20-year-olds only bought about 3,000 things and 70-year-olds bought about 11,000 things, and overall the entire population bought about 45,000 things.

Let's use this data to play around with the ideas of conditional probability. Let's first figure out what's the probability of buying something given that you're in your 30s. The notation for that will be P(E|F) if we're calling purchase E, and F as the event that you're in your 30s.

Now we have this fancy equation that gave you a way of computing P(E|F) given P(E,F), and P(E), but we don't need that. You don't just blindly apply equations whenever you see something. You have to think about your data intuitively. What is it telling us? I want to figure out the probability of purchasing something given that you're in your 30s. Well I have all the data I need to compute that directly.

```
PEF = float(purchases[30]) / float(totals[30]) 
```

I have how much stuff 30-year-olds purchased in the purchases[30] bucket, and I know how many 30-year-olds there are. So I can just divide those two numbers to get the ratio of 30-year-old purchases over the number of 30-year-olds. I can then output that using the print command:

```
print ("P(purchase | 30s): ", PEF) 
```

I end up with a probability of purchasing something given that you're in your 30s of being about 30%:

```
P(purchase | 30s): 0.2992959865211 
```

**Note:** that if you're using Python 2, the print command doesn't have the surrounding brackets, so it would be:

```
print "p(purchase | 30s): ", PEF 
```

If I want to find P(F), that's just the probability of being 30 overall, I can take the total number of 30-year-olds divided by the number of people in my dataset, which is 100,000:

```
PF = float(totals[30]) / 100000.0 
print ("P(30's): ", PF) 
```

Again, remove those brackets around the print statement if you're using Python 2. That should give the following output:

```
P(30's): 0.16619 
```

I know the probability of being in your 30s is about 16%.

We'll now find out P(E), which just represents the overall probability of buying something irrespective of your age:

```
PE = float(totalPurchases) / 100000.0 
print ("P(Purchase):", PE) 
 
P(Purchase): 0.45012 
```

That works out to be, in this example, about 45%. I can just take the total number of things purchased by everybody regardless of age and divide it by the total number of people to get the overall probability of purchase.
