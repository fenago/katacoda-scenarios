The result is a list of bounding boxes, where each bounding box defines a lower-left-corner
of the bounding box, as well as the width and height. If we assume there is only one face in
the photo for our experiments, we can determine the pixel coordinates of the bounding box as
follows. Sometimes the library will return a negative pixel index, and I think this is a bug. We
can fix this by taking the absolute value of the coordinates.

```
# extract the bounding box from the first face
x1, y1, width, height = results[0][box]
# bug fix
x1, y1 = abs(x1), abs(y1)
x2, y2 = x1 + width, y1 + height
```

We can use these coordinates to extract the face.

```
# extract the face
face = pixels[y1:y2, x1:x2]
```

We can then use the PIL library to resize this small image of the face to the required size;
specifically, the model expects square input faces with the shape 160 × 160.

```
# resize pixels to the model size
image = Image.fromarray(face)
image = image.resize((160, 160))
face_array = asarray(image)
```

We can use this function to extract faces as needed in the next section that can be provided
as input to the FaceNet model