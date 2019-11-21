One of the impressive examples of the CycleGAN in the paper was to transform photographs of
horses to zebras, and the reverse, zebras to horses. The authors of the paper referred to this as
the problem of object transfiguration and it was also demonstrated on photographs of apples
and oranges. In this tutorial, we will develop a CycleGAN from scratch for image-to-image
translation (or object transfiguration) from horses to zebras and the reverse. We will refer to
this dataset as horses2zebra.

You will see the following directory structure:
horse2zebra
	- testA
	- testB
	- trainA
	- trainB

The A category refers to horse and B category refers to zebra, and the dataset is comprised
of train and test elements. We will load all photographs and use them as a training dataset.
The photographs are square with the shape 256 × 256 and have filenames like n023814602.jpg.
The example below will load all photographs from the train and test folders and create an array
of images for category A and another for category B. Both arrays are then saved to a new file in
compressed NumPy array format.


We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_26/01_load_prepare_dataset.py` to view file.

#### Run Code
Now, run the python code by running: `python 01_load_prepare_dataset.py`{{execute}}
