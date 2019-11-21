In this section, we will develop the CycleGAN model for translating photos of horses to zebras
and photos of zebras to horses. The same model architecture and configuration described in the
paper was used across a range of image-to-image translation tasks. This architecture is both
described in the body of the paper, with additional detail in the appendix of the paper, and a
fully working implementation provided as open source implemented for the Torch deep learning
framework. The implementation in this section will use the Keras deep learning framework
based directly on the model described in the paper and implemented in the author’s codebase,
designed to take and generate color images with the size 256×256 pixels.

The architecture is comprised of four models: two discriminator models, and two generator
models. The discriminator is a deep convolutional neural network that performs image classification. It takes a source image as input and predicts the likelihood of whether the target image
is a real or fake image. Two discriminator models are used, one for Domain-A (horses) and one
for Domain-B (zebras). The discriminator design is based on the effective receptive field of the
model, which defines the relationship between one output of the model to the number of pixels
in the input image. This is called a PatchGAN model and is carefully designed so that each
output prediction of the model maps to a 70 × 70 square or patch of the input image. The
benefit of this approach is that the same model can be applied to input images of different sizes, e.g. larger or smaller than 256 × 256 pixels.
