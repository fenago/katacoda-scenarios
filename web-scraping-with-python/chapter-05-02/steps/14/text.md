We need to run a Spider and look for data for item fields in the provided URLs. We can start running the Spider from the command line by issuing the `scrapy crawl quotes`{{execute}} command or as seen in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-02/steps/14/1.png)

#### Running a Spider (scrapy crawl quotes)
The Scrapy argument crawl is provided with a Spider name (quotes) in the command. A successful run of the command will result in information about Scrapy, bots, Spider, crawling stats, and HTTP methods, and will list the item data as a dictionary. 

While executing a Spider we will receive various forms of information, such as INFO/DEBUG/scrapy statistics a