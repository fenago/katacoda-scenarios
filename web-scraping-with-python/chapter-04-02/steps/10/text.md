In this case, we will be processing XML content with the PyQuery urlXML object, which uses parser='xml':

```
#creating PyQuery object using parser 'xml'
urlXML = pq(xmlFile, parser='xml')

print("Children Length: ",urlXML.children().__len__())
```

As shown in the following code, the first and inner children elements return the required URL content we are willing to extract:

```
print("First Children: ", urlXML.children().eq(0))
print("Inner Child/First Children: ", urlXML.children().children().eq(0))
```


```
First Children: 
<url xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
<loc>https://webscraping.com</loc>
</url>

Inner Child/First Children: 
<loc xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">https://webscraping.com</loc>
```

The remove_namespace() function can be used on a PyQuery object and processed for its final output, as shown in the following code:

```
for url in urlXML.remove_namespaces().children().find('loc:contains("blog")').items():
    dataSet.append(url.text())

print("Length of dataSet: ", len(dataSet))
print(dataSet)
```

The PyQuery remove_namespace() and xhtml_to_html() methods remove the namespaces from XML and XHTML, respectively. Use of these two methods allows us to work with elements that use HTML-related properties.
We can also process the same content with a different approach; that is, by using a regular expression and obtaining the output as required. Let's proceed with the following code:

```
print("URLs using Children: ",urlXML.children().text()) 
#print("URLs using Children: ",urlXML.children().children().text()) 
#print("URLs using Children: ",urlXML.text())
```

The PyQuery children() object method returns all the child nodes, and text() will extract the text content:

As shown in the preceding output, all the links from the child nodes are returned as a single string:

```
blogXML = re.split(r'\s',urlXML .children().text())
print("Length of blogXML: ",len(blogXML))

#filter(), filters URLs from blogXML that matches string 'blog'
dataSet= list(filter(lambda blogXML:re.findall(r'blog',blogXML),blogXML))
print("Length of dataSet: ",len(dataSet))
print("Blog Urls: ",dataSet)
```

Here, re.split() is used to split the string of URLs received with the space character, \s. This returns a total of 139 elements. Finally, blogXML is filtered using re.findall(), which finds the blog string in the blogXML elements and results in the following:

In this section, we have used a few scraping techniques to extract the desired content from files and websites. Content identification and the requirement to scrape is pretty dynamic and is also based on the structure of the website. With libraries such as pyquery, we can obtain and deploy the necessary tools and techniques for scraping in an effective and efficient manner.


Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/xml-parser.py` to view python code file.

#### Run Code
Now, run the python code by running: `python xml-parser.py`{{execute}}