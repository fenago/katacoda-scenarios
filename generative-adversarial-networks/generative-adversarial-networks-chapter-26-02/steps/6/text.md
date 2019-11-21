
The output of the model depends on the size of the input image but may be one value or a
square activation map of values. Each value is a probability that a patch in the input image is
real. These values can be averaged to give an overall likelihood or classification score if needed. A
pattern of Convolutional-BatchNorm-LeakyReLU layers is used in the model, which is common
to deep convolutional discriminator models. Unlike other models, the CycleGAN discriminator
uses InstanceNormalization instead of BatchNormalization. It is a very simple type of
normalization and involves standardizing (e.g. scaling to a standard Gaussian) the values on
each output feature map, rather than across features in a batch. An implementation of instance
normalization is provided in the keras-contrib project that provides early access to community
supplied Keras features.

The define discriminator() function below implements the 70×70 PatchGAN discriminator model as per the design of the model in the paper. The model takes a 256 × 256 sized image
as input and outputs a patch of predictions. The model is optimized using least squares loss
(L2) implemented as mean squared error, and a weighting is used so that updates to the model
have half (0.5) the usual effect. The authors of CycleGAN paper recommend this weighting
of model updates to slow down changes to the discriminator, relative to the generator model
during training.

```
# define the discriminator model
def define_discriminator(image_shape):
# weight initialization
init = RandomNormal(stddev=0.02)
# source image input
in_image = Input(shape=image_shape)
# C64
d = Conv2D(64, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(in_image)
d = LeakyReLU(alpha=0.2)(d)
# C128
d = Conv2D(128, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(d)
d = InstanceNormalization(axis=-1)(d)
d = LeakyReLU(alpha=0.2)(d)
# C256
d = Conv2D(256, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(d)
d = InstanceNormalization(axis=-1)(d)
d = LeakyReLU(alpha=0.2)(d)
# C512
d = Conv2D(512, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(d)
d = InstanceNormalization(axis=-1)(d)
d = LeakyReLU(alpha=0.2)(d)
# second last output layer
d = Conv2D(512, (4,4), padding='same', kernel_initializer=init)(d)
d = InstanceNormalization(axis=-1)(d)
d = LeakyReLU(alpha=0.2)(d)
# patch output
patch_out = Conv2D(1, (4,4), padding='same', kernel_initializer=init)(d)
# define model
model = Model(in_image, patch_out)
# compile model
model.compile(loss='mse', optimizer=Adam(lr=0.0002, beta_1=0.5), loss_weights=[0.5])
return model
```
