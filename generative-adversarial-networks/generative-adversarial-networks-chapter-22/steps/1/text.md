The Pix2Pix GAN is a generator model for performing image-to-image translation trained
on paired examples. For example, the model can be used to translate images of daytime to
nighttime, or from sketches of products like shoes to photographs of products. The benefit
of the Pix2Pix model is that compared to other GANs for conditional image generation, it is
relatively simple and capable of generating large high-quality images across a variety of image
translation tasks. The model is very impressive but has an architecture that appears somewhat
complicated to implement for beginners. In this tutorial, you will discover how to implement
the Pix2Pix GAN architecture from scratch using the Keras deep learning framework. After
completing this tutorial, you will know:
- How to develop the PatchGAN discriminator model for the Pix2Pix GAN.
- How to develop the U-Net encoder-decoder generator model for the Pix2Pix GAN.
- How to implement the composite model for updating the generator and how to train both
models.
Let’s get started.
