This tutorial is divided into five parts; they are:
1. Vector Arithmetic in Latent Space
2. Large-Scale CelebFaces Dataset (CelebA)
3. How to Prepare the CelebA Faces Dataset
4. How to Develop a GAN for CelebA
5. How to Explore the Latent Space for Faces

#### Vector Arithmetic in Latent Space
The generator model in the GAN architecture takes a point from the latent space as input and
generates a new image. The latent space itself has no meaning. Typically it is a 100-dimensional
hypersphere with each variable drawn from a Gaussian distribution with a mean of zero and
a standard deviation of one. Through training, the generator learns to map points onto the
latent space with specific output images and this mapping will be different each time the model
is trained. The latent space has structure when interpreted by the generator model, and this
structure can be queried and navigated for a given model.

Typically, new images are generated using random points in the latent space. Taken a step
further, points in the latent space can be constructed (e.g. all 0s, all 0.5s, or all 1s) and used as
input or a query to generate a specific image. A series of points can be created on a linear path
between two points in the latent space, such as two generated images. These points can be used
to generate a series of images that show a transition between the two generated images. Finally,
the points in the latent space can be kept and used in simple vector arithmetic to create new
points in the latent space that, in turn, can be used to generate images. This is an interesting
idea, as it allows for the intuitive and targeted generation of images.