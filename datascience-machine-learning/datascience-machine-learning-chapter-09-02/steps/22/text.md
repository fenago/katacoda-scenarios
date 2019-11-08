Let's try and put the algorithm to use. Let's try to look up the best article for the word Gettysburg. If you're not familiar with US history, that's where Abraham Lincoln gave a famous speech. So, we can transform the word Gettysburg into its hash value using the following code:

```
gettysburgTF = hashingTF.transform(["Gettysburg"]) 
gettysburgHashValue = int(gettysburgTF.indices[0]) 
```

We will then extract the TF-IDF score for that hash value into a new RDD for each document:

```
gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue])  
```

What this does is extract the TF-IDF score for Gettysburg, from the hash value it maps to for every document, and stores that in this gettysburgRelevance RDD.

We then combine that with the documentNames so we can see the results:

```
zippedResults = gettysburgRelevance.zip(documentNames)  
```

Finally, we can print out the answer:

```
print ("Best document for Gettysburg is:") 
print (zippedResults.max()) 
```
