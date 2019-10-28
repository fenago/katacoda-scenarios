Before we can prepare a second boosted model, we must update the instance weights. This is
the very core of boosting. The weights are updated so that the next model that is created pays
more attention to the training instances that the previous models got wrong and less attention
to the instances that it got right. The weight for a training instance is updated using:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/10/1.JPG)

We know the current weight for each training instance (0.1) and the errors made on each
training instance. We now also know the stage. Updating the weights for each training instance
is therefore quite straightforward. Below are the updated weights for each training instance.
You will notice that only the weights for the one instance that the first model got wrong are
difference. In fact it is larger so that the next model that is created pays more attention to
them.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/10/2.JPG)
