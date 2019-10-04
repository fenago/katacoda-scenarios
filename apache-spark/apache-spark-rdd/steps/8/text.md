**Step 2:** You can access the first element of the RDD using the first method as shown below.

`lettersRDD.first`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_022.png) 

As you can see from the screenshot above, the first element in the RDD has been returned.

You can use the take(n) method to read the n elements from your RDD. Where n is number of elements starting from the first element you want to read.

`lettersRDD.take(4)`{{execute}} 


But if you want to view all the elements in the RDD, you have to use collect method as shown below. Please note that using collect on a large dataset is not recommended, as collect will bring all the data of an RDD to the Driver program and load it in its memory. 

`lettersRDD.collect`{{execute}} 


![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 3/Selection_024.png)

