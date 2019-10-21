

We can move the mouse on the page loaded after turning ON the element selector. Basically, we are searching for the exact HTML element that we are pointing to using the mouse:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/5/1.png)

As seen in the preceding screenshot, the element has been selected and, as we move the mouse over the first book picture available, this action results in the following:

- The div.image_container element is displayed and selected in the page itself.
- Inside the elements panel source, we can find the particular HTML code, <div class="image_container">, being highlighted too. This information (where the book picture is located) can also be found using right-click + page source or Ctrl + U and searching for the specific content.

The same action can be repeated for various sections of HTML content that we wish to scrape, as in the following examples:

- The price for a listed book is found inside the div.product_price element.
- The star-rating is found inside p.star-rating.
- The book title is found inside `<h3>`, found before div.product_price or after p.star-rating.
- The book detail link is found inside `<a>`, which exists inside `<h3>`.

From the following screenshot, it's also clear that the previously listed elements are all found inside article.product_prod. Also, at the bottom of the following screenshot, we can identify the DOM path as article.product_prod:
 
![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/5/2.png)

DOM navigation, as found in the preceding screenshots, can be beneficial while dealing with XPath expressions, and can verify the content using the page source, if the path or element displayed by the element inspector actually exists (inside the obtained page source).

DOM elements, navigation paths, and elements found using the elements inspector or selectors should be cross-verified for their existence in page sources or inside resources that are found in Network panels, to be sure.
