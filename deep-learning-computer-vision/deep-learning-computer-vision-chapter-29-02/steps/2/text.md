Before we can perform face recognition, we need to detect faces. Face detection is the process of
automatically locating faces in a photograph and localizing them by drawing a bounding box
around their extent. In this tutorial, we will also use the Multi-Task Cascaded Convolutional
Neural Network, or MTCNN, for face detection, e.g. finding and extracting faces from photos.
This is a state-of-the-art deep learning model for face detection, described in the 2016 paper
titled Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks.

We can use the mtcnn library to create a face detector and extract faces for our use with
the VGGFace face detector models in subsequent sections


##### Tutorial Overview
This tutorial is divided into six parts; they are:
1. Face Recognition
2. VGGFace and VGGFace2 Models
3. How to Install the keras-vggface Library
4. How to Detect Faces for Face Recognition
5. How to Perform Face Identification With VGGFace2
6. How to Perform Face Verification With VGGFace2



#### How to Install the keras-vggface Library
The authors of VGFFace2 provide the source code for their models, as well as pre-trained models
that can be downloaded with standard deep learning frameworks such as Caffe and PyTorch,
although there are no examples for TensorFlow or Keras. We could convert the provided models
to TensorFlow or Keras format and develop a model definition in order to load and use these
pre-trained models. Thankfully, this work has already been done and can be used directly by
third-party projects and libraries. Perhaps the best-of-breed third-party library for using the
VGGFace2 (and VGGFace) models in Keras is the keras-vggface project and library by Refik
Can Malli1. This library can be installed via pip; for example:


`pip install git+https://github.com/rcmalli/keras-vggface.git`{{execute}}

After successful installation, you should then see a message like the following:

```
Successfully installed keras-vggface-0.6
```


You can confirm that the library was installed correctly by querying the installed package:
`pip show keras-vggface`{{execute}}


This will summarize the details of the package; for example:

```
Name: keras-vggface
Version: 0.5
Summary: VGGFace implementation with Keras framework
Home-page: https://github.com/rcmalli/keras-vggface
Author: Refik Can MALLI
Author-email: mallir@itu.edu.tr
License: MIT
Location: ...
Requires: numpy, scipy, h5py, pillow, keras, six, pyyaml
Required-by
```
