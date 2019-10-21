To deal with the preceding condition or reading the content from file, HTTP URL, or FTP, parse() is a really effective approach. It uses the default parser unless specified; one is supplied to it as an extra argument. The following code demonstrates the use of the parse() function, which is being iterated for the element name to obtain its text:

```
from lxml import etree

#read and parse the file
tree = etree.parse("food.xml")

#iterate through 'name' and print text content
for element in tree.iter('name'):
    print(element.text)
```

The preceding code results in the following output: Butter Milk with Vanilla, Fish and Chips, and so on, which are obtained from the name element and from the food.xml file:

```
Butter Milk with Vanilla
Fish and Chips
Egg Roll
Pineapple Cake
Eggs and Bacon
Orange Juice
```

A multiple-tree element can also be iterated, as seen here:

```
for element in tree.iter('name','rating','feedback'):
    print("{} - {}".format(element.tag, element.text))
```

#### Run Code
Now, run the python code by running: `python lxmlParse.py`{{execute}}