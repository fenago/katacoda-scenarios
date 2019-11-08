So, let's go run that and see what happens. As usual, to run the Spark script, we're not going to just hit the play icon. We have to go to Tools>Canopy Command Prompt. In the Command Prompt that opens up, we will type in spark-submit TF-IDF.py, and off it goes.

#### Run Code
Now, run the python code by running: `python TF-IDF.py`{{execute}}

We are asking it to chunk through quite a bit of data, even though it's a small sample of Wikipedia it's still a fair chunk of information, so it might take a while. Let's see what comes back for the best document match for Gettysburg, what document has the highest TF-IDF score?

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-02/steps/22/2.png)

It's Abraham Lincoln! Isn't that awesome? We just made an actual search engine that actually works, in just a few lines of code.

And there you have it, an actual working search algorithm for a little piece of Wikipedia using Spark in MLlib and TF-IDF. And the beauty is we can actually scale that up to all of Wikipedia if we wanted to, if we had a cluster large enough to run it.

Hopefully we got your interest up there in Spark, and you can see how it can be applied to solve what can be pretty complicated machine learning problems in a distributed manner. So, it's a very important tool, and I want to make sure you don't get through this book on data science without at least knowing the concepts of how Spark can be applied to big data problems. So, when you need to move beyond what one computer can do, remember, Spark is at your disposal.

