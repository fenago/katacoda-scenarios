
So, even more fancy words: dynamic programming can be used to describe what we just did as well. Wow! That sounds like artificial intelligence, computers programming themselves, Terminator 2, Skynet stuff. But no, it's just what we just did. If you look up the definition of dynamic programming, it is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions ideally, using a memory-based data structure.

The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution thereby saving computation time at the expense of a (hopefully) modest expenditure in storage space:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/19/3.png)

We have a complicated exploration phase that finds the optimal rewards associated with each action for a given state. Once we have that table of the right action to take for a given state, we can very quickly use that to make our Pac-Man move in an optimal manner in a whole new maze that he hasn't seen before. So, reinforcement learning is also a form of dynamic programming. Wow!

To recap, you can make an intelligent Pac-Man agent by just having it semi-randomly explore different choices of movement given different conditions, where those choices are actions and those conditions are states. We keep track of the reward or penalty associated with each action or state as we go, and we can actually discount, going back multiple steps if you want to make it even better.

Then we store those Q values that we end up associating with each state, and we can use that to inform its future choices. So we can go into a whole new maze, and have a really smart Pac-Man that can avoid the ghosts and eat them up pretty effectively, all on its own. It's a pretty simple concept, very powerful though. You can also say that you understand a bunch of fancy terms because it's all called the same thing. Q-learning, reinforcement learning, Markov decision processes, dynamic programming: all tied up in the same concept.
