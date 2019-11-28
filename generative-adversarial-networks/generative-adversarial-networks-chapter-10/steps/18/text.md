Perhaps the most common failure when training a GAN is a failure to converge. Typically, a
neural network fails to converge when the model loss does not settle down during the training
process. In the case of a GAN, a failure to converge refers to not finding an equilibrium between
the discriminator and the generator. The likely way that you will identify this type of failure is
that the loss for the discriminator has gone to zero or close to zero. In some cases, the loss of
the generator may also rise and continue to rise over the same period.

This type of loss is most commonly caused by the generator outputting garbage images that
the discriminator can easily identify. This type of failure might happen at the beginning of the
run and continue throughout training, at which point you should halt the training process. For
some unstable GANs, it is possible for the GAN to fall into this failure mode for a number of
batch updates, or even a number of epochs, and then recover. There are many ways to impair
our stable GAN to achieve a convergence failure, such as changing one or both models to have
insufficient capacity, changing the Adam optimization algorithm to be too aggressive, and using
very large or very small kernel sizes in the models.

In this case, we will update the example to combine the real and fake samples when updating
the discriminator. This simple change will cause the model to fail to converge. This change is
as simple as using the vstack() NumPy function to combine the real and fake samples and
then calling the train on batch() function to update the discriminator model. The result is
also a single loss and accuracy scores, meaning that the reporting of model performance, must
also be updated. 
