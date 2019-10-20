This step is used to obtain the desired format from the data. For example, we might require fixed decimal places in the price that`s received, we may need to convert or round up large floating values into fixed decimal places, split large strings into smaller units, and more, and then write them to datasets. There may also be cases where decimal numbers or integers are extracted as strings and need to be formatted. Normally, converting data types and presenting data is considered formatting:

`python`{{execute}}

`price = 1234.567801`{{execute}}

`newprice = round(price,2)`{{execute}}

`print(newprice)`{{execute}}

`totalsum="200.35"`{{execute}}

`print(type(totalsum))`{{execute}}

For large precision use: https://docs.python.org/2/library/decimal.html
`totalsum = float(totalsum)`{{execute}}

`print(type(totalsum))`{{execute}}

`totalsum`{{execute}}

`ratings = 5.5`{{execute}}

`print(int(ratings))`{{execute}}

`quit()`{{execute}}

These additional steps can also be performed within the scripts while we are extracting particular data, and has been done in the examples we`ve looked at throughout the book. In many cases, cleaning and formatting works together, or is done side by side.
