In addition to choosing the number of codebook vectors, an initial learning rate must be
specified. A good default value is 0.3, but values are typically between 0.1 and 0.5. The learning
rate is used to update the codebook vectors. In this section we will look at the rule used to
update the codebook vectors for one training pattern. Let’s take the first training pattern:

```
X1 = 3:393533211, X2 = 2.331273381, Y = 0.
```

The update rule for one pattern is as follows:

1. Calculate the distance from the training pattern to each codebook vector.
2. Select the most similar codebook vector, called the Best Matching Unit (BMU).
3. Update the best matching unit to be closer to the training pattern if it has the same class,
otherwise further away.

