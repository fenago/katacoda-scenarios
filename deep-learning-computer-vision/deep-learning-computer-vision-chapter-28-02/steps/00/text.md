This tutorial is divided into four parts; they are:
1. Face Detection
2. Test Photographs
3. Face Detection With OpenCV
4. Face Detection With Deep Learning

#### Face Detection
Face detection is a problem in computer vision of locating and localizing one or more faces in a
photograph (introduced in Chapter 27). Locating a face in a photograph refers to finding the
coordinates of the face in the image, whereas localization refers to demarcating the extent of
the face, often via a bounding box around the face.

Detecting faces in a photograph is easily solved by humans, although this has historically
been challenging for computers given the dynamic nature of faces. For example, faces must be
detected regardless of orientation or angle they are facing, light levels, clothing, accessories, hair
color, facial hair, makeup, age, and so on.

Given a photograph, a face detection system will output zero or more bounding boxes that
contain faces. Detected faces can then be provided as input to a subsequent system, such as a
face recognition system.

There are perhaps two main approaches to face recognition: feature-based methods that
use hand-crafted filters to search for and detect faces, and image-based methods that learn
holistically how to extract faces from the entire image