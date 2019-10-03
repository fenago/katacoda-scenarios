

**Step 7:** We now have our data in structured columns with named records. We can now simply convert it to a dataset using toDS method. 

But before we can use the toDS method, we need to import the implicits as shown below.

```
import ss.implicits._

val recordsDs = structRecords.toDS()
```

We now have our datacset recordsDs created from RDD.

**Step 8:** Let us now call the show method on our dataset and run the program.
 
```
recordsDs.show()
  }
}
```

