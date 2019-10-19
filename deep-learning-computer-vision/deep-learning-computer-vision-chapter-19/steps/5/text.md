The first step is to develop a baseline model. This is critical as it both involves developing
the infrastructure for the test harness so that any model we design can be evaluated on the
dataset, and it establishes a baseline in model performance on the problem, by which all
improvements can be compared. The design of the test harness is modular, and we can develop
a separate function for each piece. This allows a given aspect of the test harness to be modified
or inter-changed, if we desire, separately from the rest. We can develop this test harness with
five key elements. They are the loading of the dataset, the preparation of the dataset, the
definition of the model, the evaluation of the model, and the presentation of results

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_19/02_baseline_model.py` to view file.

#### Run Code
**Note:** It will take some time to complete.

Now, run the python code by running: `python 02_baseline_model.py`{{execute}}
