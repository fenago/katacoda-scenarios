Generally, it is a good idea to prepare data for LVQ in the same way as you would prepare it
for k-Nearest Neighbors.

- **Classification:** LVQ is a classification algorithm that works for both binary (two-class)
and multiclass classification algorithms. The technique has been adapted for regression.
- **Multiple-Passes:** Good technique with LVQ involves performing multiple passes of the
training dataset over the codebook vectors (e.g. multiple learning runs). The first with
a higher learning rate to settle the pool of codebook vectors and the second run with a
small learning rate to fine tune the vectors.
- **Multiple Best Matches:** Extensions of LVQ select multiple best matching units to
modify during learning, such as one of the same class and one of a different class which
are drawn toward and away from a training sample respectively. Other extensions use a
custom learning rate for each codebook vector. These extensions can improve the learning
process.
- **Normalize Inputs:** Traditionally, inputs are normalized (rescaled) to values between 0
and 1. This is to avoid one attribute from dominating the distance measure. If the input
data is normalized, then the initial values for the codebook vectors can be selected as
random values between 0 and 1.
- **Feature Selection:** Feature selection that can reduce the dimensionality of the input
variables can improve the accuracy of the method. LVQ suffers from the same curse of
dimensionality in making predictions as k-Nearest Neighbors.