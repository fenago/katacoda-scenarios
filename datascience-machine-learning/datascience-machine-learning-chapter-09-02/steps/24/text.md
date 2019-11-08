This chapter was originally produced for Spark 1, so let's talk about what's new in Spark 2, and what new capabilities exist in MLlib now.

So, the main thing with Spark 2 is that they moved more and more toward Dataframes and Datasets. Datasets and Dataframes are kind of used interchangeably sometimes. Technically a dataframe is a Dataset of row objects, they're kind of like RDDs, but the only difference is that, whereas an RDD just contains unstructured data, a Dataset has a defined schema to it.

A Dataset knows ahead of time exactly what columns of information exists in each row, and what types those are. Because it knows about the actual structure of that Dataset ahead of time, it can optimize things more efficiently. It also lets us think of the contents of this Dataset as a little, mini database, well, actually, a very big database if it's on a cluster. That means we can do things like issue SQL queries on it.

This creates a higher-level API with which we can query and analyze massive Datasets on a Spark cluster. It's pretty cool stuff. It's faster, it has more opportunities for optimization, and it has a higher-level API that's often easier to work with.
