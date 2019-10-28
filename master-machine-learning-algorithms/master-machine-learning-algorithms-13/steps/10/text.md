The best matching unit need to be moved closer to the training pattern if it is the same class
or further away if the classes differ. The class for the BMU is 0 and this matches the class of
the training instance 0. Therefore we need update the attributes to be closer to the training
instance, limited by the learning rate. The learning rate controls how much change can be made
to the codebook vectors for a single update. Let’s use an initial learning rate of 0.7 which is
much larger than normal in order to show fast learning on this simple problem. The update
procedure for a single attribute is therefore:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/10/1.JPG)

Where j is the attribute on the codebook vector being updated (e.g. X1), alpha is the
learning rate and trainingj is the same attribute on the training instance (e.g. X1). If the
BMU had a different class, the update would be almost identical except we would use a negative
sign to push the BMU further away from the training instance. For example:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/10/2.JPG)

We have just completed an update for one training instance.