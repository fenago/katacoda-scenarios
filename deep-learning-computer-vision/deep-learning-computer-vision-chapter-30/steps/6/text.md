We can use the mtcnn library to create a face detector and extract faces for our use with
the FaceNet face detector models in subsequent sections. The first step is to load an image as a
NumPy array, which we can achieve using the PIL library and the open() function. We will also
convert the image to RGB, just in case the image has an alpha channel or is black and white.

```
# load image from file
image = Image.open(filename)
# convert to RGB, if needed
image = image.convert(RGB)
# convert to array
pixels = asarray(image)
```

Next, we can create an MTCNN face detector class and use it to detect all faces in the
loaded photograph.

```
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
results = detector.detect_faces(pixels)
```
