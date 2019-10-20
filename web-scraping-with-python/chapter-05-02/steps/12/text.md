In the preceding section, we tried scraping data for the URL in start_urls, that is, http://quotes.toscrape.com/. It's also to be noted that this particular URL results in quotes listings for the first page only. 

Quotes listings are found across multiple pages and we need to access each one of those pages to collect the information. A pattern for pagination links is found in the following list:

- http://quotes.toscrape.com/ (first page)
- http://quotes.toscrape.com/page/2/
- http://quotes.toscrape.com/page/3/

XPath and CSS Selectors used inside the parse(), as found in codes from the preceding section, will be scraping data from the first page or page 1 only. Pagination links found across pages can be requested and extracted by passing the link to parse() inside Spider using the callback argument from a scrapy.Request.

As seen in the following code, a link to page 2 found on page 1 is extracted and passed to scrapy.Request, making a request to the nextPage processing plus yielding the item fields using parse(). Similarly, the iteration takes place until the link to the next page or nextPage exists

```
def parse(self, response):
    print("Response Type >>> ", type(response))
    rows = response.css("div.quote")
    
    for row in rows:
        item = QuotesItem()
        ......
        ......
        yield item
    
    #using CSS
    nextPage = response.css("ul.pager > li.next > a::attr(href)").extract_first() 
    #using XPath
    #nextPage = response.xpath("//ul[@class='pager']//li[@class='next']/a/@href").extract_first()
    
    if nextPage:
        print("Next Page URL: ",nextPage)
        #nextPage obtained from either XPath or CSS can be used.
        yield scrapy.Request('http://quotes.toscrape.com'+nextPage,callback=self.parse)

 print('Completed')
```
