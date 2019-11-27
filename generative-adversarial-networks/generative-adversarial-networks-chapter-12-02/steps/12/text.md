We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_12/04_inception_score_cifar10.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_inception_score_cifar10.py`{{execute}}

Running the example may take some time depending on the speed of your workstation. It
may also require a large amount of RAM. If you have trouble with the example, try reducing
the number of images in the training dataset. Running the example loads the dataset, prepares
the model, and calculates the inception score on the CIFAR-10 training dataset. We can see
that the score is 11.3, which is close to the expected score of 11.24.

```
loaded (50000, 32, 32, 3)
score 11.317895 0.14821531
```
