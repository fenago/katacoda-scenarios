
Let's go back to our script:

```
rawData = sc.textFile("e:/sundog-consult/udemy/datascience/PastHires.csv") 
header = rawData.first() 
rawData = rawData.filter(lambda x:x != header) 
```

The first thing we need to do is read that CSV data in, and we're going to throw away that first row, because that's our header information, remember. So, here's a little trick for doing that. We start off by importing every single line from that file into a raw data RDD, and I could call that anything I want, but we're calling it sc.textFile. SparkContext has a textFile function that will take a text file and create a new RDD, where each entry, each line of the RDD, consists of one line of input.

**Note:**

Make sure you change the path to that file to wherever you actually installed it, otherwise it won't work.
