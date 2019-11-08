One problem that we have in reinforcement learning is the exploration problem. How do I make sure that I efficiently cover all the different states and actions within those states during the exploration phase?

**The simple approach**

One simple approach is to always choose the action for a given state with the highest Q value that I've computed so far, and if there's a tie, just choose at random. So, initially all of my Q values might be 0, and I'll just pick actions at random at first.

As I start to gain information about better Q values for given actions and given states, I'll start to use those as I go. But, that ends up being pretty inefficient, and I can actually miss a lot of paths that way if I just tie myself into this rigid algorithm of always choosing the best Q value that I've computed thus far.

**The better way**

So, a better way is to introduce a little bit of random variation into my actions as I'm exploring. So, we call that an epsilon term. So, suppose we have some value, that I roll the dice, I have a random number. If it ends up being less than this epsilon value, I don't actually follow the highest Q value; I don't do the thing that makes sense, I just take a path at random to try it out, and see what happens. That actually lets me explore a much wider range of possibilities, a much wider range of actions, for a wider range of states more efficiently during that exploration stage.

So, what we just did can be described in very fancy mathematical terms, but you know conceptually it's pretty simple.
