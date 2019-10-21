From Task 1, we were able to load the URL and retrieve its content. Saving the content to local files using libraries methods and using file handling concepts will be implemented in this task. Saving content to local files and working on content with tasks like parsing and traversing can be really quick and even reduce network resources:

Load and save the content [from](https://www.samsclub.com/robots.txt) using urllib:

`import urllib.request `{{execute}}

`urllib.request.urlretrieve('https://www.samsclub.com/robots.txt')`{{execute}}

`urllib.request.urlretrieve(link,"testrobots.txt") #urlretrieve(url, filename=None)`{{execute}}

```
('testrobots.txt', <http.client.HTTPMessage object at 0x04322DF0>)
```

The urlretrieve() function, that is, urlretrieve(url, filename=None, reporthook=None, data=None), from urllib.request returns a tuple with the filename and HTTP headers. You can find this file in the C:\\Users..Temp directory if no path is given; otherwise, the file will be generated in the current working directory with the name provided to the urlretrieve() method as the second argument. This was testrobots.txt in the preceding code:


```import urllib.request
import os
content = urllib.request.urlopen('https://www.samsclub.com/robots.txt').read() #reads robots.txt content from provided URL```{{execute}}

```file = open(os.getcwd()+os.sep+os.sep+"robots.txt","wb")```{{execute}}

`file.write(content)`{{execute}}

`file.close() #closes the file handle`{{execute}}

In the preceding code, we are reading the URL and writing the content found using a file handling concept. 

Load and save the content from https://www.samsclub.com/sitemap.xml using requests:

`link="https://www.samsclub.com/sitemap.xml"`{{execute}} 

`import requests`{{execute}} 

`content = requests.get(link).content`{{execute}} 

`content`{{execute}} 

```
b'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<sitemap><loc>https://www.samsclub.com/sitemap_categories.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_1.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_2.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_locators.xml</loc></sitemap>\n</sitemapindex>'
```

`file = open(os.getcwd()+os.sep+os.sep+"sitemap.xml","wb")`{{execute}} 

`file.write(content)`{{execute}} 

`file.close() #closes the file handle`{{execute}} 

`quit`{{execute}}

In both cases, we were able to find the content from the respective URL and save it to individual files and locations. The contents from the preceding code was found as bytes literals, for example, `b'<!DOCTYPE … or b'<?xml`. Page content can also be retrieved in a text format, such as `requests.get(link).text`{{execute}} 

#### Verify Files
You can verify that azure files were created successfully by running:

`ls`{{execute}}

`cat robots.txt`{{execute}}

`cat sitemap.xml`{{execute}}