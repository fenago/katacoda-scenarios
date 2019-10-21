The parse() function inside Spider is the place to implement all logical processes for scraping data. As seen in the following code, we are using XPath expressions in this Spider to extract the values for the required fields in QuotesItem. 

As seen in the next code snippet an item object from QuotesItem is used to collect individual field-related data and it's finally being collected and iterated using the Python keyword yield. parse() is actually a generator that is returning object item from QuotesItem.

Python keyword yield is used to return a generator. Generators are functions that return an object that can be iterated. The Python function can be treated as a generator using the yield in place of the return.
parse() has an additional argument response; this is an object of scrapy.http.response.html.HtmlResponse that is returned by Scrapy with the page content of the accessed or crawled URL. The response obtained can be used with XPath and CSS Selectors for further scraping activities:

```
'''
Using XPath
'''
def parse(self, response):
 print("Response Type >>> ", type(response))
 rows = response.xpath("//div[@class='quote']") #root element
 
 print("Quotes Count >> ", rows.__len__())
 for row in rows:
     item = QuotesItem()

     item['tags'] =     row.xpath('div[@class="tags"]/meta[@itemprop="keywords"]/@content').extract_first().strip()
     item['author'] = row.xpath('//span/small[@itemprop="author"]/text()').extract_first()
     item['quote'] = row.xpath('span[@itemprop="text"]/text()').extract_first()
     item['author_link'] = row.xpath('//a[contains(@href,"/author/")]/@href').extract_first()

     if len(item['author_link'])>0:
         item['author_link'] = 'http://quotes.toscrape.com'+item['author_link']

     yield item
```

As seen in the following code, the XPath expression is being applied to the response using the xpath() expression and is used as a response.xpath(). XPath expressions or queries provided to response.xpath() are parsed as rows, that is, an element block containing the desired elements for fields.

The obtained rows will be iterated for extracting individual element values by providing the XPath query and using additional functions as listed here:

- **extract():** Extract all the elements matching the provided expression.
- **extract_first():** Extract only the first element that matches the provided expression.
- **strip():** Clears the whitespace characters from the beginning and the end of the string. We need to be careful using this function to the extracted content if they result in a type other than string such as NoneType or List, and so on as it can result in an error.
In this section, we have collected quotes listings details using XPath; in the next section, we will cover the same process but using CSS Selectors.