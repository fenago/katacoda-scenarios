

Let's consider the following example, which contains colNames with the column to be used, and dataSet with the cleaned and formatted data:

<pre class="file" data-filename="save.py" data-target="replace">
import csv
import json

colNames = ['Title','Price','Stock','Rating']
dataSet= [['Rip it Up and ...', 35.02, 'In stock', 5],['Our Band Could Be ...', 57.25, 'In stock', 4],
    ['How Music Works', 37.32, 'In stock', 2],['Love Is a Mix ...', 18.03, 'Out of stock',1],
    ['Please Kill Me: The ...', 31.19, 'In stock', 4],["Kill 'Em and Leave: ...", 45.0, 'In stock',5],
    ['Chronicles, Vol. 1', 52.60, 'Out of stock',2],['This Is Your Brain ...', 38.4, 'In stock',1],
    ['Orchestra of Exiles: The ...', 12.36, 'In stock',3],['No One Here Gets ...', 20.02, 'In stock',5],
   ['Life', 31.58, 'In stock',5],['Old Records Never Die: ...', 55.66, 'Out of Stock',2],
    ['Forever Rockers (The Rocker ...', 28.80, 'In stock',3]]
</pre>

Now we will write the preceding dataSet to the CSV file. The first line of the CSV file should always contain the column names. In this case, we will use colNames for the columns:

<pre class="file" data-filename="save.py">

fileCsv = open('bookdetails.csv', 'w')
writer = csv.writer(fileCsv) #csv.writer object created

writer.writerow(colNames)  #write columns from colNames
for data in dataSet:       #iterate through dataSet and write to file
    writer.writerow(data)

fileCsv.close() #closes the file handler
</pre>

The preceding code will result in the bookdetails.csv file, which has the following content:

```
Title,Price,Stock,Rating
Rip it Up and ...,35.02,In stock,5
Our Band Could Be ...,57.25,In stock,4
...........
Life,31.58,In stock,5
Old Records Never Die: ...,55.66,Out of Stock,2
Forever Rockers (The Rocker ...,28.8,In stock,3
```

Similarly, let's create a JSON file with colNames and dataSets. JSON is similar to Python dictionary, where each data or value possesses a key; that is, it exists in a key-value pair:

<pre class="file" data-filename="save.py">
finalDataSet=list() #empty DataSet

for data in dataSet:
    finalDataSet.append(dict(zip(colNames,data))) 

print(finalDataSet)
</pre>


#### Run Code
Now, run the python code by running: `python save.py`{{execute}}

`cat bookdetails.csv`{{execute}}


```
[{'Price': 35.02, 'Stock': 'In stock', 'Title': 'Rip it Up and ...', 'Rating': 5}, {'Price': 57.25, 'Stock': 'In stock', ..........'Title': 'Old Records Never Die: ...', 'Rating': 2}, {'Price': 28.8, 'Stock': 'In stock', 'Title': 'Forever Rockers (The Rocker ...', 'Rating': 3}]
```

As we can see, finalDataSet is formed by appending data from dataSet and by using the zip() Python function. zip() combines each individual element from the list. This zipped object is then converted into a Python dictionary. For example, consider the following code:

```
#first iteration from loop above dict(zip(colNames,data)) will generate
{'Rating': 5, 'Title': 'Rip it Up and ...', 'Price': 35.02, 'Stock': 'In stock'}
```

