
The discriminator models are trained directly on real and generated images, whereas the
generator models are not. Instead, the generator models are trained via their related discriminator
models. Specifically, they are updated to minimize the loss predicted by the discriminator
for generated images marked as real, called adversarial loss. As such, they are encouraged to
generate images that better fit into the target domain. The generator models are also updated
based on how effective they are at the regeneration of a source image when used with the other
generator model, called cycle loss. Finally, a generator model is expected to output an image
without translation when provided an example from the target domain, called identity loss.
Altogether, each generator model is optimized via the combination of four outputs with four
loss functions:
- Adversarial loss (L2 or mean squared error).
- Identity loss (L1 or mean absolute error).
- Forward cycle loss (L1 or mean absolute error).
- Backward cycle loss (L1 or mean absolute error).

This can be achieved by defining a composite model used to train each generator model that
is responsible for only updating the weights of that generator model, although it is required to
share the weights with the related discriminator model and the other generator model. This is
implemented in the define composite model() function below that takes a defined generator
model (g model 1) as well as the defined discriminator model for the generator models output
(d model) and the other generator model (g model 2). The weights of the other models are
marked as not trainable as we are only interested in updating the first generator model, i.e. the
focus of this composite model.
