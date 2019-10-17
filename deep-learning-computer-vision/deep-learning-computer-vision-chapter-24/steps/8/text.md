We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_24/02_make_prediction.py` to view file.

#### Run Code

Now, run the python code by running: `python 02_make_prediction.py`{{execute}}

Running the example returns a list of three NumPy arrays, the shape of which is displayed
as output. These arrays predict both the bounding boxes and class labels but are encoded.
They must be interpreted.

```
[(1, 13, 13, 255), (1, 26, 26, 255), (1, 52, 52, 255)]
```
