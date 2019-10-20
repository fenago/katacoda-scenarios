In this section, we will utilize most of the techniques and concepts learned throughout the chapters so far and implement some scraping tasks.

For the task ahead, we will first select the URLs required. In this case, it will be http://books.toscrape.com/, but by targeting a music category, which [is](http://books.toscrape.com/catalogue/category/books/music_14/index.html). With the chosen target URL, its time now to explore the web page and identify the content that we are willing to extract.

We are willing to collect certain information such as the title, price, availability, imageUrl, and rating found for each individual item (that is, the Article element) listed in the page. We will attempt different techniques using lxml and XPath to scrape data from single and multiple pages, plus the use of CSS selectors.

#### Example 1 – extracting selected data from a single page using lxml.html.xpath
In this example, we will use XPath to collect information from the provided URL and use lxml features.

In the following code, a musicUrl string object contains a link to the page. musicUrl is parsed using the parse() function, which results in the doc and lxml.etree.ElementTree objects:

```
import lxml.html
musicUrl= "http://books.toscrape.com/catalogue/category/books/music_14/index.html"
doc = lxml.html.parse(musicUrl)
```

We now have an ElementTree doc available; we will be collecting the XPath expressions for the chosen fields such as title and price, found on the musicUrl page.

```
#base element
articles = doc.xpath("//*[@id='default']/div/div/div/div/section/div[2]/ol/li[1]/article")[0]

#individual element inside base
title = articles.xpath("//h3/a/text()")
price = articles.xpath("//div[2]/p[contains(@class,'price_color')]/text()")
availability = articles.xpath("//div[2]/p[2][contains(@class,'availability')]/text()[normalize-space()]")
imageUrl = articles.xpath("//div[1][contains(@class,'image_container')]/a/img/@src")
starRating = articles.xpath("//p[contains(@class,'star-rating')]/@class")
```

The XPath for the preceding articles posseses all of the fields that are available inside  <article>, such as title, price, availability, imageUrl, and starRating. The articles field is an expression of a type of parent element with child elements. Also, individual XPath expressions for child elements are also declared, such as the title field, that is, title = articles.xpath("//h3/a/text()"). We can notice the use of articles in the expression.

It is also to be noticed in child expressions that element attributes or key names such as class or src can also be used as @class and @src, respectively.

Now that the individual expressions have been set up, we can print the items that collect all of the found information for available expressions and return those in the Python list. The cleaning and formatting for data received has also been done with the map(), replace(), and strip() Python functions and Lambda operator, as seen in the following code:

```
#cleaning and formatting 
stock = list(map(lambda stock:stock.strip(),availability))
images = list(map(lambda img:img.replace('../../../..','http://books.toscrape.com'),imageUrl))
rating = list(map(lambda rating:rating.replace('star-rating ',''),starRating))

print(title)
print(price)
print(stock)
print(images)
print(rating)
```

Collected or extracted data might require the additional task of cleaning, that is, removing unwanted characters, white spaces, and so on. It might also require formatting or transforming data into the desired format such as converting string date and time into numerical values, and so on. These two actions help to maintain some predefined or same-structured data.


Data collected in such a way can be merged into a single Python object as shown in the following code or can be written into external files such as CSV or JSON for further processing:

```
#Merging all 
dataSet = zip(title,price,stock,images,rating)
print(list(dataSet))
```

dataSet in the preceding code is generated using the zip() Python function. zip() collects individual indexes from all provided list objects and appends them as a tuple. The final output from dataSet has particular values for each <article>

#### Run Code
Now, run the python code by running: `python scrapelxml.py`{{execute}}

The final output for the preceding code is shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/11/1.JPG)
