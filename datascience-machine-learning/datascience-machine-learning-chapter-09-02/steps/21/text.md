Now, the magic happens. The first thing we're going to do is create a HashingTF object, and we're going to pass in a parameter of 100,000. This means that I'm going to hash every word into one of 100,000 numerical values:

```
hashingTF = HashingTF(100000)  
```

Instead of representing words internally as strings, which is very inefficient, it's going to try to, as evenly as possible, distribute each word to a unique hash value. I'm giving it up to 100,000 hash values to choose from. Basically, this is mapping words to numbers at the end of the day.

Next, I'm going to call transform on hashingTF with my actual RDD of documents:

```
tf = hashingTF.transform(documents) 
```

That's going to take my list of words in every document and convert it to a list of hash values, a list of numbers that represent each word instead.

This is actually represented as a sparse vector at this point to save even more space. So, not only have we converted all of our words to numbers, but we've also stripped out any missing data. In the event that a word does not appear in a document where you're not storing the fact that word does not appear explicitly, it saves even more space.

#### Computing the TF-IDF score
To actually compute the TF-IDF score for each word in each document, we first cache this tf RDD.

```
tf.cache() 
```

We do that because we're going to use it more than once. Next, we use IDF(minDocFreq=2), meaning that we're going to ignore any word that doesn't appear at least twice:

```
idf = IDF(minDocFreq=2).fit(tf) 
```

We call fit on tf, and then in the next line we call transform on tf:

```
tfidf = idf.transform(tf) 
```

What we end up with here is an RDD of the TF-IDF score for each word in each document.
