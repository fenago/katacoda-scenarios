The Maximal-Margin Classifier is a hypothetical classifier that best explains how SVM works in
practice. The numeric input variables (x) in your data (the columns) form an n-dimensional
space. For example, if you had two input variables, this would form a two-dimensional space. A
hyperplane is a line that splits the input variable space. In SVM, a hyperplane is selected to
best separate the points in the input variable space by their class, either class 0 or class 1. In
two-dimensions you can visualize this as a line and let’s assume that all of our input points can
be completely separated by this line. For example:
B0 + (B1 × X1) + (B2 × X2) = 0 (26.1)
Where the coefficients (B1 and B2) that determine the slope of the line and the intercept
(B0) are found by the learning algorithm, and X1 and X2 are the two input variables. You can
make classifications using this line. By plugging in input values into the line equation, you can
calculate whether a new point is above or below the line.
11626.2. Soft Margin Classifier 117
- Above the line, the equation returns a value greater than 0 and the point belongs to the
first class (class 0).
- Below the line, the equation returns a value less than 0 and the point belongs to the
second class (class 1).
- A value close to the line returns a value close to zero and the point may be difficult to
classify.
- If the magnitude of the value is large, the model may have more confidence in the
prediction.