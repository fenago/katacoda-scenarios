
**Step 5:** We now have to implement the merge function so that the buffer outputs from all the tasks are merged.

```
def merge(b1: Average, b2: Average): Average = {
  b1.sum += b2.sum
  b1.count += b2.count
  b1
}
```

This function simply adds the sum and counts of all the buffers and returns back the buffer.

The program at this point should look like in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_031.png)

**Step 6:** Next, similar to the evaluate method in the previous task we have to implement the finish method. The finish method contains the logic to compute the average i.e., dividing the sum with count.

def finish(reduction: Average): Double = reduction.sum / reduction.count


**Step 7:** We now have to implement the encoders for buffer and output values using the bufferEncoder and outputEncoder. These encoders are required for serialization purposes to translate between the Scala and Spark types.


def bufferEncoder: Encoder[Average] = Encoders.product
def outputEncoder: Encoder[Double] = Encoders.scalaDouble



The error below the object name should have been gone by now as we have implemented all the methods required to create a typed UDAF.

The program should now look like the one shown in the screenshot.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_032.png) 
