This tutorial is divided into four parts; they are:
1. Challenge of Training GANs
2. Heuristics for Training Stable GANs
3. Deep Convolutional GANs (DCGANs).
4. Soumith Chintala’s GAN Hacks.

#### Challenge of Training GANs
GANs are difficult to train. The reason they are difficult to train is that both the generator
model and the discriminator model are trained simultaneously in a game. This means that
improvements to one model come at the expense of the other model. The goal of training two
models involves finding a point of equilibrium between the two competing concerns.

It also means that every time the parameters of one of the models are updated, the nature
of the optimization problem that is being solved is changed. This has the effect of creating a
dynamic system.