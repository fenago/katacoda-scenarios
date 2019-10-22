Now that we have tested the preceding XML with various XPath expressions, let's consider a simple XML with some attributes. Attributes are extra properties that identify certain parameters for a given node or element. A single element can contain a unique attributes set. Attributes found in XML nodes or HTML elements help to identify the unique element with the value it contains. As we can see in the code in the following XML, attributes are found as a key=value pair of information, for example id="1491946008":

```
<?xml version="1.0" encoding="UTF-8"?>
<books>
     <book id="1491946008" price='47.49'>
        <author>Luciano Ramalho</author>
         <title>
            Fluent Python: Clear, Concise, and Effective Programming
        </title>
     </book>
     <book id="1491939362" price='29.83'>
         <author>Allen B. Downey</author>
         <title>
 Think Python: How to Think Like a Computer Scientist
        </title>
     </book>
</books>
```

XPath expression accepts key attributes by adding the @ character in front of the key name. Listed in the following table are a few examples of XPath using attributes with a brief description.

XPath expression | Description
--- | ---
`//book/@price` | Selects the price attribute for a book
`//book` |  Selects the book field and its elements
`//book[@price>30]` | Selects all elements in book the price attribute of which is greater than 30
`//book[@price<30]/title` |  Selects title from books where the price attribute is less than 30
`//book/@id` |  Selects the id attribute and its value. The //@id expression also results in the same output
`//book[@id=1491939362]/author` |  Selects author from book where id=1491939362


We have tried to explore and learn a few basic features about XPath and writing expressions to retrieve the desired content. In the Scraping using lxml - a Python library section, we will use Python programming libraries to further explore deploying code using XPath to scrape provided documents (XML or HTML) and learn to generate or create XPath expressions using browser tools.