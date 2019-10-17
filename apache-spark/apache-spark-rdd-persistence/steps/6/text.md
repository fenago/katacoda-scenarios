Let's go back to our example and see how we can use cache() and persist() methods.

`val data2 = sc.textFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_4/treasure_island.txt")`{{execute}} 

Once we load the file using the TextFile API, we can now cache or persist the data RDD. Before we can cache or persist we have to import the following.

`import org.apache.spark.storage.StorageLevel`{{execute}} 

And then use the cache() method, if we need the default implementation of storage only.

`data2.cache()`{{execute}} 
