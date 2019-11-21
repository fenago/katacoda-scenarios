A generative adversarial network, or GAN for short, is an architecture for training deep learningbased generative models. The architecture is comprised of a generator and a discriminator
model. The generator model is responsible for generating new plausible examples that ideally
are indistinguishable from real examples in the dataset. The discriminator model is responsible
for classifying a given image as either real (drawn from the dataset) or fake (generated). The
models are trained together in a zero-sum or adversarial manner, such that improvements in
the discriminator come at the cost of a reduced capability of the generator, and vice versa.

GANs are effective at image synthesis, that is, generating new examples of images for a
target dataset. Some datasets have additional information, such as a class label, and it is
desirable to make use of this information. For example, the MNIST handwritten digit dataset
has class labels of the corresponding integers, the CIFAR-10 small object photograph dataset has
class labels for the corresponding objects in the photographs, and the Fashion-MNIST clothing
dataset has class labels for the corresponding items of clothing. There are two motivations for
making use of the class label information in a GAN model.

1. Improve the GAN.
2. Targeted Image Generation.