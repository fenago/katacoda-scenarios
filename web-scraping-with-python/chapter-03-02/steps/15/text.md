Let's deploy the preceding concept using Python code, as shown in the following snippet:

```
from lxml import html
import requests
from lxml.cssselect import CSSSelector
url = 'https://developer.ibm.com/announcements/category/data-science/?fa=date%3ADESC&fb='
url_get = requests.get(url)
tree = html.document_fromstring(url_get.content)
```

The required Python library and URLs are declared and the page content url_get is parsed with lxml.html. With lxml.html.HTMLElement obtained, we can now select and navigate to the desired element in the tree with the XPath or CSS selector:

```
announcements=[]
articles = tree.cssselect('.ibm--card > a.ibm--card__block_link')

for article in articles:
    link = article.get('href')
    atype = article.cssselect('div.ibm--card__body > h5')[0].text.strip()
    adate = article.cssselect('div.ibm--card__body > h5 > .ibm--card__date')[0].text
    title = article.cssselect('div.ibm--card__body > h3.ibm--card__title')[0].text_content()
    excerpt= article.cssselect(' div.ibm--card__body > p.ibm--card__excerpt')[0].text
    category= article.cssselect('div.ibm--card__bottom > p.cpt-byline__categories span')
    
    #only two available on block: except '+'
    #announcements.append([link,atype,adate,title,excerpt,[category[0].text,category[1].text]])
    
    announcements.append([link,atype,adate,title,excerpt,[span.text for span in category if     span.text!='+']])

print(announcements)
```

**articles** is a defined main CSS query and is looped for all available articles found in the page as article. Each article has different elements for type, date, title, category, and so on. Element data or attributes are collected using text, text_content(), and get(). cssselect returns the Python list objects, hence, indexing, such as [0], is used to collect particular element content.

**category** in the preceding code doesn't have any indexing, as it contains a multiple `<span>` element whose value is being extracted using a list comprehension technique, while appending or using indexing as shown in the comments. Output obtained for the code is shown in the following screenshot. Minor cleaning of data has been attempted, but the final list still contains the obtained raw data:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/15/1.JPG)

#### Run Code
Now, run the python code by running: `python scrapelxmlcss.py`{{execute}}
