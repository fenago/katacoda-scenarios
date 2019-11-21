The Cycle Generative Adversarial Network, or CycleGAN, is an approach to training a deep
convolutional neural network for image-to-image translation tasks. Unlike other GAN models
for image translation, the CycleGAN does not require a dataset of paired images. For example,
if we are interested in translating photographs of oranges to apples, we do not require a training
dataset of oranges that have been manually converted to apples. This allows the development
of a translation model on problems where training datasets may not exist, such as translating
paintings to photographs. In this tutorial, you will discover how to develop a CycleGAN model
to translate photos of horses to zebras, and back again. After completing this tutorial, you will
know:
- How to load and prepare the horses to zebras image translation dataset for modeling.
