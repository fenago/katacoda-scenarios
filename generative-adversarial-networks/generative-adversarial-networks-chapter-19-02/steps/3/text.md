The generative adversarial network is an architecture for training a generative model, typically
deep convolutional neural networks for generating image. The architecture is comprised of both
a generator model that takes random points from a latent space as input and generates images,
and a discriminator for classifying images as either real (from the dataset) or fake (generated).
Both models are then trained simultaneously in a zero-sum game. A conditional GAN, cGAN or
CGAN for short, is an extension of the GAN architecture that adds structure to the latent space. The training of the GAN model is changed so that the generator is provided
both with a point in the latent space and a class label as input, and attempts to generate an
image for that class. The discriminator is provided with both an image and the class label and
must classify whether the image is real or fake as before.

The addition of the class as input makes the image generation process, and image classification
process, conditional on the class label, hence the name. The effect is both a more stable training
process and a resulting generator model that can be used to generate images of a given specific
type, e.g. for a class label. The Auxiliary Classifier GAN, or AC-GAN for short, is a further
extension of the GAN architecture building upon the CGAN extension. It was introduced by
Augustus Odena, et al. from Google Brain in the 2016 paper titled Conditional Image Synthesis
with Auxiliary Classifier GANs. As with the conditional GAN, the generator model in the
AC-GAN is provided both with a point in the latent space and the class label as input, e.g. the
image generation process is conditional.