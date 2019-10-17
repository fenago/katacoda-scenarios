The first step is to detect the face in each photograph and reduce the dataset to a series of
faces only. Let’s test out our face detector function defined in the previous section, specifically
extract face(). Looking in the 5-celebrity-faces-dataset/train/ben afflek/ directory,
we can see that there are 14 photographs of Ben Affleck in the training dataset. We can detect
the face in each photograph, and create a plot with 14 faces, with two rows of seven images
each. 

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/03_extract_faces.py` to view file.


#### Run Code
Now, run the python code by running: `python 03_extract_faces.py`{{execute}}


Running the example takes a moment and reports the progress of each loaded photograph
along the way and the shape of the NumPy array containing the face pixel data.

```
1 (160, 160, 3)
2 (160, 160, 3)
3 (160, 160, 3)
4 (160, 160, 3)
5 (160, 160, 3)
6 (160, 160, 3)
7 (160, 160, 3)
8 (160, 160, 3)
9 (160, 160, 3)
10 (160, 160, 3)
11 (160, 160, 3)
12 (160, 160, 3)
13 (160, 160, 3)
14 (160, 160, 3)
```
