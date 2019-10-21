A tree-type structure (also known as an element-tree) is a base model for most markup languages and is often referred to as the Document Object Model (DOM). With the help of the DOM and its defined conventions, we can access, traverse, and manipulate elements.

Elements are structured inside some parent elements, which are inside their own parent and so on; this describes a parent-child relationship that is the most significant feature of markup language. Many applications that support XML or markup language supports the DOM and even contain a parser to use.

For extraction, it is necessary to identify the exact location of information. Information can be found nested inside a tree structure and could possess some additional attributes to represent the content. XPath and CSS selectors are both used to navigate along the DOM and search for desired elements or nodes found in the document.

In the following sections, we will introduce both XPath and CSS selectors, and use them for a web-scraping purpose with a supportive Python library.