A mode collapse refers to a generator model that is only capable of generating one or a small
subset of different outcomes, or modes. Here, mode refers to an output distribution, e.g. a
multi-modal function refers to a function with more than one peak or optima. With a GAN
generator model, a mode failure means that the vast number of points in the input latent space
(e.g. hypersphere of 100 dimensions in many cases) result in one or a small subset of generated
images.

A mode collapse can be identified when reviewing a large sample of generated images. The
images will show low diversity, with the same identical image or same small subset of identical
images repeating many times. A mode collapse can also be identified by reviewing the line plot
of model loss. The line plot will show oscillations in the loss over time, most notably in the
generator model, as the generator model is updated and jumps from generating one mode to
another model that has different loss. We can impair our stable GAN to suffer mode collapse
a number of ways. Perhaps the most reliable is to restrict the size of the latent dimension
directly, forcing the model to only generate a small subset of plausible outputs. Specifically, the
latent dim variable can be changed from 100 to 1, and the experiment re-run.

```
...
# size of the latent space
latent_dim = 1
...
```
