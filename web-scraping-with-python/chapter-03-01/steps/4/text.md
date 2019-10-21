The XML Path (XPath) language is a part of XML-based technologies (XML, XSLT, and XQuery), which deal with navigating through DOM elements or locating nodes in XML (or HTML) documents using expressions also known as XPath expressions. XPath is normally a path that identifies nodes in documents. XPath is also a W3C (short for World Wide Web Consortium) recommendation (https://www.w3.org/TR/xpath/all/).

XPath or XPath expressions are also identified as absolute and relative:

- The absolute path is an expression that represents a complete path from the root element to the desired element. It begins with /html and looks like `/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/span/b[1]`. Individual elements are identified with their position and represented by an index number.
- The relative path represents an expression chosen from certain selected elements to the desired element. Relative paths are shorter and readable in comparison to absolute paths and look like `//*[@id="answer"]/div/span/b[@class="text"]`. A relative path is often preferred over an absolute path as element indexes, attributes, logical expressions, and so on can be combined and articulated in a single expression.

With XPath expressions, we can navigate hierarchically through elements and reach the targeted one. XPath is also implemented by various programming languages, such as JavaScript, Java, PHP, Python, and C++. Web applications and browsers also have built-in support to XPath.

Expressions can be built using a number of built-in functions available for various data types. Operations related to general math (+, -, *, /), comparison (<, >, =, !=, >=, <=), and combination operators (and, or, and mod) can also be used to build expression. XPath is also a core block for XML technologies such as XQuery and eXtensible Stylesheet Language Transformations (XSLT).

**Note:** `XML Query (XQuery)` is a query language that uses XPath expressions to extract data from XML document. 
XSLT is used to render XML in a more readable format.

As we can see from the two preceding XPaths tested, expressions are created almost like a filesystem (command line or Terminal path), which we use in various OS. XPath expressions contain code patterns, functions, and conditional statements and support the use of predicates.

Predicates are used to identify a specific node or element. Predicate expressions are written using square brackets that are similar to Python lists or array expressions.