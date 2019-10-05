The difference between cache() and persist() methods is that the cache() uses the default storage level of StorageLevel.MEMORY_ONLY, while the persist() method can have the combination of various storage levels as seen below.


#### Persistence Storage Levels

Level | Description
--- | --- 
MEMORY_ONLY` | 	This is the default storage level. The RDD when cached is stored in memory only. If the RDD doesn't fit in the memory, few partitions which do not fit are computed on the fly when an action is called. The RDDs are stored as deserialized Java objects.
`MEMORY_AND_DISK` | This storage level uses disk to store few partitions of RDD if they do not fit in the memory. So, instead of recomputing the RDD partitions which do not fit in memory, they are spilled to disk. The RDDs are stored as deserialized Java objects.
`MEMORY_ONLY_SER` | This storage level is same as MEMORY_ONLY but RDDs are stored as serialized Java objects. Serialization is more space efficient when compared to deserialized objects but is CPU intensive operation.
`MEMORY_AND_DISK_SER` | This storage level is same as MEMORY_AND_DISK but RDDs are stored as serialized Java objects in memory. The partitions which don't fit in memory are spilled to disk.
`DISK_ONLY` | In this storage level, the RDDs are stored to the disk only and not in memory. This requires low space when compared to persisting in memory but is CPU intensive.
`MEMORY_ONLY_2 MEMORY_AND_DISK_2 MEMORY_AND_DISK_2` | All these levels are same as above but store the RDD partitions with replication factor of 2. Meaning each partition is stored on two nodes of a cluster with replication.
