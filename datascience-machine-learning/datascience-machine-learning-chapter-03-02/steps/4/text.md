The probability of B given A is equal to the probability of A and B occurring over the probability of A alone occurring, so this teases out the probability of B being dependent on the probability of A.

It'll make more sense with an example here, so bear with me.

Let's say that I give you, my readers, two tests, and 60% of you pass both tests. Now the first test was easier, 80% of you passed that one. I can use this information to figure out what percentage of readers who passed the first test also passed the second. So here's a real example of the difference between the probability of B given A and the probability of A and B.

I'm going to represent A as the probability of passing the first test, and B as the probability of passing the second test. What I'm looking for is the probability of passing the second test given that you passed the first, that is, P (B|A).

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-03-02/steps/2.png)

So the probability of passing the second test given that you passed the first is equal to the probability of passing both tests, P(A,B) (I know that 60% of you passed both tests irrespective of each other), divided by the probability of passing the first test, P(A), which is 80%. It's worked out to 60% passed both tests, 80% passed the first test, therefore the probability of passing the second given that you passed the first works out to 75%.

OK, it's a little bit tough to wrap your head around this concept. It took me a little while to really internalize the difference between the probability of something given something and the probability of two things happening irrespective of each other. Make sure you internalize this example and how it's really working before you move on.