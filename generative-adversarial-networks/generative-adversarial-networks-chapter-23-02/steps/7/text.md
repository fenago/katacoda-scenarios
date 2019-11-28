
The discriminator model is trained directly on real and generated images, whereas the
generator model is not. Instead, the generator model is trained via the discriminator model. It
is updated to minimize the loss predicted by the discriminator for generated images marked as
real. As such, it is encouraged to generate more realistic images. The generator is also updated
to minimize the L1 loss or mean absolute error between the generated image and the target
image. The generator is updated via a weighted sum of both the adversarial loss and the L1
loss, where the authors of the model recommend a weighting of 100 to 1 in favor of the L1 loss.
This is to encourage the generator strongly toward generating plausible translations of the input
image, and not just plausible images in the target domain.

This can be achieved by defining a new logical model comprised of the weights in the existing
standalone generator and discriminator model. This logical or composite model involves stacking
the generator on top of the discriminator. A source image is provided as input to the generator
and to the discriminator, although the output of the generator is connected to the discriminator
as the corresponding target image. The discriminator then predicts the likelihood that the
generated image was a real translation of the source image. The discriminator is updated
in a standalone manner, so the weights are reused in this composite model but are marked
as not trainable. The composite model is updated with two targets, one indicating that the
generated images were real (cross-entropy loss), forcing large weight updates in the generator
toward generating more realistic images, and the executed real translation of the image, which is
compared against the output of the generator model (L1 loss). 