I explore some set of actions that I can take for a given set of states, I use that to inform the rewards associated with a given action for a given set of states, and after that exploration is done I can use that information, those Q values, to intelligently navigate through an entirely new maze for example.

This can also be called a Markov decision process. So again, a lot of data science is just assigning fancy, intimidating names to simple concepts, and there's a ton of that in reinforcement learning.

**Markov decision process**

So, if you look up the definition of Markov decision processes, it is "a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker".

- **Decision making:** What action do we take given a set of possibilities for a given state?
- **In situations where outcomes are partly random:** Hmm, kind of like our random exploration there.
- **Partly under the control of a decision maker:** The decision maker is our Q values that we computed.

So, MDPs, Markov decision processes, are a fancy way of describing our exploration algorithm that we just described for reinforcement learning. The notation is even similar, states are still described as s, and s' is the next state that we encounter. We have state transition functions that are defined as Pa for a given state of s and s'. We have our Q values, which are basically represented as a reward function, an Ra value for a given s and s'. So, moving from one state to another has a given reward associated with it, and moving from one state to another is defined by a state transition function:

- States are still described as **s** and **s''**
- State transition functions are described as **Pa(s,s')**
- Our Q values are described as a reward function **Ra(s,s')**

So again, describing what we just did, only a mathematical notation, and a fancier sounding word, Markov decision processes. And, if you want to sound even smarter, you can also call a Markov decision process by another name: a discrete time stochastic control process. That sounds intelligent! But the concept itself is the same thing that we just described.
