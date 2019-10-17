The output of the model is, in fact, encoded candidate bounding boxes from three different grid
sizes, and the boxes are defined in the context of anchor boxes, carefully chosen based on an
analysis of the size of objects in the MSCOCO dataset. The script provided by experiencor
provides a function called decode netout() that will take each one of the NumPy arrays, one at
a time, and decode the candidate bounding boxes and class predictions. Further, any bounding
boxes that don’t confidently describe an object (e.g. all class probabilities are below a threshold)
are ignored. We will use a probability of 60% or 0.6. The function returns a list of BoundBox
instances that define the corners of each bounding box in the context of the input image shape
and class probabilities.

```
# define the anchors
anchors = [[116,90, 156,198, 373,326], [30,61, 62,45, 59,119], [10,13, 16,30, 33,23]]
# define the probability threshold for detected objects
class_threshold = 0.6
boxes = list()
for i in range(len(yhat)):
# decode the output of the network
boxes += decode_netout(yhat[i][0], anchors[i], class_threshold, input_h, input_w)
```

Next, the bounding boxes can be stretched back into the shape of the original image. This
is helpful as it means that later we can plot the original image and draw the bounding boxes,
hopefully detecting real objects. The experiencor script provides the correct yolo boxes()
function to perform this translation of bounding box coordinates, taking the list of bounding
boxes, the original shape of our loaded photograph, and the shape of the input to the network
as arguments. The coordinates of the bounding boxes are updated directly.

```
# correct the sizes of the bounding boxes for the shape of the image
correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)
```

The model has predicted a lot of candidate bounding boxes, and most of the boxes will
be referring to the same objects. The list of bounding boxes can be filtered and those boxes
that overlap and refer to the same object can be merged. We can define the amount of overlap
as a configuration parameter, in this case, 50% or 0.5. This filtering of bounding box regions
is generally referred to as non-maximal suppression and is a required post-processing step.
The experiencor script provides this via the do nms() function that takes the list of bounding
boxes and a threshold parameter. Rather than purging the overlapping boxes, their predicted
probability for their overlapping class is cleared. This allows the boxes to remain and be used if
they also detect another object type.
```
# suppress non-maximal boxes
do_nms(boxes, 0.5)
```

This will leave us with the same number of boxes, but only very few of interest. We can
retrieve just those boxes that strongly predict the presence of an object: that is are more than
60% confident. This can be achieved by enumerating over all boxes and checking the class
prediction values. We can then look up the corresponding class label for the box and add it to
the list. Each box must be considered for each class label, just in case the same box strongly
predicts more than one object. We can develop a get boxes() function that does this and
takes the list of boxes, known labels, and our classification threshold as arguments and returns
parallel lists of boxes, labels, and scores.

```
# get all of the results above a threshold
def get_boxes(boxes, labels, thresh):
v_boxes, v_labels, v_scores = list(), list(), list()
# enumerate all boxes
for box in boxes:
# enumerate all possible labels
for i in range(len(labels)):
# check if the threshold for this label is high enough
if box.classes[i] > thresh:
v_boxes.append(box)
v_labels.append(labels[i])
v_scores.append(box.classes[i]*100)
# don't break, many labels may trigger for one box
return v_boxes, v_labels, v_scores
```
