
The architecture is described in such a way that the discriminator and auxiliary classifier
may be considered separate models that share model weights. In practice, the discriminator
and auxiliary classifier can be implemented as a single neural network model with two outputs.

The first output is a single probability via the sigmoid activation function that indicates the
realness of the input image and is optimized using binary cross-entropy like a normal GAN
discriminator model. The second output is a probability of the image belonging to each class via
the softmax activation function, like any given multiclass classification neural network model,
and is optimized using categorical cross-entropy. To summarize:
- **Generator Model:**
    * Input: Random point from the latent space, and the class label.
    * Output: Generated image.
- **Discriminator Model:**
    * Input: Image
    * Output: Probability that the provided image is real, probability of the image
belonging to each known class.

The plot below summarizes the inputs and outputs of a range of conditional GANs, including
the AC-GAN, providing some context for the differences.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-19/steps/2-0/1.png)
