
Next, dataFrameFromDirectory() is a function I wrote, which basically says I have a path to a directory, and I know it's given classification, spam or ham, then it uses the readFiles() function, that I also wrote, which will iterate through every single file in a directory. So readFiles() is using the os.walk() function to find all the files in a directory. Then it builds up the full pathname for each individual file in that directory, and then it reads it in. And while it's reading it in, it actually skips the header for each e-mail and just goes straight to the text, and it does that by looking for the first blank line.

It knows that everything after the first empty line is actually the message body, and everything in front of that first empty line is just a bunch of header information that I don't actually want to train my spam classifier on. So it gives me back both, the full path to each file and the body of the message. So that's how we read in all of the data, and that's the majority of the code!

So what I have at the end of the day is a DataFrame object, basically a database with two columns, that contains message bodies, and whether it's spam or not. We can go ahead and run that, and we can use the head command from the DataFrame to actually preview what this looks like:

```
data.head() 
```

The first few entries in our DataFrame look like this: for each path to a given file full of e-mails we have a classification and we have the message body:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/18/1.jpg)

Alright, now for the fun part, we're going to use the MultinomialNB() function from scikit-learn to actually perform Naive Bayes on the data that we have.

```
vectorizer = CountVectorizer() 
counts = vectorizer.fit_transform(data['message'].values) 
 
classifier = MultinomialNB() 
targets = data['class'].values 
classifier.fit(counts, targets) 
```

This is what your output should now look like:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/18/2.jpg)

Once we build a MultinomialNB classifier, it needs two inputs. It needs the actual data that we're training on (counts), and the targets for each thing (targets). So counts is basically a list of all the words in each e-mail and the number of times that word occurs.

So this is what CountVectorizer() does: it takes the message column from the DataFrame and takes all the values from it. I'm going to call vectorizer.fit_transform which basically tokenizes or converts all the individual words seen in my data into numbers, into values. It then counts up how many times each word occurs.

This is a more compact way of representing how many times each word occurs in an e-mail. Instead of actually preserving the words themselves, I'm representing those words as different values in a sparse matrix, which is basically saying that I'm treating each word as a number, as a numerical index, into an array. What that does is, just in plain English, it split each message up into a list of words that are in it, and counts how many times each word occurs. So we're calling that counts. It's basically that information of how many times each word occurs in each individual message. Mean while targets is the actual classification data for each e-mail that I've encountered. So I can call classifier.fit() using my MultinomialNB() function to actually create a model using Naive Bayes, which will predict whether new e-mails are spam or not based on the information we've given it.

Let's go ahead and run that. It runs pretty quickly! I'm going to use a couple of examples here. Let's try a message body that just says Free Money now!!! which is pretty clearly spam, and a more innocent message that just says "Hi Bob, how about a game of golf tomorrow?" So we're going to pass these in.

```
examples = ['Free Money now!!!', "Hi Bob, how about a game of golf tomorrow?"] 
example_counts = vectorizer.transform(examples) 
predictions = classifier.predict(example_counts) 
predictions 
```

The first thing we do is convert the messages into the same format that I trained my model on. So I use that same vectorizer that I created when creating the model to convert each message into a list of words and their frequencies, where the words are represented by positions in an array. Then once I've done that transformation, I can actually use the predict() function on my classifier, on that array of examples that have transformed into lists of words, and see what we come up with:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-05-01/steps/18/3.jpg)

```
array(['spam', 'ham'], dtype='|S4') 
```

And sure enough, it works! So, given this array of two input messages, Free Money now!!! and Hi Bob, it's telling me that the first result came back as spam and the second result came back as ham, which is what I would expect. That's pretty cool. So there you have it.

