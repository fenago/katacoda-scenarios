In this tutorial, we will use the so-called maps dataset used in the Pix2Pix paper. This is a
dataset comprised of satellite images of New York and their corresponding Google maps pages.
The image translation problem involves converting satellite photos to Google maps format, or
the reverse, Google maps images to Satellite photos.

Download the dataset and unzip it into your current working directory. This will create a
directory called maps/ with the following structure:

```
maps
    * train
    * val
```