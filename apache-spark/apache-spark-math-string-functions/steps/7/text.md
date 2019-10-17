There are a plethora of String functions available in Spark. Let us look at few of them now.

**Step 1:** As usual, let us first create the List and create a dataset from it. Please make sure to specify imports again if you have closed the Spark session.

```val quote = List("I have no special talent.",
  "I am only passionately curious.",
  "I have a dream.",
  "I came, I saw, I conquered.")```{{execute}} 

`val quoteDS = quote.toDS().cache()`{{execute}} 

Let us use the show method to display the dataset as shown below.

`quoteDS.show()`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_044.png)
