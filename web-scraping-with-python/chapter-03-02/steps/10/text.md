**Example – reading and parsing HTML for retrieving HTML form type element attributes**

In this example, we will be reading HTML from the http://httpbin.org/forms/post URL, which contains HTML-based form elements. Form elements have various predefined attributes such as type, value, and name and can exist with manual attributes. In the preceding examples, we tried to implement various functions—XPath and CSSSelect—to retrieve content from the desired element.

Here, we will try to collect the attributes and their values found in HTML-form elements:

```
from lxml import html
import requests
response = requests.get('http://httpbin.org/forms/post')

# build the DOM Tree
tree = html.fromstring(response.text)

for element in tree.iter('input'):
     print("Element: %s \n\tvalues(): %s \n\tattrib: %s \n\titems(): %s \n\tkeys(): %s"%
     (element.tag, element.values(),element.attrib,element.items(),element.keys()))
     print("\n")
```

In the preceding code, the response.text and a str type object is obtained for the given URL. The fromstring() function parses the provided string object and returns the root node or the HTMLElement tree type.

In this example, we are iterating the input element or <input...> and are looking to identify the attributes each input possesses.


#### Run Code
Now, run the python code by running: `python etreeFromString.py`{{execute}}

The preceding code results in the output shown here:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/10/1.JPG)

There are a number of functions and properties used with the <input> element in the code resulting from the output. Listed in the following in some of the code used in the example with an explanation:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/10/2.JPG)
