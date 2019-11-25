Generative Adversarial Networks, or GANs, are challenging to train. This is because the
architecture involves both a generator and a discriminator model that compete in a zero-sum
game. It means that improvements to one model come at the cost of a degrading of performance
in the other model. The result is a very unstable training process that can often lead to
failure, e.g. a generator that generates the same image all the time or generates nonsense. As
such, there are a number of heuristics or best practices (called GAN hacks) that can be used
when configuring and training your GAN models. These heuristics have been hard won by
practitioners testing and evaluating hundreds or thousands of combinations of configuration
operations on a range of problems over many years.
Some of these heuristics can be challenging to implement, especially for beginners. Further,
some or all of them may be required for a given project, although it may not be clear which
subset of heuristics should be adopted, requiring experimentation. This means a practitioner
must be ready to implement a given heuristic with little notice. In this tutorial, you will discover
how to implement a suite of best practices or GAN hacks that you can copy-and-paste directly
into your GAN project. After reading this tutorial, you will know:
- The simultaneous training of generator and discriminator models in GANs is inherently
unstable.
- How to implement seven best practices for the deep convolutional GAN model architecture
from scratch.
- How to implement four additional best practices from Soumith Chintala’s GAN Hacks
presentation and list.
Let’s get started.
