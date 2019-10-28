An epoch is one pass through the entire training dataset (all 10 instances). This involves
applying the above procedure for each training instance, locating the BMU and updating it.
Before the start of the run we must choose the number of epochs to perform in order to train
the model. The number could be hundreds, thousands or even tens of thousands of epochs,
depending on the difficulty of the problem. Each epoch, the learning rate is decreased from the
starting value. This means that at the start of the run the model is doing a lot of learning and
towards the end of the run it is only doing very small adjustments to codebook vectors already
learned. The learning rate can be calculated for a given epoch as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/11/1.JPG)

Where LearningRate is the learning rate for the current epoch (0 to MaxEpoch-1), alpha
is the learning rate specified to the algorithm at the start of the training run and MaxEpoch is
the total number of epochs to run the algorithm also specified at the start of the run.
We end up with the following codebook vectors:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/11/2.JPG)

The process probably needs to be repeated for another 10-to-20 epochs with a lower learning
rate (e.g. 0.3) to settle down the codebook vectors.