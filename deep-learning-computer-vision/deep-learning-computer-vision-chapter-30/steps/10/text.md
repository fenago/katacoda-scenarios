So far, so good. Next, we can extend this example to step over each subdirectory for a given
dataset (e.g. train or val), extract the faces, and prepare a dataset with the name as the
output label for each detected face. The load faces() function below will load all of the faces
into a list for a given directory, e.g. 5-celebrity-faces-dataset/train/ben afflek/.

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/04_extract_faces_dataset.py` to view file.


#### Run Code
Now, run the python code by running: `python 04_extract_faces_dataset.py`{{execute}}


Running the example may take a moment. First, all of the photos in the train dataset
are loaded, then faces are extracted, resulting in 93 samples with square face input and a
class label string as output. Then the val dataset is loaded, providing 25 samples that can be
used as a test dataset. Both datasets are then saved to a compressed NumPy array file called
5-celebrity-faces-dataset.npz that is about three megabytes and is stored in the current
working directory.

```
>loaded 14 examples for class: ben_afflek
>loaded 19 examples for class: madonna
>loaded 17 examples for class: elton_john
>loaded 22 examples for class: mindy_kaling
>loaded 21 examples for class: jerry_seinfeld
(93, 160, 160, 3) (93,)
>loaded 5 examples for class: ben_afflek
>loaded 5 examples for class: madonna
>loaded 5 examples for class: elton_john
>loaded 5 examples for class: mindy_kaling
>loaded 5 examples for class: jerry_seinfeld
(25, 160, 160, 3) (25,)
```
