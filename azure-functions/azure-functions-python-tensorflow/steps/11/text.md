In the editor, open **predict.py** and look at the _initialize function near the top of the file. Notice that the TensorFlow model is loaded from disk the first time the function is executed and saved to global variables. The loading from disk is skipped in subsequent executions of the **_initialize** function. Caching the model in memory with this technique speeds up later predictions.

