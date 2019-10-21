lxml has a large module set, and, in this section, we will learn to explore lxml using most of its features with examples before moving into scraping tasks. The examples are geared toward extraction activity rather than development.

#### Example 1 – reading XML from file and traversing through its elements
In this example, we will be reading the XML content available from the food.xml file. We will use XML content:

```
from lxml import etree
xml = open("food.xml","rb").read() #open and read XML file
```

The XML response obtained from the preceding code needs to be parsed and traversed using lxml.etree.XML(). The XML() function parses the XML document and returns the menus root node,in this case.

```
tree = etree.XML(xml) 
#tree = etree.fromstring(xml)
#tree = etree.parse(xml)
```

The functions fromstring() and parse() functions, found in the preceding code, also provide content to a default or chosen parser used by lxml.etree.

A number of parsers are provided by lxml (XMLParser and HTMLParser) and the default one used in code can be found using >>> etree.get_default_parser(). In the preceding case, it results in `lxml.etree.XMLParser`.

Let's verify tree received after parsing:

```
print(tree)  
print(type(tree))   
```

The preceding two statements confirm that tree is an XML root element of the lxml.etree._Element type. For traversing through all elements inside a tree, tree iteration can be used, which results in elements in their found order.


Tree iteration is performed using the iter() function. The elements' tag name can be accessed using the element property, tag; similarly, elements' text can be accessed by the text property, as shown in the following:

```
for element in tree.iter():
    print("%s - %s" % (element.tag, element.text))
```

We, too, can pass child elements as an argument to the tree iterator (price and name) to obtain selected element-based responses. After passing the child element to tree.iter(), we can obtain Tag and Text or Content child elements using element.tag and element.text, respectively, as shown in the following code:

```
#iter through selected elements found in Tree
for element in tree.iter('price','name'):
 print("%s - %s" % (element.tag, element.text))
```

#### Run Code
Now, run the python code by running: `python lxmlXMLFile.py`{{execute}}

Also to be noted is that the food.xml file has been opened in rb mode and not in r mode. While dealing with local file-based content and files having encoding declarations, such as `<?xml version="1.0" encoding="UTF-8"?>`, there's a possibility of encountering the error as ValueError: Unicode strings with encoding declaration are not supported. Please use bytes input or XML fragments without declaration. Encoding/decoding the content might solve the issue mentioned, which is also based on the file mode.