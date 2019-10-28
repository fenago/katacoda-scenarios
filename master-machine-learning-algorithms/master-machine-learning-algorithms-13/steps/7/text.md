LVQ learns a population of codebook vectors from the training data. This section is broken up
into 3 parts:
1. Initial Codebook Vectors.
2. Update Codebook Vectors for One Pattern.
3. Update For One Epoch.

#### Initial Codebook Vectors
The number of codebook vectors often depends on the size and complexity of the problem.
Because we are working with a simple problem and for demonstration purposes we will select a
small number of codebook vectors of 4, two of each class. The values for the vectors can be
chosen randomly or selected from the input data. We will use the latter. The table below lists
the selected codebook vectors: