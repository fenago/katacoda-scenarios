With the binary tree representation of the CART model described above, making predictions is
relatively straightforward. Given a new input, the tree is traversed by evaluating the specific
input started at the root node of the tree. A learned binary tree is actually a partitioning of the
input space. You can think of each input variable as a dimension on an p-dimensional space.
The decision tree split this up into rectangles (when p = 2 input variables) or hyper-rectangles
with more inputs. New data is filtered through the tree and lands in one of the rectangles and
the output value for that rectangle is the prediction made by the model. This gives you some
feeling for the type of decisions that a CART model is capable of making, e.g. boxy decision
boundaries. For example, given the input of height = 160 cm and weight = 65 kg, we would
traverse the above tree as follows:
1. **Height** > 180 cm: No
2. **Weight** > 80 kg: No
3. Therefore: **Female**
