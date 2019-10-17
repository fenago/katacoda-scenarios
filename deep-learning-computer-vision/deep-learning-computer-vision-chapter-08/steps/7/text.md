
Once the iterators have been prepared, we can use them when fitting and evaluating a deep
learning model. For example, fitting a model with a data generator can be achieved by calling
the fit generator() function on the model and passing the training iterator (train it). The
validation iterator (val it) can be specified when calling this function via the validation data
argument. The steps per epoch argument must be specified for the training iterator in order
to define how many batches of images defines a single epoch.
For example, if you have 1,000 images in the training dataset (across all classes) and a batch
size of 64, then the steps per epoch would be about 16, or 1000 64 . Similarly, if a validation
iterator is applied, then the validation steps argument must also be specified to indicate the
number of batches in the validation dataset defining one epoch.

```
# define model
model = ...
# fit model
model.fit_generator(train_it, steps_per_epoch=16, validation_data=val_it,
validation_steps=8)
```

Once the model is fit, it can be evaluated on a test dataset using the evaluate generator()
function and passing in the test iterator (test it). The steps argument defines the number of
batches of samples to step through when evaluating the model before stopping.

```
# evaluate model
loss = model.evaluate_generator(test_it, steps=24)
```

Finally, if you want to use your fit model for making predictions on a very large dataset, you
can create an iterator for that dataset as well (e.g. predict it) and call the predict generator()
function on the model.

```
# make a prediction
yhat = model.predict_generator(predict_it, steps=24)
```

Let’s use our small dataset defined in the previous section to demonstrate how to define an `ImageDataGenerator` instance and prepare the dataset iterators in the next step.