The Python bs4 library contains a BeautifulSoup class, which is used for parsing. On successful installation of the library, we can obtain the details as shown in the following screenshot, using Python IDE:

`pip install bs4 lxml requests`{{execute}} 

Also, the collection of simple (named) and explainable methods available as seen in the preceding screenshot and encoding support makes it more popular among developers. 

Let's import BeautifulSoup and SoupStrainer from bs4, as seen in the following code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-01/steps/4/1.png)

`python`{{execute}}

```from bs4 import BeautifulSoup
from bs4 import SoupStrainer #,BeautifulSoup```{{execute}}

We will be using the HTML as shown in the following snippet or html_doc as a sample to explore some of the fundamental features of Beautiful Soup. The response obtained for any chosen URL, using requests or urllib, can also be used for content in real scraping cases:

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter05/test.py` and copy and paste code in the python IDE.

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-01/steps/4/2.JPG)

To proceed with parsing and accessing Beautiful Soup methods and properties, a Beautiful Soup object, generally known as a soup object, must be created. Regarding the type of string or markup content provided in the constructor, a few examples of creating Beautiful Soup objects, along with the parameters mentioned earlier, are listed next:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-01/steps/4/3.JPG)

For this particular case, we will be creating the soupA object using lxml as a parser, along with the SoupStrainer object tagsA (parsing only `<a>`, that is, the elements or anchor tag of HTML). We can obtain partial content to parse using SoupStrainer, which is very useful when dealing with heavy content. 

soupA, an object of Beautiful Soup, presents all of the `<a>` elements found for the SoupStrainer object tagsA as used in the following code; as seen in the output, only the `<a>` tag has been collected, or the parsed document is the SoupStrainer object parsed using lxml:


`tagsA = SoupStrainer("a")`{{execute}} 

`soupA = BeautifulSoup(html_doc,'lxml',parse_only=tagsA)`{{execute}} 

`print(type(soupA))`{{execute}} 


`print(soupA)`{{execute}} 

HTML content, available from the website, might not always be formatted in a clean string. It would be difficult and time-consuming to read page content that is presented as paragraphs rather than as a line-by-line code.

The Beautiful Soup prettify() function returns a Unicode string, presents the string in a clean, formatted structure that is easy to read, and identifies the elements in a tree structure as seen in the following code; the prettify() function also accepts the parameter encoding:

`print(soupA.prettify())`{{execute}} 

Document-based elements (such as HTML tags) in a parsed tree can have various attributes with predefined values. Element attributes are important resources as they provide identification and content together within the element. Verifying whether the element contains certain attributes can be handy when traversing through the tree.

For example, as seen in the following code, the HTML `<a>` element contains the class, href, and id attributes, each carrying predefined values, as seen in the following snippet:

`<a class="sister" href="http://example.com/lacie" id="link2">`

The has_attr() function from Beautiful Soup returns a Boolean response to the searched attribute name for the chosen element, as seen in the following code element a:

- Returns False for the name attribute
- Returns True for the class attribute

We can use the has_attr() function to confirm the attribute keys by name, if it exists inside the parsed document as follows:

`print(soupA.a.has_attr('class'))`{{execute}} 

`print(soupA.a.has_attr('name'))`{{execute}} 

With a basic introduction to Beautiful Soup and a few methods explored in this section, we will now move forward for searching, traversing, and iterating through the parsed tree looking for elements and their content in the upcoming section. 