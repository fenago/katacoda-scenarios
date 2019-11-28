

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_17/07_inference_sgan.py` to view file.

#### Run Code
Now, run the python code by running: `python 07_inference_sgan.py`{{execute}}

Running the example loads the model and evaluates it on the MNIST dataset.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.
In this case, we can see that the model achieves the expected performance of 95.432% on
the training dataset, confirming we have loaded the correct model. We can also see that the
accuracy on the holdout test dataset is as good, or slightly better, at about 95.920%. This
shows that the learned classifier has good generalization.

```
Train Accuracy: 95.432%
Test Accuracy: 95.920%
```

We have successfully demonstrated the training and evaluation of a semi-supervised classifier
model fit via the GAN architecture.