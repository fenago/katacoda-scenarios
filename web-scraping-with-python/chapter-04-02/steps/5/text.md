In this example, we will be scraping details for quotes found in books from http://quotes.toscrape.com/tag/books/. Each individual quote contains certain information, plus a link to the author's detail page, which will also be processed so that we can obtain information regarding the author:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-04-02/steps/5/1.png)


Main page from http://quotes.toscrape.com/tag/books/
In the following code, the elements in keys will be used as keys for output and will contain the Python dictionary. Basically, we will be collecting data for elements in keys:

```
from pyquery import PyQuery as pq
sourceUrl = 'http://quotes.toscrape.com/tag/books/'
dataSet = list()
keys = ['quote_tags','author_url','author_name','born_date','born_location','quote_title']

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = pq(url)
    return pq(pageSource)
```

read_url() from the preceding code is also updated and is different in comparison to the libraries we used in the Example 1 – scraping data science announcements section. In this example, it returns the PyQuery object for the provided URL:

```
if __name__ == '__main__':
    get_details(sourceUrl)

    print("\nTotal Quotes collected: ", len(dataSet))
    print(dataSet)

    for info in dataSet:
        print(info['author_name'],' born on ',info['born_date'], ' in ',info['born_location'])
```

There is an additional iteration being done with dataSet for certain values from the info dictionary, which is found inside dataSet.
