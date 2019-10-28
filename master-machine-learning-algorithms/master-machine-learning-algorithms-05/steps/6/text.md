We can calculate the new coefficient values using a simple update equation.

```
b = b + alpha × (y − prediction) × prediction × (1 − prediction) x X
```

Where b is the coefficient we are updating and prediction is the output of making a prediction
using the model. Alpha is a parameter that you must specify at the beginning of the training
run. This is the learning rate and controls how much the coefficients (and therefore the model)
changes or learns each time it is updated. Larger learning rates are used in online learning
(when we update the model for each training instance). Good values might be in the range 0.1
to 0.3. Let’s use a value of 0.3.
You will notice that the last term in the equation is x, this is the input value for the
coefficient. You will notice that the B0 does not have an input. This coefficient is often called
the bias or the intercept and we can assume it always has an input value of 1.0. This assumption
can help when implementing the algorithm using vectors or arrays. Let’s update the coefficients
using the prediction (0.5) and coefficient values (0.0) from the previous section.

```
B0 = B0 + 0.3 × (0 − 0.5) × 0.5 × (1 − 0.5) × 1.0
B1 = B1 + 0.3 × (0 − 0.5) × 0.5 × (1 − 0.5) × 2.7810836
B2 = B2 + 0.3 × (0 − 0.5) × 0.5 × (1 − 0.5) × 2.550537003
```

**or**

```
B0 = −0.0375
B1 = −0.104290635
B2 = −0.095645138
```
