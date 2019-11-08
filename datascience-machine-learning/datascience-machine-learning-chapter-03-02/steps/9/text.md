What I want you to do is modify the following Python code which was used in the preceding section.

```
from numpy import random 
random.seed(0) 
 
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0} 
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0} 
totalPurchases = 0 
for _ in range(100000): 
ageDecade = random.choice([20, 30, 40, 50, 60, 70]) 
purchaseProbability = 0.4 
totals[ageDecade] += 1 
if (random.random() < purchaseProbability): 
totalPurchases += 1 
purchases[ageDecade] += 1 
```

Modify it to actually not have a dependency between purchases and age. Make that an evenly distributed chance as well. See what that does to your results. Do you end up with a very different conditional probability of being in your 30s and purchasing something versus the overall probability of purchasing something? What does that tell you about your data and the relationship between those two different attributes? Go ahead and try that, and make sure you can actually get some results from this data and understand what's going on, and I'll run through my own solution to that exercise in just a minute.

So that's conditional probability, both in theory and in practice. You can see there's a lot of little nuances to it and a lot of confusing notation. Go back and go through this section again if you need to wrap your head around it. I gave you a homework assignment, so go off and do that now, see if you can actually modify my code in that IPython Notebook to produce a constant probability of purchase for those different age groups. Come back and we'll take a look at how I solved that problem and what my results were.