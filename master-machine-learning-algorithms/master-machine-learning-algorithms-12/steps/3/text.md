KNN makes predictions using the training dataset directly. Predictions are made for a new
data point by searching through the entire training set for the k most similar instances (the
neighbors) and summarizing the output variable for those k instances. For regression this might
be the mean output variable, in classification this might be the mode (or most common) class
value.
To determine which of the k instances in the training dataset are most similar to a new
input a distance measure is used. For real-valued input variables, the most popular distance
9922.2. Making Predictions with KNN 100
measure is Euclidean distance. Euclidean distance is calculated as the square root of the sum of
the squared differences between a point a and point b across all input attributes i.


Other popular distance measures include:
- Hamming Distance: Calculate the distance between binary vectors.
- Manhattan Distance: Calculate the distance between real vectors using the sum of their
absolute difference. Also called City Block Distance.
- Minkowski Distance: Generalization of Euclidean and Manhattan distance.


