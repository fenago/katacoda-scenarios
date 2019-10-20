
In this section, we will be collecting XPath expressions and CSS queries for the required element. In a similar way to how we explored the Page Inspector and Elements panel in the preceding section, let's proceed with the following steps to obtain an XPath expression and CSS query for the selected element:

- Choose the Element Selector and obtain the element code
- Right-click the mouse on the element code obtained
- Choose the Copy option from the menu
- From the sub-menu options, choose Copy XPath for XPath expression for chosen element
- Or choose Copy selector for the CSS selector (query)

As seen in the following screenshot, we select various sections of a single book item and obtain respective CSS selectors or XPath expressions, accessing the menu options:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/6/1.png)

Copying XPath and CSS selector using page inspect
The following are some XPath and CSS selectors collected using DevTools for items available with products such as book title and price.

**XPath selectors** using DevTools:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/6/1.JPG)

**CSS query selectors** using DevTools:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/6/2.JPG)

Similarly other essential XPath or CSS selectors will also be collected as required. After collection and verification or cleaning (shortening) of these expressions and queries, scraping logic is applied using Python programming to automate the data collection.

Again, there's no particular way out of following the steps as discussed in the previous section. The XPath or CSS selector can also be determined or formed revealing the HTML source or page source; there are also lots of browser-based extensions that support similar tasks. It's the developer's choice to be comfortable with any way out that we have discussed to deal with the XPath and CSS selectors.

One of the recently listed browser-based extensions to generate XPath and CSS selectors for Google Chrome is ChroPath (https://autonomiq.io/chropath/). Writing customized expressions and queries is advised for self-practice and knowledge. Extensions and other similar applications should be used while processing a large information source.

In this section, we inspected and explored the Elements panel for element identification and DOM navigation: modifying, removing elements, altering scripts, and so on. Related options also exist in the Elements panel. In the following section, we will be using the Python library, lxml, to code Scraper and collect data from the chosen website using XPath and CSS selector.

