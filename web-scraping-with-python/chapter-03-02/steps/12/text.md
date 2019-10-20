In example 1, we tried the simple XPath-based technique for a URL with a limited number of results on a single page. In this case, we will be targeting a food and drink category, [that is](http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html), which has its content across pages. An XPath-based looping operation will be used in this example, which supports a more effective collection of data.

As we will be dealing with multiple pages, it's good practice to check for a few individual page URLs that can be found in the browser while moving through the listed pages. Most of the time, it might contain some patterns that can solve the puzzle easily, as used in the following code:

```
import lxml.html
from lxml.etree import XPath

baseUrl = "http://books.toscrape.com/"

#Main URL
bookUrl = "http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html"

#Page URL Pattern obtained (eg: page-1.html, page-2.html...)
pageUrl = "http://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-"
bookUrl is the main URL we are interested in; it also contains the page link for the next page, which contains a pattern, as found in pageUrl, for example, page-2.html
```


An empty dataSet list is defined to hold data found from each article across pages.

An individual page URL is obtained by concatenating pageUrl with a page number, and .html. totalPages is found after calculating totalArticles and perPageArticles as traced from the page itself. totalPages obtained will give an exact loop count and is more manageable to apply in the loop (the while loop is found in the code):

```
articles = XPath("//*[@id='default']//ol/li[position()>0]")

titlePath = XPath(".//article[contains(@class,'product_pod')]/h3/a/text()")
pricePath = XPath(".//article/div[2]/p[contains(@class,'price_color')]/text()")
stockPath = XPath(".//article/div[2]/p[2][contains(@class,'availability')]/text()[normalize-space()]")
imagePath = XPath(".//article/div[1][contains(@class,'image_container')]/a/img/@src")
starRating = XPath(".//article/p[contains(@class,'star-rating')]/@class")
```

As we can see in the previous code, articles is the major XPath expression used to loop for finding individual elements inside the `<article>` field. The expression should contain a certain condition that can be fulfilled to preform a loop; in this case, we identified that the `<article>` field exists inside of the `<ol><li>` element.