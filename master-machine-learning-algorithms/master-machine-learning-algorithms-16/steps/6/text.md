This section lists some heuristics for best preparing your data for AdaBoost.

- **Quality Data:** Because the ensemble method continues to attempt to correct misclassification’s in the training data, you need to be careful that the training data is of a
high-quality.
- **Outliers:** Outliers will force the ensemble down the rabbit hole of working hard to correct
for cases that are unrealistic. These could be removed from the training dataset.
- **Noisy Data:** Noisy data, specifically noise in the output variable can be problematic. If
possible, attempt to isolate and clean these from your training dataset.