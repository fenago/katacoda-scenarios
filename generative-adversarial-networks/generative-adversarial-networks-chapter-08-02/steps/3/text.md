We could start training this model now with real examples with a class label of one and
randomly generate samples with a class label of zero. The development of these elements will be
useful later, and it helps to see that the discriminator is just a normal neural network model for
binary classification. First, we need a function to load and prepare the dataset of real images.
We will use the cifar.load data() function to load the CIFAR-10 dataset and just use the
input part of the training dataset as the real images.

```
...
# load cifar10 dataset
(trainX, _), (_, _) = load_data()
```
