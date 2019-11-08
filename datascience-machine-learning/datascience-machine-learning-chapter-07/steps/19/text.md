Our next topic's a fun one: reinforcement learning. We can actually use this idea with an example of Pac-Man. We can actually create a little intelligent Pac-Man agent that can play the game Pac-Man really well on its own. You'll be surprised how simple the technique is for building up the smarts behind this intelligent Pac-Man. Let's take a look!

So, the idea behind reinforcement learning is that you have some sort of agent, in this case Pac-Man, that explores some sort of space, and in our example that space will be the maze that Pac-Man is in. As it goes, it learns the value of different state changes within different conditions.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-07/steps/19/1.png)

For example, in the preceding image, the state of Pac-Man might be defined by the fact that it has a ghost to the South, and a wall to the West, and empty spaces to the North and East, and that might define the current state of Pac-Man. The state changes it can take would be to move in a given direction. I can then learn the value of going in a certain direction. So, for example, if I were to move North, nothing would really happen, there's no real reward associated with that. But, if I were to move South I would be destroyed by the ghost, and that would be a negative value.
