`data.take(5)`{{execute}} 

The above line uses the take() function to return first five elements of the RDD. This is an action which triggers the evaluation. The RDD data is now computed by loading it from the file system and then the action is performed. 

Now, let's say we need to count the elements in our RDD. 
`data.count()`{{execute}} 

We are now running a new action, which is causing the RDD to  compute again by loading it from the file system and then the action count is performed. As you can see, we are evaluating the RDD twice. This takes lot of time if the data is very big. To overcome this problem we have cache() and persist() method which can be cache or persist the RDD in memory or on the disk. We will discuss more in the next step. 
