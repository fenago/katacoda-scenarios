Repeat this process for the rest of the dataset. One pass through the dataset is called an epoch.
Now repeat the process for a further 15 epochs for a total of 160 iterations (16 epochs × 10
updates per epoch). It is possible to keep track of the loss or the accuracy of the model for each
epoch. This is a great way to get insight into whether the algorithm is converging or whether
there is a bug in the implementation. If you plot the accuracy for the model at the end of each
epoch, you should see something that looks like the following graph:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/11/1.JPG)


You can see that after 16 epochs that we achieve an accuracy of 100% on the training data.
You should arrive at final values for the coefficients that look like the following:

```
B1 = 0.552391765
B2 = −0.724533592
```

The form of the learned hyperplane is therefore:

```
0 + (0.552391765 × X1) + (−0.724533592 × X2) = 0
```
