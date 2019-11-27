
Recall that the Wasserstein loss seeks scores for real and fake that are more different during
training. We can see this towards the end of the run, such as the final epoch where the c1 loss
for real examples is 5.338 (really -5.338) and the c2 loss for fake examples is -14.260, and this
separation of about 10 units is consistent at least for the prior few iterations. We can also see
that in this case, the model is scoring the loss of the generator at around 20. Again, recall that
we update the generator via the critic model and treat the generated examples as real with the
target of -1, therefore the score can be interpreted as a value around -20, close to the loss for
fake samples.

```
...
>961, c1=5.110, c2=-15.388 g=19.57916.5. How to Train a Wasserstein GAN Model 325
>962, c1=6.116, c2=-15.222 g=20.054
>963, c1=4.982, c2=-15.192 g=21.048
>964, c1=4.238, c2=-14.689 g=23.911
>965, c1=5.585, c2=-14.126 g=19.578
>966, c1=4.807, c2=-14.755 g=20.034
>967, c1=6.307, c2=-16.538 g=19.572
>968, c1=4.298, c2=-14.178 g=17.956
>969, c1=4.283, c2=-13.398 g=17.326
>970, c1=5.338, c2=-14.260 g=19.927
```

