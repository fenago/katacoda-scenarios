The Inception Score, or IS for short, is an objective metric for evaluating the quality of
generated images, specifically synthetic images output by generative adversarial network models.
The inception score was proposed by Tim Salimans, et al. in their 2016 paper titled Improved
Techniques for Training GANs. In the paper, the authors use a crowd-sourcing platform (Amazon
Mechanical Turk) to evaluate a large number of GAN generated images. They developed the
inception score as an attempt to remove the subjective human evaluation of images. The authors
discover that their scores correlated well with the subjective evaluation.

The inception score involves using a pre-trained deep learning neural network model for image
classification to classify the generated images. Specifically, the Inception v3 model described by
Christian Szegedy, et al. in their 2015 paper titled Rethinking the Inception Architecture for
Computer Vision. The reliance on the inception model gives the inception score its name. A
large number of generated images are classified using the model. Specifically, the probability of
the image belonging to each class is predicted. These predictions are then summarized into the
inception score. The score seeks to capture two properties of a collection of generated images:
- **Image Quality.** Do images look like a specific object?
- **Image Diversity.** Is a wide range of objects generated?

The inception score has a lowest value of 1.0 and a highest value of the number of classes
supported by the classification model; in this case, the Inception v3 model supports the 1,000
classes of the ILSVRC 2012 dataset, and as such, the highest inception score on this dataset is
1,000. The CIFAR-10 dataset is a collection of 50,000 images divided into 10 classes of objects.
The original paper that introduces the inception calculated the score on the real CIFAR-10
training dataset, achieving a result of 11.24 +/- 0.12. Using the GAN model also introduced in
their paper, they achieved an inception score of 8.09 +/- .07 when generating synthetic images
for this dataset.