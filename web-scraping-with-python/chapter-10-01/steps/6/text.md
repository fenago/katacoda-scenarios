Now, with the available finalDataSet, we can dump or add the data to a JSON file using the dump() function from the json module:

<pre class="file" data-filename="save.py">

with open('bookdetails.json', 'w') as jsonfile:
    json.dump(finalDataSet,jsonfile)
</pre>

#### Run Code
Now, run the python code by running: `python save.py`{{execute}}

`cat bookdetails.json`{{execute}}

The preceding code will result in the bookdetails.json file. Its content is as follows:

```
[
  {
    "Price": 35.02,
    "Stock": "In stock",
    "Title": "Rip it Up and ...",
    "Rating": 5
  },
  ................
  {
    "Price": 28.8,
    "Stock": "In stock",
    "Title": "Forever Rockers (The Rocker ...",
    "Rating": 3
  }
]
```

In this section, we have covered the basic steps for managing raw data. The files we have obtained can be shared and exchanged easily across various independent systems, used as models for ML, and can be imported as data sources in applications. Furthermore, we can also use Database Management Systems (DBMS) such as MySQL, PostgreSQL, and more to store data and execute Structured Query Language (SQL) using the necessary Python libraries.