These results are important, as it highlights that the quality generated can and does vary
across the run, even after the training process becomes stable. More training iterations, beyond
some point of training stability may or may not result in higher quality images. We can
summarize these observations for stable GAN training as follows:
- Discriminator loss on real and fake images is expected to sit around 0.5.
- Generator loss on fake images is expected to sit between 0.5 and perhaps 2.0.
- Discriminator accuracy on real and fake images is expected to sit around 80%.
- Variance of generator and discriminator loss is expected to remain modest.
- The generator is expected to produce its highest quality images during a period of stability.
- Training stability may degenerate into periods of high-variance loss and corresponding
lower quality generated images.

Now that we have a stable GAN model, we can look into modifying it to produce some
specific failure cases. There are two failure cases that are common to see when training GAN
models on new problems; they are mode collapse and convergence failure.
