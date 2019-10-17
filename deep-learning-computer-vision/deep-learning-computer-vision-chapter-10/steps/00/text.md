This tutorial is divided into three parts; they are:
1. Images as 3D Arrays
2. Manipulating Image Channels
3. Keras Channel Ordering

#### Images as 3D Arrays
An image can be stored as a three-dimensional array in memory. Typically, the image format
has one dimension for rows (height), one for columns (width) and one for channels. If the image
is black and white (grayscale), the channels dimension may not be explicitly present, e.g. there
is one unsigned integer pixel value for each (row, column) coordinate in the image. Colored
images typically have three channels. A given pixel value at the (row, column) coordinate will
have red, green, and blue components. Deep learning neural networks require that image data
be provided as three-dimensional arrays.
This applies even if your image is grayscale. In this case, the additional dimension for the
single color channel must be added. There are two ways to represent the image data as a three
dimensional array. The first involves having the channels as the last or third dimension in
the array. This is called channels last. The second involves having the channels as the first
dimension in the array, called channels first.

- Channels Last. Image data is represented in a three-dimensional array where the last
channel represents the color channels, e.g. [rows][cols][channels].
- Channels First. Image data is represented in a three-dimensional array where the first
channel represents the color channels, e.g. [channels][rows][cols].

Some image processing and deep learning libraries prefer channels first ordering, and some
prefer channels last. As such, it is important to be familiar with the two approaches to
representing images.