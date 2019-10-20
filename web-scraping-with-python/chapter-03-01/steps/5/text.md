Let's explore a few XPath expressions from the XML content as seen in the following from the food.xml file:


#### XML content
In the following example, we will be using XPath-Tester from Code Beautify (https://codebeautify.org/Xpath-Tester). Use the XML source URL provided earlier to fetch the XML content and use it with the Code Beautify XPath-Tester.

You can use https://codebeautify.org/Xpath-Tester, https://www.freeformatter.com/xpath-tester.htm, or any other XPath tester tools that are available free on the web.

Everything is a node in an XML document, for example, menus, food, and price. An XML node can be an element itself (elements are types or entities that have start and end tags).

The preceding XML document can also be read as inherited element blocks. Parent node menus contain multiple child nodes food, which distinguishes child elements for appropriate values and proper data types. The XPath expression, //food, as shown in the following screenshot, displays the result for the selected node food. Node selection also retrieves the child nodes within the parents, as seen in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-01/steps/5/1.png)


The XPath expression in the following screenshot selects the child node, price, found inside all parent nodes food. There are six child food nodes available, each of them containing price, name, description, feedback, and rating:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-01/steps/5/2.png)


As we can see from the two preceding XPaths tested, expressions are created almost like a filesystem (command line or Terminal path), which we use in various OS. XPath expressions contain code patterns, functions, and conditional statements and support the use of predicates.