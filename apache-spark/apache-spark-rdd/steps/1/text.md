Resilient Distributed Dataset also known as RDD is the basic data structure of Spark, which is immutable and fault tolerant collection of elements that can be computed and stored in parallel over a cluster of machines. Let us look at each word individually and try to understand it in detail.

**Resilient:** The RDDs are fault tolerant to any data loss. Any loss in data due to hardware failure or data corruption can be recovered using the RDD lineage graph or DAG. 

**Distributed:** The RDDs can be distributed over a cluster of machines in memory.

**Dataset:** The RDDs can be created with any of the datasets such as a text file, JSON, CSV, Database file via JDBC etc.
