The process of model improvement may continue for as long as we have ideas and the time
and resources to test them out. At some point, a final model configuration must be chosen and
adopted. In this case, we will keep things simple and use the baseline model as the final model.
First, we will finalize our model, by fitting a model on the entire training dataset and saving
the model to file for later use. We will then load the model and evaluate its performance on the
hold out test dataset, to get an idea of how well the chosen model actually performs in practice.
Finally, we will use the saved model to make a prediction on a single image.

#### Save Final Model
A final model is typically fit on all available data, such as the combination of all train and test
dataset. In this tutorial, we are intentionally holding back a test dataset so that we can estimate
the performance of the final model, which can be a good idea in practice. As such, we will fit
our model on the training dataset only.

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/05_save_final_model.py` to view file.


#### Run Code
**Note:** It will take some time to complete.

Now, run the python code by running: `python 05_save_final_model.py`{{execute}}

