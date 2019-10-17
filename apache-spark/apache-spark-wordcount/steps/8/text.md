**Step 2:** At this point, we have each word in a row. In order to count the occurences of each word, we have to map each word to a key-value pair where the key is the word itself and the value will be number 1.

```
val wordskv = words.map(word => (word, 1))
```
 

Here we use a map function to create a key value pair for each word where the key is the word and value is the literal number 1. With this operation we will end up having a tuples of word and the literal number 1.

**Step 3:** Now that we have tuples, all we need to do is add the values (literal number 1) for the same key. To achieve this, we use the reduceByKey function. As the name suggests, the reduceByKey function takes a key and applies operations to the values of that key.

```
val count = wordskv.reduceByKey((x,y) => x + y)
```


The above line of code takes the wordskv RDD and applied reduceByKey function to perform a sum of all the values for a key. This way we will end up with tuple where the first element is the word and the second element is the number of occurences for that word.


The reduceByKey function is similar to reduce function which we have seen in the previous chapter. The difference is that the reduceByKey function performs reduce operation on values for a given key in a tuple while reduce function is applied for all the elements in the collection. 

 
