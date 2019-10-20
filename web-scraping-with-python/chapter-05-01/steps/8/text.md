In this section, we will build a web crawler to demonstrate the real content-based scraping, targeting web content.

We will be scraping quotes from http://toscrape.com/ and targeting quotes from authors found at http://quotes.toscrape.com/. The crawler will collect the quote and author information from the first five listing pages and write the data into a CSV file. We will also explore the individual author page and extract information about the authors. 



```
import requests
import re
from bs4 import BeautifulSoup
import csv

sourceUrl = 'http://quotes.toscrape.com/'
keys = ['quote_tags','author_url','author_name','born_date','born_location','quote_title']
```

In the preceding code there are a few libraries and objects found as listed and described here:

sourceUrl: Represents the URL of the main page to be scraped for data for category web scraping
keys: The Python list contains the columns name that will be used while writing records to an external file
requests: This library is imported to use for making an HTTP request to page URLs with quote listings and receiving a response
csv: This library will be used to write scraped data to an external CSV file
bs4: Library for implementing and using Beautiful Soup
The first line in a CSV file contains column names. We need to write these columns before appending records with real content in the CSV file.
The read_url() function, as found in the following code, will be used to make a request and receive a response using the requests function. This function will accept a url argument for pages:

```
def read_url(url):
    """Read given Url, Returns requests object for page content"""
    response = requests.get(url)
    return response.text
```

dataSet is a handle defined to manage the external file quotes.csv. csv.writer() file handle is use for accessing CSV-based properties. The writerow() function is passed with keys for writing a row containing the column names from the list keys to the external file as shown in the following:

```
if __name__ == '__main__':
    dataSet = open('quotes.csv', 'w', newline='', encoding='utf-8')
    dataWriter = csv.writer(dataSet)

    # Write a Header or Column_names to CSV
    dataWriter.writerow(keys)

    #load details for provided URL
    get_details(sourceUrl, dataWriter)
    dataSet.close()
```
