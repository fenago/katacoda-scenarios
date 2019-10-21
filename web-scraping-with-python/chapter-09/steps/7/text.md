Now that we've covered the basics and had an overview of Regex, we will use Regex to scrape (extract) data in bulk in a similar manner to using XPath, CSS selectors, pyquery, bs4, and so on by choosing between the implementation of Regex, XPath, pyquery, and more. This depends on the requirements and feasibility of web access and the availability of the content.

It's not always a requirement that the content should be unstructured to apply Regex and extract data. Regex can be implemented for both structured and unstructured web content that's found in order to extract the desired data. In this section, we'll explore a few examples while using Regex and its various properties.

#### Example 1 – extracting HTML-based content
In this example, we will be using the HTML content from the regexHTML.html file and apply a Regex pattern to extract information such as the following:

- HTML elements
- The element's attributes (key and values)
- The element's content

This example will provide you with a general overview of how we can deal with various elements, values, and so on that exist inside web content and how we can apply Regex to extract that content. The steps we will be applying in the following code will be helpful for processing HTML and similar content:

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter09/regexHTML.html` to view html file.

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/7/1.JPG)

The preceding code is the HTML page source we will be using. The content here is structured, and there are numerous ways that we can deal with it.

In the following code, we will be using functions such as the following:

- read_file(): This will read the HTML file and return the page source for further processing. 
- applyPattern(): This accepts a pattern argument, that is, the Regex pattern for finding content, which is applied to the HTML source using re.findall() and prints information such as a list of searched elements and their counts.
To begin with, let's import re and bs4:

#### Python Code
Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter09/regexHTML.py` to view python code file.

```
import re
from bs4 import BeautifulSoup

def read_file():
   ''' Read and return content from file (.html). '''
    content = open("regexHTML.html", "r")
    pageSource = content.read()
    return pageSource

def applyPattern(pattern):
'''Applies regex pattern provided to Source and prints count and contents'''
    elements = re.findall(pattern, page) #apply pattern to source
    print("Pattern r'{}' ,Found total: {}".format(pattern,len(elements)))
    print(elements) #print all found tags
    return

if __name__ == "__main__":
    page = read_file() #read HTML file 
```
Here, page is an HTML page source that's read from an HTML file using read_file(). We have also imported BeautifulSoup in the preceding code to extract individual HTML tag names and just to compare the implementation of code and results found by using soup.find_all() and a Regex pattern that we will be applying:

```
soup = BeautifulSoup(page, 'lxml')
print([element.name for element in soup.find_all()])
```
