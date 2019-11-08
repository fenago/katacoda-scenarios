
Now, I'm going to extract the first line, the first row from that RDD, by using the first function. So, now the header RDD will contain one entry that is just that row of column headers. And now, look what's going on in the above code, I'm using filter on my original data that contains all of the information in that CSV file, and I'm defining a filter function that will only let lines through if that line is not equal to the contents of that initial header row. What I've done here is, I've taken my raw CSV file and I've stripped out the first line by only allowing lines that do not equal that first line to survive, and I'm returning that back to the rawData RDD variable again. So, I'm taking rawData, filtering out that first line, and creating a new rawData that only contains the data itself. With me so far? It's not that complicated.

Now, we're going to use a map function. What we need to do next is start to make more structure out of this information. Right now, every row of my RDD is just a line of text, it is comma-delimited text, but it's still just a giant line of text, and I want to take that comma-separated value list and actually split it up into individual fields. At the end of the day, I want each RDD to be transformed from a line of text that has a bunch of information separated by commas into a Python list that has actual individual fields for each column of information that I have. So, that's what this lambda function does:

```
csvData = rawData.map(lambda x: x.split(",")) 
```

It calls the built-in Python function split, which will take a row of input, and split it on comma characters, and divide that into a list of every field delimited by commas.

The output of this map function, where I passed in a lambda function that just splits every line into fields based on commas, is a new RDD called csvData. And, at this point, csvData is an RDD that contains, on every row, a list where every element is a column from my source data. Now, we're getting close.

It turns out that in order to use a decision tree with MLlib, a couple of things need to be true. First of all, the input has to be in the form of LabeledPoint data types, and it all has to be numeric in nature. So, we need to transform all of our raw data into data that can actually be consumed by MLlib, and that's what the createLabeledPoints function that we skipped past earlier does. We'll get to that in just a second, first here's the call to it:

```
trainingData = csvData.map(createLabeledPoints) 
```