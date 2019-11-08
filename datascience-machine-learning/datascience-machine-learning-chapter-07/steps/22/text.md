
Now, you can also look ahead a little bit, to make an even more intelligent agent. So, I'm actually two steps away from getting a power pill here. So, as Pac-Man were to explore this state, if I were to hit the case of eating that power pill on the next state, I could actually factor that into the Q value for the previous state. If you just have some sort of a discount factor, based on how far away you are in time, how many steps away you are, you can factor that all in together. So, that's a way of actually building in a little bit of memory into the system. You can "look ahead" more than one step by using a discount factor when computing Q (here s is previous state, s' is current state):

```
Q(s,a) += discount * (reward(s,a) + max(Q(s')) - Q(s,a))
```

So, the Q value that I experience when I consume that power pill might actually give a boost to the previous Q values that I encountered along the way. So, that's a way to make Q-learning even better.
