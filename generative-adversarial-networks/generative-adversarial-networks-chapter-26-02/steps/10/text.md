
The discriminator is connected to the output of the generator in order to classify generated
images as real or fake. A second input for the composite model is defined as an image from
the target domain (instead of the source domain), which the generator is expected to output
without translation for the identity mapping. Next, forward cycle loss involves connecting the
output of the generator to the other generator, which will reconstruct the source image. Finally,
the backward cycle loss involves the image from the target domain used for the identity mapping
that is also passed through the other generator whose output is connected to our main generator
as input and outputs a reconstructed version of that image from the target domain.
To summarize, a composite model has two inputs for the real photos from Domain-A and
Domain-B, and four outputs for the discriminator output, identity generated image, forward
cycle generated image, and backward cycle generated image. Only the weights of the first or
main generator model are updated for the composite model and this is done via the weighted
sum of all loss functions. The cycle loss is given more weight (10-times) than the adversarial
loss as described in the paper, and the identity loss is always used with a weighting half that of
the cycle loss (5-times), matching the official implementation source code.

```
# define a composite model for updating generators by adversarial and cycle loss
def define_composite_model(g_model_1, d_model, g_model_2, image_shape):
# ensure the model we're updating is trainable
g_model_1.trainable = True
# mark discriminator as not trainable
d_model.trainable = False
# mark other generator model as not trainable
g_model_2.trainable = False
# discriminator element
input_gen = Input(shape=image_shape)
gen1_out = g_model_1(input_gen)
output_d = d_model(gen1_out)
# identity element
input_id = Input(shape=image_shape)
output_id = g_model_1(input_id)
# forward cycle
output_f = g_model_2(gen1_out)
# backward cycle
gen2_out = g_model_2(input_id)
output_b = g_model_1(gen2_out)
# define model graph
model = Model([input_gen, input_id], [output_d, output_id, output_f, output_b])
# define optimization algorithm configuration
opt = Adam(lr=0.0002, beta_1=0.5)
# compile model with weighting of least squares loss and L1 loss
model.compile(loss=['mse', 'mae', 'mae', 'mae'], loss_weights=[1, 5, 10, 10],
optimizer=opt)
return model
```
