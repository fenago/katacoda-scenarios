It is also possible to remove the persisted RDDs manually. You simply have to use the unpersist() function to the RDD you want to unpersist.

`data2.unpersist()`{{execute}} 

However, if you choose not to remove the persisted RDDs manually, Spark automatically removes the partitions based on Least Recently Used (LRU) cache policy, when there is too much data cached in memory. So, you need not worry about breaking a job when memory is full.
