The VGGFace refers to a series of models developed for face recognition and demonstrated on
benchmark computer vision datasets by members of the Visual Geometry Group (VGG) at
the University of Oxford. There are two main VGG models for face recognition at the time of
writing; they are VGGFace and VGGFace2. Let’s take a closer look at each in turn.

#### VGGFace Model
The VGGFace model, was described by Omkar Parkhi in the 2015 paper titled Deep Face
Recognition. A contribution of the paper was a description of how to develop a very large
training dataset, required to train modern-convolutional-neural-network-based face recognition
systems, to compete with the large datasets used to train models at Facebook and Google.

A deep convolutional neural network architecture is used in the VGG style, with blocks of
convolutional layers with small kernels and ReLU activations followed by max pooling layers,
and the use of fully connected layers in the classifier end of the network.

#### VGGFace2 Model
Qiong Cao, et al. from the VGG describe a follow-up work in their 2017 paper titled VGGFace2:
A Dataset For Recognizing Faces Across Pose And Age. They describe VGGFace2 as a much
larger dataset that they have collected for the intent of training and evaluating more effective
face recognition models

#### How to Install the keras-vggface Library
The authors of VGFFace2 provide the source code for their models, as well as pre-trained models
that can be downloaded with standard deep learning frameworks such as Caffe and PyTorch,
although there are no examples for TensorFlow or Keras. We could convert the provided models
to TensorFlow or Keras format and develop a model definition in order to load and use these
pre-trained models. Thankfully, this work has already been done and can be used directly by
third-party projects and libraries. Perhaps the best-of-breed third-party library for using the
VGGFace2 (and VGGFace) models in Keras is the keras-vggface project and library by Refik
Can Malli1. This library can be installed via pip; for example:

```
sudo pip install git+https://github.com/rcmalli/keras-vggface.git
```
