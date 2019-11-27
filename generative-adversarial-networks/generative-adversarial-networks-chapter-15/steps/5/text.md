The generator model takes a point in latent space as input and outputs a grayscale image
with the shape 28 × 28 pixels, where pixel values are in the range [-1,1] via the Tanh activation
function on the output layer. The define generator() function below defines the generator
model. This model is not compiled as it is not trained in a standalone manner.

```
# define the standalone generator model
def define_generator(latent_dim):
# weight initialization
init = RandomNormal(stddev=0.02)
# define model
model = Sequential()
# foundation for 7x7 image
n_nodes = 256 * 7 * 7
model.add(Dense(n_nodes, kernel_initializer=init, input_dim=latent_dim))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Reshape((7, 7, 256)))
# upsample to 14x1415.3. How to Develop an LSGAN for MNIST 292
model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same',
kernel_initializer=init))
model.add(BatchNormalization())
model.add(Activation('relu'))
# upsample to 28x28
model.add(Conv2DTranspose(64, (4,4), strides=(2,2), padding='same',
kernel_initializer=init))
model.add(BatchNormalization())
model.add(Activation('relu'))
# output 28x28x1
model.add(Conv2D(1, (7,7), padding='same', kernel_initializer=init))
model.add(Activation('tanh'))
return model
```

