We will be using http://books.toscrape.com/ from http://toscrape.com/. toscrape provides resources related to web scraping for beginners and developers to learn and implement Scraper.

Let's open the http://books.toscrape.com URL using the web browser, Google Chrome, as shown here:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/4/1.png)

As the page content is successfully loaded, we can load DevTools with a right-click on the page and press the option Inspect or by pressing Ctrl + Shift + I. If accessing through the Chrome menu, click More Tools and Developer Tools. The browser should look similar to the content in the preceding screenshot.

As you can see in the preceding screenshot, in inspect mode, the following is loaded:

- Panel elements are default on the left-hand side.
- CSS styles-based content is on the right-hand side.
- We notice the DOM navigation or elements path in the bottom left-hand corner, for example, html.no-js body .... div.page_inner div.row.

We have covered a basic overview of such panels in Chapter 1, Web Scraping Fundamentals, in the Developer Tools section. As developer tools get loaded, we can find a pointer-icon listed, at first, from the left; this is used for selecting elements from the page, as shown in the following screenshot; this element selector (inspector) can be turned ON/OFF using Ctrl + Shift + C:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/4/2.png)