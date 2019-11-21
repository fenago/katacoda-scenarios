Additional information that is correlated with the input images, such as class labels, can be
used to improve the GAN. This improvement may come in the form of more stable training,
faster training, and/or generated images that have better quality. Class labels can also be used
for the deliberate or targeted generation of images of a given type. A limitation of a GAN model
is that it may generate a random image from the domain. There is a relationship between points
in the latent space to the generated images, but this relationship is complex and hard to map.
Alternately, a GAN can be trained in such a way that both the generator and the discriminator
models are conditioned on the class label. This means that when the trained generator model is
used as a standalone model to generate images in the domain, images of a given type, or class
label, can be generated.

For example, in the case of MNIST, specific handwritten digits can be generated, such as the
number 9; in the case of CIFAR-10, specific object photographs can be generated such as frogs;
and in the case of the Fashion-MNIST dataset, specific items of clothing can be generated, such
as dress. This type of model is called a Conditional Generative Adversarial Network, CGAN or
cGAN for short. The cGAN was first described by Mehdi Mirza and Simon Osindero in their
2014 paper titled Conditional Generative Adversarial Nets. In the paper, the authors motivate
the approach based on the desire to direct the image generation process of the generator model.

Their approach is demonstrated in the MNIST handwritten digit dataset where the class labels
are one hot encoded and concatenated with the input to both the generator and discriminator
models. The image below provides a summary of the model architecture.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-17/steps/2-0/1.png)
