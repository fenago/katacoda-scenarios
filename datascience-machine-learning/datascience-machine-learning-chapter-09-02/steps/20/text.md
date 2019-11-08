
The next thing I'm going to do is split those up:

```
fields = rawData.map(lambda x: x.split("\t")) 
```

I'm going to split up each document based on their tab delimiters into a Python list, and create a new fields RDD that, instead of raw input data, now contains Python lists of each field in that input data.

Finally, I'm going to map that data, take in each list of fields, extract field number three x[3], which I happen to know is the body of the article itself, the actual article text, and I'm in turn going to split that based on spaces:

```
documents = fields.map(lambda x: x[3].split(" ")) 
```

What x[3] does is extract the body of the text from each Wikipedia article, and split it up into a list of words. My new documents RDD has one entry for every document, and every entry in that RDD contains a list of words that appear in that document. Now, we actually know what to call these documents later on when we're evaluating the results.

I'm also going to create a new RDD that stores the document names:

```
documentNames = fields.map(lambda x: x[1]) 
```

All that does is take that same fields RDD and uses this map function to extract the document name, which I happen to know is in field number one.

So, I now have two RDDs, documents, which contains lists of words that appear in each document, and documentNames, which contains the name of each document. I also know that these are in the same order, so I can actually combine these together later on to look up the name for a given document.
