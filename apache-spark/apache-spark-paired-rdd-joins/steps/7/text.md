Let us now perform actions on the paired RDDs and also look at caching and persisting RDDs. Also, let us continue the program from previous task and apply actions over them.

 
**Step 1:** We shall be using the joined RDD for all the actions we perform in this task. Since we shall be using this RDD more than once, let us persist it before performing these actions so that the application does not process all the transformations over and over again whenever an action is called.

```
joined.persist(StorageLevel.MEMORY_AND_DISK_SER)
```

You might see an error about the missing import. If so, please add the following import to the list of imports.

```
import org.apache.spark.storage.StorageLevel
```

You may use your desired level of persist storage level above.
