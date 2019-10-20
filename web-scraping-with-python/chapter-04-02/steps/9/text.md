In this example, we will be extracting URLs that have been found for blogs in the sitemap.xml file from [here](https://webscraping.com/sitemap.xml)

In the preceding examples, we used HTML content, but PyQuery can also be used to traverse XML file content. By default, pyquery uses an LXML-based xml parser, which can be provided while creating a PyQuery object. We will be using both lxml.html and xml in the file's content.

For more information on pyquery and parser, please visit the Exploring pyquery section of this chapter. For information regarding the site map, please visit Chapter 1, Web Scraping Fundamentals, the Data finding techniques (seeking data from the web) section, in the Sitemaps subsection.
The following screenshot shows the content that's available in the sitemap.xml file:



To begin with, let's import pyquery and read the file's content as xmlFile:

```
from pyquery import PyQuery as pq

if __name__ == '__main__':
    # reading file
    xmlFile = open('sitemap.xml', 'r').read()   
```

#### Case 1 – using the HTML parser
Here, we will be using the lxml.html parser to parse xmlFile by passing an argument parser, parser='html', to PyQuery:

```
# creating PyQuery object using parser 'html'
 urlHTML = pq(xmlFile, parser='html')

print("Children Length: ",urlHTML.children().__len__())
print("First Children: ",urlHTML.children().eq(0))
print("Inner Child/First Children: ",urlHTML.children().children().eq(0))
```

Using PyQuery's urlHTML object allows us to check the count and the child elements that were obtained from the data, as shown in the following output:

```
Children Length: 137

First Children: 
<url>
<loc>https://webscraping.com</loc>
</url>

Inner Child/First Children: <loc>https://webscraping.com</loc>
```

As we can see, urlHTML.children() contains the required elements to look for the URL. We can process this data with the items() method, which traverses through each element that's obtained. Let's create dataSet (Python list()) that will be appended with the URLs that are extracted.

Element-based iteration can be performed with urlHTML.children().find('loc:contains("blog")').items() by using a selector that contains the blog string:

```
dataSet=list()
for url in urlHTML.children().find('loc:contains("blog")').items():
    dataSet.append(url.text())

print("Length of dataSet: ", len(dataSet))
print(dataSet)
```

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/html-parser.py` to view python code file.

#### Run Code
Now, run the python code by running: `python html-parser.py`{{execute}}
