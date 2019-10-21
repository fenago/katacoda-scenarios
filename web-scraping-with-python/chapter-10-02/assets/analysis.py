# %%
'''
In this section, we will be reading data from the bookdetails.csv file and conducting analysis and visualization using the file's data. Let's import the libraries that are required, that is, pandas and matplotlib.pyplot. We will be using the  pd and plt aliases, respectively, and reading the data from the file:
'''

# %%
import pandas as pd
%matplotlib notebook
import matplotlib.pyplot as plt

dataSet = pd.read_csv('bookdetails.csv') #loads the file content as dataframe.

print(type(dataSet)) #<class 'pandas.core.frame.DataFrame'>

# %%
'''
As we can see, the read_csv() function reads the content from a CSV file and generates a DataFrame object. pandas also supports various data files via the use of functions such as read_html(), read_excel(), read_json(), and read_sql_table().

Here, dataSet is an object of the pandas DataFrame. The DataFrame represents a two-dimensional tabular structure with rows, columns, and indexes. Query-level analysis, conditional statements, filtering, grouping, and more are supported by DataFrames against data in rows and columns:
'''

# %%
print(dataSet)


# %%
'''
Dataset contents from a CSV file
Row indexes are also shown, all of which start with 0 (zero). The general statistical output can be obtained by using the describe() function:
'''

# %%
print(dataSet.describe()) 
#print(dataSet.describe('price') will only generate values for column price
  
# %%
'''
As we can see, by default, describe() selects the columns that are applicable to statistical functions and returns calculations with the following functions:

- count: Number of rows

- mean: Average value for the related column

- min: Minimum value found

- max: Maximum value found

- std: Calculated standard deviation

- 25%: Returns the 25th percentile

- 50%: Returns the 50th percentile

- 75%: Returns the 75th percentile

In the following code, we are selecting an individual column called Price as price_group. All of the columns from the dataset can be listed using dataSet.columns. Multiple columns can be selected by using the following dataSet[['Price','Rating']] format:
'''

# %%
print(dataSet.columns)

print(sum(dataSet['Price']))

print(sum(dataSet['Rating']))
print(dataSet['Price'][0:5])

# %%
'''
The following code shows the individual data for the Price column:
'''

# %%
#dataSet[['Price','Rating']] will select both column
price_group = dataSet[['Price']] #selecting 'Price' column only.
print(price_group) 


# %%
'''
pandas DataFrames also accept conditions or filtering actions being used on columns. As you can see, the filter is applied to Rating for values that are >=4.0, and only Title and Price are going to be returned:
'''

# %%
print(dataSet[dataSet['Rating']>=4.0][['Title','Price']])

# %%
'''
Similarly, string-based filters can also be applied. Stock, which contains the Out text, is filtered, and the output returns all the columns that satisfy the Out text. The contains() function accepts regular expressions and strings:
'''

# %%
print(dataSet[dataSet.Stock.str.contains(r'Out')])


# %%
print(dataSet[dataSet.Rating.between(3.5,4.5)]['Title'])

# %%
'''
Since we have the price_group data, we can call the plot() function on the data with the help of the show() function:
'''

# %%
bar_plot = price_group.plot()  #default plot
bar_plot.set_xlabel("No of Books") #set X axis: label
bar_plot.set_ylabel("Price") #set Y axis: label
plt.show() #displays the plot or chart created

# %%
'''
We can also change the kind of chart, that is, line, bar, and more.

In the following code, kind='bar' overwrites the default line type:
'''

# %%
bar_plot = price_group.plot(kind='bar') #kind='bar'
bar_plot.set_xlabel("No of Books")  #Label for X-Axis
bar_plot.set_ylabel("Price") #label for Y-Axis
plt.show() 

# %%
'''
So far, we have used a basic chart type with a single column. In the following code, we are plotting a bar chart with the Price and Rating values:
'''

# %%
price_group = dataSet[['Price','Rating']]  #obtain both columns
#title: generates a title for plot
bar_plot = price_group.plot(kind='bar',title="Book Price ad Rating")
bar_plot.set_xlabel("No of Books")
bar_plot.set_ylabel("Price")
plt.show()

# %%
'''
Bar chart with Price and Rating columns

So far, we have successfully plotted line and bar charts. The following code plots a pie chart for the first six items from the Price column and labels them with the first six Title available from dataSet:
'''

# %%
prices = dataSet['Price'][0:6] #Price from first 6 items
labels = dataSet['Title'][0:6] #Book Titles from first 6 items
legends,ax1 = plt.pie(prices, labels=labels, shadow=True, startangle=45)
plt.legend(legends, prices, loc="best")
plt.show() 

# %%
'''
The values from Price are used as legends. In this section, we have displayed the basic features that are available from both libraries.
'''
