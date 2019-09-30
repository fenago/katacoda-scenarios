However, if we want to use the various storage levels as explained above, we have to use the persist() method and specify the desired storage level. So the code will look like:

scala> data.persist(StorageLevel.MEMORY_AND_DISK_SER)

At this point of time, we have simply specified out storage level for persistence. The actual persistence happens when the action on the RDD is called.

scala> data.take(5)

After this action is completed, the RDD is stored in the memory and any partitions that do not fit in memory are spilled to disk. When we trigger another action as below, the RDD will not be computed again as it is already computed and persisted. This will reduce the total time taken to complete the job without having to compute the same RDD over and over again.

scala> data.count()