Before we can perform face recognition, we need to detect faces. Face detection is the process of
automatically locating faces in a photograph and localizing them by drawing a bounding box
around their extent. In this tutorial, we will also use the Multi-Task Cascaded Convolutional
Neural Network, or MTCNN, for face detection, e.g. finding and extracting faces from photos.
This is a state-of-the-art deep learning model for face detection, described in the 2016 paper
titled Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks.
Note, the installation of the face detection library was covered in Chapter 28 and is summarized
again here for completeness. We will use the implementation provided by Ivan de Paz Centeno
in the ipazc/mtcnn project.


We can confirm that the library was installed correctly by importing the library and printing
the version; for example:

```
# confirm mtcnn was installed correctly
import mtcnn
# print version
print(mtcnn.__version__)
```

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/02_check_mtcnn_version.py` to view file.

#### Run Code
Now, run the python code by running: `python 02_check_mtcnn_version.py`{{execute}}
