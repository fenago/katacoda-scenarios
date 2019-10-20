In the previous section, we learned about using some important features that are available from pyquery and traversing or identifying elements using those features. In this section, we will be using most of these features from pyquery and we will be using them to scrape data from the web by providing examples with various use cases.

#### Example 1 – scraping data science announcements
In this example, we will be scraping announcements-related details that are found within the data science category from https://developer.ibm.com/announcements/category/data-science/.

The same URL from https://developer.ibm.com/ has also been used to collect data using lxml.cssselect under Example 3, in the Web scraping using LXML section from Chapter 3, Using LXML, XPath, and CSS Selectors. It is suggested that you explore both examples and compare the features that were used.
To begin with, let's import pyquery and requests:

```
from pyquery import PyQuery as pq
import requests
dataSet = list()
```

Create dataSet so that you have an empty list to collect data that we will find from various pages, along with the libraries to be used. We have declared read_url(), which will be used to read the provided URL and return a PyQuery object. In this example, we will be using sourceUrl, that is, https://developer.ibm.com/announcements/:

```
sourceUrl='https://developer.ibm.com/announcements/'

def read_url(url):
 """Read given Url , Returns pyquery object for page content"""
 pageSource = requests.get(url).content
 return pq(pageSource)
```

The information to be collected can be retrieved [from](https://developer.ibm.com/announcements/category/data-science/?fa=date:DESC&fb=) or obtained using sourceUrl+"category/data-science/?fa=date:DESC&fb=". Here, we will be looping through pageUrls.

pageUrls results in the following page URLs. These were obtained by using list comprehension and range():

- https://developer.ibm.com/announcements/category/data-science/page/1?fa=date:DESC&fb=
- https://developer.ibm.com/announcements/category/data-science/page/2?fa=date:DESC&fb=

As shown in the following code, pageUrls generates a list of page-based URLs that can be processed further via the use of the get_details() function. This is used to retrieve articles:

```
if __name__ == '__main__':
    mainUrl = sourceUrl+"category/data-science/?fa=date:DESC&fb="
    pageUrls = [sourceUrl+"category/data-science/page/%(page)s?fa=date:DESC&fb=" % {'page': page} for page in range(1, 3)]

    for pages in pageUrls:
        get_details(pages)

    print("\nTotal articles collected: ", len(dataSet))
    print(dataSet)
```

As we can see from the preceding code, the following URLs were listed:

https://developer.ibm.com/announcements/category/data-science/page/1?fa=date:DESC&fb=

https://developer.ibm.com/announcements/category/data-science/page/2?fa=date:DESC&fb=

The URLs from pageUrls are iterated and passed to get_details() for further processing.