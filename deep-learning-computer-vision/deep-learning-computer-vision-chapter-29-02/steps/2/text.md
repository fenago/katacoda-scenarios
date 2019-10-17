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