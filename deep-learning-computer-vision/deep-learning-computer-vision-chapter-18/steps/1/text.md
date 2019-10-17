How to Use Pre-Trained Models and
Transfer Learning
Deep convolutional neural network models may take days or even weeks to train on very large
datasets. A way to short-cut this process is to re-use the model weights from pre-trained
models that were developed for standard computer vision benchmark datasets, such as the
ImageNet image recognition tasks. Top performing models can be downloaded and used directly,
or integrated into a new model for your own computer vision problems. In this tutorial, you
will discover how to use transfer learning when developing convolutional neural networks for
computer vision applications. After reading this tutorial, you will know:
- Transfer learning involves using models trained on one problem as a starting point on a
related problem.
- Transfer learning is flexible, allowing the use of pre-trained models directly, as feature
extraction preprocessing, and integrated into entirely new models.
- Keras provides convenient access to many top performing models on the ImageNet image
recognition tasks such as VGG, Inception, and ResNet.
Let’s get started.
