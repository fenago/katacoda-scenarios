In most cases, a document's content is obtained by using requests or urllib and is provided to pyquery as follows:

`from pyquery import PyQuery as pq`{{execute}}

`import requests`{{execute}}

`response = requests.get('http://www.example.com').text #content`{{execute}}

`from urllib.request import urlopen`{{execute}}

`response = urlopen('http://www.example.com').read()`{{execute}}

`docTree = pq(response)`{{execute}}

`print(docTree)`{{execute}}

pyquery can also load URLs using the Python library, urllib (default), or requests. It also supports requests-based parameters:


`pq("https://www.python.org")`{{execute}}


`site=pq("https://www.python.org")`{{execute}}

`print(type(site))`{{execute}}


`pq("https://www.samsclub.com")`{{execute}}

The pq object we obtained from the preceding code is being parsed using the XML parser (default) that's available from lxml, which can also be updated with the extra parser argument being passed to it:

`doc = pq('http://www.google.com', parser = 'html')`{{execute}}

Normally, HTML code from a page source or other sources, such as files, is provided as a string to pyquery for further processing, as shown in the following code:

`doc = pq('<div><p>Testing block</p><p>Second block</p></div>')`{{execute}}

`print(type(doc))`{{execute}}

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/test.html` to view html file.

`pagesource = open('test.html','r').read() #reading locally saved HTML`{{execute}}

`print(type(pagesource))`{{execute}}

`page = pq(pagesource)`{{execute}}

`print(type(page))`{{execute}}

With the PyQuery object or pq that was received from the document or URL that was loaded, we can proceed and explore the features that are available from pyquery.