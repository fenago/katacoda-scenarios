We can also run the Spider and save the item found or data scraped to the external files. Data is exported or stored in files for easy access, usage, and convenience in sharing and managing. 

With Scrapy, we can export scraped data to external files using crawl commands as seen in the following list: 

To extract data to a CSV file we can use the scrapy following command as seen in the following screenshot:

`scrapy crawl quotes -o quotes.csv`{{execute}}

`cat quotes.csv`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-02/steps/15/1.png)

To extract data to JSON file format, we can use the C:\ScrapyProjects\Quotes>  command as seen in the following:

`scrapy crawl quotes -o quotes.json`{{execute}}

`cat quotes.json`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-02/steps/15/2.png)

The -o parameter followed by a filename will be generated inside the main project folder. Please refer to the official Scrapy documentation about feed exports [at](http://docs.scrapy.org/en/latest/topics/feed-exports.html) for more detailed information and file types that can be used to export data.

In this section, we learned about Scrapy and used it to create a Spider to scrape data and export the data scraped to external files. In the next section, we will deploy the crawler on the web.