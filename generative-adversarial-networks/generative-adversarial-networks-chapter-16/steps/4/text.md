Now that we know the specific implementation details for the WGAN, we can implement the
model for image generation. In this section, we will develop a WGAN to generate a single
handwritten digit (the number seven) from the MNIST dataset (described in Section 7.2). This
is a good test problem for the WGAN as it is a small dataset requiring a modest mode that is
quick to train. The first step is to define the models.

The critic model takes as input one 28 × 28 grayscale image and outputs a score for the
realness or fakeness of the image. It is implemented as a modest convolutional neural network
using best practices for DCGAN design such as using the LeakyReLU activation function with a
slope of 0.2, batch normalization, and using a 2 × 2 stride to downsample. The critic model
makes use of the new ClipConstraint weight constraint to clip model weights after minibatch
updates and is optimized using the custom wasserstein loss() function, and the RMSProp
version of stochastic gradient descent with a learning rate of 0.00005. The define critic()
function below implements this, defining and compiling the critic model and returning it. The
input shape of the image is parameterized as a default function argument to make it clear.

```
# define the standalone critic model
def define_critic(in_shape=(28,28,1)):
# weight initialization
init = RandomNormal(stddev=0.02)
# weight constraint
const = ClipConstraint(0.01)
# define model
model = Sequential()
# downsample to 14x14
model.add(Conv2D(64, (4,4), strides=(2,2), padding='same', kernel_initializer=init,
kernel_constraint=const, input_shape=in_shape))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# downsample to 7x7
model.add(Conv2D(64, (4,4), strides=(2,2), padding='same', kernel_initializer=init,
kernel_constraint=const))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# scoring, linear activation
model.add(Flatten())
model.add(Dense(1))16.5. How to Train a Wasserstein GAN Model 315
# compile model
opt = RMSprop(lr=0.00005)
model.compile(loss=wasserstein_loss, optimizer=opt)
return model
```
