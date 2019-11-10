We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_24/03_object_detection.py` to view file.

#### Run Code

Now, run the python code by running: `python 03_object_detection.py`{{execute}}

Running the example again prints the shape of the raw output from the model. This is
followed by a summary of the objects detected by the model and their confidence. We can see
that the model has detected three zebra, all above 90% likelihood.

```
[(1, 13, 13, 255), (1, 26, 26, 255), (1, 52, 52, 255)]
zebra 94.91060376167297
zebra 99.86329674720764
zebra 96.8708872795105
```

Example output from performing object detection with the YOLOv3 model.

A plot of the photograph is created and the three bounding boxes are plotted. We can see
that the model has indeed successfully detected the three zebra in the photograph.

![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-chapter-24/steps/11/1.JPG)
