We need to generate a Spider to collect the data. The Spider will perform the crawling activity. An empty default folder named spiders does exist inside the ScrapyProjects\Quotes\Quotes folder.

From the `ScrapyProjects\Quotes` project folder, run or execute the scrapy genspider quotes quotes.toscrape.com command.

 `cd Quotes`{{execute}}

 `scrapy genspider quotes quotes.toscrape.com`{{execute}}

Successful execution of the command will create a quotes.py file, that is, a Spider inside the ScrapyProjects\Quotes\Quotes\spiders\ path. The generated Spider class QuotesSpider inherits Scrapy features from scrapy.Spider. There's also a few required properties and functions found inside QuotesSpider as seen in the following code:

```
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        'http://www.quotes.toscrape.com/',
    )

    def parse(self, response):
        pass
```

The QuotesSpider Spider class contains automatically generated properties that are assigned for specific tasks, as explored in the following list:

- **name:** This variable holds value, that is, the name of the Spider quotes as seen in the preceding code. The name identifies the Spider and can be used to access it. The value of the name is provided through the command-line instructions while issuing scrapy genspider quotes, which is the first parameter after genspider.
- **allowed_domains:** The created Spiders are allowed to crawl within the listed domains found in the allowed_domains. The last parameter passed is the quotes.toscrape.com parameter, while generating a Spider is actually a domain name that will be listed inside an allowed_domains list.
- A domain name passed to allowed_domains will generate URLs for start_urls. If there are any chances of URL redirection, such URL domain names need to be mentioned inside the allowed_domains. 
- **start_urls:** These contain a list of URLs that are actually processed by Spider to crawl. The domain names found or provided to the allowed_domains are automatically added to this list and can be manually added or updated. Scrapy generates the URLs for start_urls adding HTTP protocols. On a few occasions, we might also need to change or fix the URLs manually, for example, www added to the domain name needs to be removed. start_urls after the update will be seen as in the following code:

```
start_urls = ( 'http://quotes.toscrape.com/',)
```

parse(): This function is implemented with the logic relevant to data extraction or processing. parse() acts as a main controller and starting point for scraping activity. Spiders created for the main project will begin processing the provided URLs or start_urls from, or inside, the parse(). XPath-and CSS Selector-related expressions and codes are implemented, and extracted values are also added to the item (that is, the QuotesItem from the item.py file). 
