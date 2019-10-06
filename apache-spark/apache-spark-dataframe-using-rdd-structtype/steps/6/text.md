
 

**Step 7:** We now have our data in structured columns with named records. We can now simply convert it to a dataFrame using toDF method. 

But before we can use the toDF method, we need to import the implicits as shown below.

```
import ss.implicits._

val recordsDf = structRecords.toDF()
```

We now have our dataFrame recordsDf created from RDD.

 



**Step 8:** Let us now call the show method on our dataFrame and run the program.

```
recordsDf.show()

  }

}
```

The output is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_022.png)

To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.rddToDf"`{{execute}} 

Task is complete!
