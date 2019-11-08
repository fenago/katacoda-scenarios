There are more ways to create RDDs as well. You can create them from a JDBC connection. Basically any database that supports JDBC can also talk to Spark and have RDDs created from it. Cassandra, HBase, Elasticsearch, also files in JSON format, CSV format, sequence files object files, and a bunch of other compressed files like ORC can be used to create RDDs. I don't want to get into the details of all those, you can get a book and look those up if you need to, but the point is that it's very easy to create an RDD from data, wherever it might be, whether it's on a local filesystem or a distributed data store.

Again, RDD is just a way of loading and maintaining very large amounts of data and keeping track of it all at once. But, conceptually within your script, an RDD is just an object that contains a bunch of data. You don't have to think about the scale, because Spark does that for you.

#### RDD operations
Now, there are two different types of classes of things you can do on RDDs once you have them, you can do transformations, and you can do actions.

#### Transformations
Let's talk about transformations first. Transformations are exactly what they sound like. It's a way of taking an RDD and transforming every row in that RDD to a new value, based on a function you provide. Let's look at some of those functions:

- **map() and flatmap():** map and flatmap are the functions you'll see the most often. Both of these will take any function that you can dream up, that will take, as input, a row of an RDD, and it will output a transformed row. For example, you might take raw input from a CSV file, and your map operation might take that input and break it up into individual fields based on the comma delimiter, and return back a Python list that has that data in a more structured format that you can perform further processing on. You can chain map operations together, so the output of one map might end up creating a new RDD that you then do another transformation on, and so on, and so forth. Again, the key is, Spark can distribute those transformations across the cluster, so it might take part of your RDD and transform it on one machine, and another part of your RDD and transform it on another.

Like I said, map and flatmap are the most common transformations you'll see. The only difference is that map will only allow you to output one value for every row, whereas flatmap will let you actually output multiple new rows for a given row. So you can actually create a larger RDD or a smaller RDD than you started with using flatmap.

- **filter():** filter can be used if what you want to do is just create a Boolean function that says "should this row be preserved or not? Yes or no."
- **distinct():** distinct is a less commonly used transformation that will only return back distinct values within your RDD.
- **sample():** This function lets you take a random sample from your RDD
union(), intersection(), subtract() and Cartesian(): You can perform intersection operations like union, intersection, subtract, or even produce every cartesian combination that exists within an RDD.
