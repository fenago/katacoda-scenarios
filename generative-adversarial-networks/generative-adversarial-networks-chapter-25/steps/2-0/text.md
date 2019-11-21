
The discriminator and generator models are trained in an adversarial zero-sum process,
like normal GAN models. The generators learn to better fool the discriminators and the
discriminators learn to better detect fake images. Together, the models find an equilibrium
during the training process. Additionally, the generator models are regularized not just to
create new images in the target domain, but instead create translated versions of the input
images from the source domain. This is achieved by using generated images as input to the
corresponding generator model and comparing the output image to the original images. Passing
an image through both generators is called a cycle. Together, each pair of generator models are
trained to better reproduce the original source image, referred to as cycle consistency.

- Domain-B → Generator-A → Domain-A → Generator-B → Domain-B
- Domain-A → Generator-B → Domain-B → Generator-A → Domain-A

There is one further element to the architecture referred to as the identity mapping. This is
where a generator is provided with images as input from the target domain and is expected to
generate the same image without change. This addition to the architecture is optional, although
it results in a better matching of the color profile of the input image.

- Domain-A → Generator-A → Domain-A
- Domain-B → Generator-B → Domain-B
