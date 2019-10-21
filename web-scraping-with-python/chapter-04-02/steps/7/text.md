In this example, we will be extracting data from American Hockey League (AHL) Playoff results, which are available from http://www.flyershistory.com/cgi-bin/ml-poffs.cgi:


The preceding URL contains the Playoff results for the AHL. This page presents information about the results in tabular format. The portion of the page source that shows relevant information is shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-04-02/steps/7/1.png)

With the source format analyzed, it's also necessary to point out that <td> containing the desired values has no attributes that can be used to identify particular table cells. In this case, we can target the position of <td> or cell with data by using CSS selectors, that is, pseudo selectors such as td:eq(0) or td:eq(1).

For more information on CSS selectors, please visit Chapter 3, Using LXML, XPath, and CSS Selectors, the Introduction to XPath and CSS selector section, in the CSS Selectors and Pseudo Selectors sub-section.
Since we will be using pyquery for this example, we will use the eq() method, which accepts the index and returns the element. For example, we could use tr.find('td').eq(1).text() for the chosen PyQuery object, tr, search for the element td, that is, <td>, with the index equal to 1, and return the text of the element.

Here, we are interested in collecting data for the columns that are listed in keys:

```
keys = ['year','month','day','game_date','team1', 'team1_score', 'team2', 'team2_score', 'game_status']
```

Now, let's import the code with pyquery and re. Regex will be used to separate the date that was obtained from the page source:

```
from pyquery import PyQuery as pq
import re

sourceUrl = 'http://www.flyershistory.com/cgi-bin/ml-poffs.cgi'
dataSet = list()
keys = ['year','month','day','game_date','team1', 'team1_score', 'team2', 'team2_score', 'game_status']

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = pq(url)
    return pq(pageSource)

if __name__ == '__main__':
    page = read_url(sourceUrl)       
``` 

Here, read_url() accepts one argument, that is, the link to the page, and returns the PyQuery object of the page source or pageSource. PyQuery automatically returns the page source for the provided URL. The page source can also be obtained by using other libraries, such as urllib, urllib3, requests, and LXML, and passed to create a PyQuery object:

```
tableRows = page.find("h1:contains('AHL Playoff Results') + table tr")
print("\nTotal rows found :", tableRows.__len__())
```

**tableRows** is a PyQuery object that will be used to traverse `<tr>` that exists inside `<table>`, which is located after `<h1>`. It contains the AHL Playoff Results text, which is obtained by using the find() function. As we can see in the following output, a total of 463 `<tr>` elements exist, but the actual number of records that were obtained might be lower, in terms of the number of available `<td>` with the actual data: