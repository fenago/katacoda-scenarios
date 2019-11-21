
We can also define a function to select a subset of the training dataset in which we keep the labels and train the supervised version of the discriminator model. The select supervised samples()
function below implements this and is careful to ensure that the selection of examples is random
and that the classes are balanced. The number of labeled examples is parameterized and set at
100, meaning that each of the 10 classes will have 10 randomly selected examples.

```
# select a supervised subset of the dataset, ensures classes are balanced
def select_supervised_samples(dataset, n_samples=100, n_classes=10):
X, y = dataset
X_list, y_list = list(), list()
n_per_class = int(n_samples / n_classes)
for i in range(n_classes):
# get all images for this class
X_with_class = X[y == i]
# choose random instances
ix = randint(0, len(X_with_class), n_per_class)
# add to list
[X_list.append(X_with_class[j]) for j in ix]
[y_list.append(i) for j in ix]
return asarray(X_list), asarray(y_list)
```
