In this chapter you will discover the k-Nearest Neighbors (KNN) algorithm for classification
and regression. After reading this chapter you will know.
- The model representation used by KNN.
- How a model is learned using KNN (hint, it’s not).
- How to make predictions using KNN
- The many names for KNN including how different fields refer to it.
- How to prepare your data to get the most from KNN.
Let’s get started.


#### KNN Model Representation
The model representation for KNN is the entire training dataset. It is as simple as that. KNN
has no model other than storing the entire dataset, so there is no learning required. Efficient
implementations can store the data using complex data structures like k-d trees to make look-up
and matching of new patterns during prediction efficient. Because the entire training dataset is
stored, you may want to think carefully about the consistency of your training data. It might be
a good idea to curate it, update it often as new data becomes available and remove erroneous
and outlier data