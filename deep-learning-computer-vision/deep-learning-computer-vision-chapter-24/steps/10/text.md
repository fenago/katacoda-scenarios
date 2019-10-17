We can call this function with our list of boxes. We also need a list of strings containing
the class labels known to the model in the correct order used during training, specifically those
class labels from the MSCOCO dataset. Thankfully, this is provided in the experiencor script.
```
# define the labels
labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
"boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
"bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
"backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
"sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",24.4. Object Detection With YOLOv3 381
"tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl",
"banana",
"apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut",
"cake",
"chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop",
"mouse",
"remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
"refrigerator",
"book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]
# get the details of the detected objects
v_boxes, v_labels, v_scores = get_boxes(boxes, labels, class_threshold)
```

Now that we have those few boxes of strongly predicted objects, we can summarize them.
```
# summarize what we found
for i in range(len(v_boxes)):
print(v_labels[i], v_scores[i])
```

We can also plot our original photograph and draw the bounding box around each detected
object. This can be achieved by retrieving the coordinates from each bounding box and creating
a Rectangle object.

```
box = v_boxes[i]
# get coordinates
y1, x1, y2, x2 = box.ymin, box.xmin, box.ymax, box.xmax
# calculate width and height of the box
width, height = x2 - x1, y2 - y1
# create the shape
rect = Rectangle((x1, y1), width, height, fill=False, color='white')
# draw the box
ax.add_patch(rect)
```

We can also draw a string with the class label and confidence.
```
# draw text and score in top left corner
label = "%s (%.3f)" % (v_labels[i], v_scores[i])
pyplot.text(x1, y1, label, color='white')
```

The draw boxes() function below implements this, taking the filename of the original
photograph and the parallel lists of bounding boxes, labels and scores, and creates a plot
showing all detected objects.

```
# draw all results
def draw_boxes(filename, v_boxes, v_labels, v_scores):
# load the image
data = pyplot.imread(filename)
# plot the image24.4. Object Detection With YOLOv3 382
pyplot.imshow(data)
# get the context for drawing boxes
ax = pyplot.gca()
# plot each box
for i in range(len(v_boxes)):
box = v_boxes[i]
# get coordinates
y1, x1, y2, x2 = box.ymin, box.xmin, box.ymax, box.xmax
# calculate width and height of the box
width, height = x2 - x1, y2 - y1
# create the shape
rect = Rectangle((x1, y1), width, height, fill=False, color='white')
# draw the box
ax.add_patch(rect)
# draw text and score in top left corner
label = "%s (%.3f)" % (v_labels[i], v_scores[i])
pyplot.text(x1, y1, label, color='white')
# show the plot
pyplot.show()
```

We can then call this function to plot our final result.

```
# draw what we found
draw_boxes(photo_filename, v_boxes, v_labels, v_scores)
```

We now have all of the elements required to make a prediction using the YOLOv3 model,
interpret the results, and plot them for review. 