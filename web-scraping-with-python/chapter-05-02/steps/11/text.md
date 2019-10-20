In this section, we will be using CSS Selectors with their extensions such as ::text and ::attr along with extract() and strip(). Similar to response.xpath(), available to run XPath expressions, CSS Selectors can be run using response.css(). The css() selector matches the elements using the provided expressions:

```
'''
Using CSS Selectors
'''
def parse(self, response):
    print("Response Type >>> ", type(response))
    rows = response.css("div.quote") #root element

    for row in rows:
        item = QuotesItem()

        item['tags'] = row.css('div.tags > meta[itemprop="keywords"]::attr("content")').extract_first()
        item['author'] = row.css('small[itemprop="author"]::text').extract_first()
        item['quote'] = row.css('span[itemprop="text"]::text').extract_first()
        item['author_link'] = row.css('a:contains("(about)")::attr(href)').extract_first()

        if len(item['author_link'])>0:
            item['author_link'] = 'http://quotes.toscrape.com'+item['author_link']

        yield item
```

As seen in the preceding code, rows represent individual elements with the post-item class, iterated for obtaining the Item fields. 
