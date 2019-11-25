Pseudo selectors are a set of handy choices when it comes to identifying or selecting the elements based on their position.

The following table lists some of the ways these types of selectors might be used, with a brief description:

CSS query | Description
--- | ---
`a:gt(0)` | Selects all `<a>` elements except those indexed at a 0 position
`a:eq(2)` | Selects `<a>` element which are indexed at 2
`a:first-child` | Selects every `<a>` element that is the first child of its parent
`a:last-child` | Selects every `<a>` element that is the last child of its parent
`a:last-of-type` | Selects the last element `<a>` of its parent
`:not(p)` | Selects all elements except `<p>`
`a:nth-child(1)` | Selects every `<a>` from the first child of its parent
`a:nth-last-child(3)` | Selects every third `<a>` from the last child of its parent
`a:nth-of-type(3)` | Selects every third `<a>` element of its parent
`a:nth-last-of-type(3)` | Selects every `<a>` element, at the third position from last, of its parent


 
CSS selectors are used as a convenient alternative to XPath expressions for selecting elements, as they are shorter in length compared to absolute XPath and use simple patterns in expressions that are easy to read and manage. CSS selectors can be converted into XPath expressions, but not vice versa.

There are also a number of tools available online, which allow the conversion of a CSS selector query into an XPath expression; one of these is https://css-selector-to-xpath.appspot.com/, as seen in the following screenshot; we shouldn't always trust the tools available and results should be tested before applying them in code:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-01/steps/12/1.png)

As described in the preceding screenshot, CSS selectors are used to select elements from a data extraction perspective and can be used in Scraper codes or even while applying styles to selected elements from a styling perspective.

In this section, we learned about the most popular web-related pattern-finding techniques of XPath and CSS selectors.