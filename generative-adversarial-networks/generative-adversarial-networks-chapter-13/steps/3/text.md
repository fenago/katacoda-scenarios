This tutorial is divided into five parts; they are:
1. What Is the Frechet Inception Distance?
2. How to Calculate the FID
3. How to Implement the FID With NumPy
4. How to Implement the FID With Keras
5. How to Calculate the FID for Real Images

#### What Is the Frechet Inception Distance?
The Frechet Inception Distance, or FID for short, is a metric for evaluating the quality of
generated images and specifically developed to evaluate the performance of generative adversarial
networks. The FID score was proposed and used by Martin Heusel, et al. in their 2017 paper
titled GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium.
The score was proposed as an improvement over the existing Inception Score, or IS.

The inception score estimates the quality of a collection of synthetic images based on how
well the top-performing image classification model Inception v3 classifies them as one of 1,000
known objects. The scores combine both the confidence of the conditional class predictions for
each synthetic image (quality) and the integral of the marginal probability of the predicted
classes (diversity). The inception score does not capture how synthetic images compare to real
images. The goal in developing the FID score was to evaluate synthetic images based on the
statistics of a collection of synthetic images compared to the statistics of a collection of real
images from the target domain.