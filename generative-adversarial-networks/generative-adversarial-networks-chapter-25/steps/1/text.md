The Cycle Generative adversarial Network, or CycleGAN for short, is a generator model for
converting images from one domain to another domain. For example, the model can be used to
translate images of horses to images of zebras, or photographs of city landscapes at night to city
landscapes during the day. The benefit of the CycleGAN model is that it can be trained without
paired examples. That is, it does not require examples of photographs before and after the
translation in order to train the model, e.g. photos of the same city landscape during the day and
at night. Instead, it is able to use a collection of photographs from each domain and extract and
harness the underlying style of images in the collection in order to perform the translation. The
model is very impressive but has an architecture that appears quite complicated to implement
for beginners. In this tutorial, you will discover how to implement the CycleGAN architecture
from scratch using the Keras deep learning framework. After completing this tutorial, you will
know:
- How to implement the discriminator and generator models.
- How to define composite models to train the generator models via adversarial and cycle
loss.
- How to implement the training process to update model weights each training iteration.
Let’s get started.
