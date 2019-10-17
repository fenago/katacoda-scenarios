Next, we need a dataset to model. In this tutorial, we will use the kangaroo dataset, made
available by Huynh Ngoc Anh (experiencor). The dataset is comprised of about 160 photographs
that contain kangaroos, and XML annotation files that provide bounding boxes for the kangaroos
in each photograph. The Mask R-CNN is designed to learn to predict both bounding boxes for
objects as well as masks for those detected objects, and the kangaroo dataset does not provide
masks. As such, we will use the dataset to learn a kangaroo object detection task, and ignore
the masks and not focus on the image segmentation capabilities of the model.
There are a few steps required in order to prepare this dataset for modeling and we will work
through each in turn in this section, including downloading the dataset, parsing the annotations
file, developing a KangarooDataset object that can be used by the Mask RCNN library, then
testing the dataset object to confirm that we are loading images and annotations correctly.


#### Install Dataset
The first step is to download the dataset into your current working directory. This can be
achieved by cloning the GitHub repository directly, as follows:

`git clone https://github.com/experiencor/kangaroo.git`{{execute}} 


This will create a new directory called kangaroo with a subdirectory called images/ that
contains all of the JPEG photos of kangaroos and a subdirectory called annotes/ that contains
all of the XML files that describe the locations of kangaroos in each photo.

```
kangaroo
    - annots
    - images
```

Looking in each subdirectory, you can see that the photos and annotation files use a consistent
naming convention, with filenames using a 5-digit zero-padded numbering system; for example:

```
images/00001.jpg
images/00002.jpg
images/00003.jpg
...
annots/00001.xml
annots/00002.xml
annots/00003.xml
...
```

This makes matching photographs and annotation files together very easy. We can also see
that the numbering system is not contiguous, that there are some photos missing, e.g. there is
no 00007 JPG or XML file. This means that we should focus on loading the list of actual files
in the directory rather than using a numbering system.