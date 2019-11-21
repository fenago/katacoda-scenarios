Pix2Pix is a Generative Adversarial Network, or GAN, model designed for general purpose
image-to-image translation. The approach was presented by Phillip Isola, et al. in their 2016
paper titled Image-to-Image Translation with Conditional Adversarial Networks and presented
at CVPR in 2017 (introduced in Chapter 21). The GAN architecture is comprised of a generator
model for outputting new plausible synthetic images, and a discriminator model that classifies
images as real (from the dataset) or fake (generated). The discriminator model is updated
directly, whereas the generator model is updated via the discriminator model. As such, the two
models are trained simultaneously in an adversarial process where the generator seeks to better
fool the discriminator and the discriminator seeks to better identify the counterfeit images.

The Pix2Pix model is a type of conditional GAN, or cGAN, where the generation of the
output image is conditional on an input, in this case, a source image. The discriminator is
provided both with a source image and the target image and must determine whether the target
is a plausible transformation of the source image. The generator is trained via adversarial loss,
which encourages the generator to generate plausible images in the target domain. The generator
is also updated via L1 loss measured between the generated image and the expected output
image. This additional loss encourages the generator model to create plausible translations of
the source image.

The Pix2Pix GAN has been demonstrated on a range of image-to-image translation tasks
such as converting maps to satellite photographs, black and white photographs to color, and
sketches of products to product photographs. Now that we are familiar with the Pix2Pix GAN,
let’s prepare a dataset that we can use with image-to-image translation.