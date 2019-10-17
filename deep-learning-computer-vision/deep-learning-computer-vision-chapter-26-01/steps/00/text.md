Tutorial Overview
This tutorial is divided into five parts; they are:
1. How to Install Mask R-CNN for Keras
2. How to Prepare a Dataset for Object Detection
3. How to Train a Mask R-CNN Model for Kangaroo Detection
4. How to Evaluate a Mask R-CNN Model
5. How to Detect Kangaroos in New Photos


#### Object detection
Object detection is a task in computer vision that involves identifying the presence, location,
and type of one or more objects in a given image. It is a challenging problem that involves
building upon methods for object recognition (e.g. where are they), object localization (e.g.
what are their extent), and object classification (e.g. what are they).
The Region-Based Convolutional Neural Network, or R-CNN, is a family of convolutional
neural network models designed for object detection, developed by Ross Girshick, et al. 

There are perhaps four main variations of the approach, resulting in the
current pinnacle called Mask R-CNN. The Mask R-CNN introduced in the 2018 paper titled
Mask R-CNN is the most recent variation of the family of models and supports both object
detection and object segmentation. Object segmentation not only involves localizing objects
in the image but also specifies a mask for the image, indicating exactly which pixels in the
image belong to the object. Mask R-CNN is a sophisticated model to implement, especially as
compared to a simple or even state-of-the-art deep convolutional neural network model. Instead
of developing an implementation of the R-CNN or Mask R-CNN model from scratch, we can
use a reliable third-party implementation built on top of the Keras deep learning framework.
The best-of-breed third-party implementation of Mask R-CNN is the Mask R-CNN Project
developed by Matterport. The project is open source released under a permissive license
(e.g. MIT license) and the code has been widely used on a variety of projects and Kaggle
competitions.