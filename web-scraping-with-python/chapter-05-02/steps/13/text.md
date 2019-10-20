We can also obtain the pagination-based result by making changes only to start_urls as seen in the code next. Using this process doesn't require the use of nextPage or scrapy.Request as used in the preceding code.

URLs to be crawled can be listed inside start_url and are recursively implemented by parse() as seen in the following code:

```
start_urls = (
    'http://quotes.toscrape.com/',
    'http://quotes.toscrape.com/page/1/',
    'http://quotes.toscrape.com/page/2/',
)
```

We can also obtain a list of URLs using the Python list comprehension technique. The range() function used in the following code accepts the start and end of the argument, that is, 1 and 4, and will result in the numbers 1, 2, and 3 as follows:

```
start_urls = ['http://quotes.toscrape.com/page/%s' % page for page in xrange(1, 6)]
```

With extraction logic along with pagination and the item declared, in the next section, we will run the crawler quotes and export the item to the external files. 