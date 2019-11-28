
It is useful to see another example of this type of failure. In this case, the configuration of
the Adam optimization algorithm can be modified to use the defaults, which in turn makes the
updates to the models aggressive and causes a failure for the training process to find a point of
equilibrium between training the two models. For example, the discriminator can be compiled
as follows:

```
...
# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

And the composite GAN model can be compiled as follows:

```
...
# compile model
model.compile(loss='binary_crossentropy', optimizer='adam')
```
