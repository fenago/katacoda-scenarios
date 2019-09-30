Let’s go back to our example and see how we can use cache() and persist() methods.

scala> val data = sc.textFile(“/some/path/records.txt”)

Once we load the file using the TextFile API, we can now cache or persist the data RDD. Before we can cache or persist we have to import the following.

scala> import org.apache.spark.storage.StorageLevel

And then use the cache() method, if we need the default implementation of storage only.

scala> data.cache()
