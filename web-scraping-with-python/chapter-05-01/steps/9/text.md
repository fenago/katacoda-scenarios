The implemented get_details() function is being coded for pagination and scraping logic. The read_url() function is supplied with a dynamically generated page URL to manage the pagination. 

The response element from the read_url() function is parsed using lxml to obtain the soup element. The rows obtained using the soup list all of the quotes available in a single page (that is, the element block containing the single quote details) found inside the `<div class="quote">` function and will be iterated to scrape data for individual items such as quote_tags, author_url, and author_name traversing through the quote element.

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter05/toscrape_quotes.py` to view python code file.

#### Run Code
Now, run the python code by running: `python toscrape_quotes.py`{{execute}}


#### Page source with quote element 
The individual items received are scraped, cleaned, and collected in a list maintaining the order of their column names and are written to the file using the writerow() function (appends the list of values to the file) accessed through the csv library and file handle.

The quotes.csv data file will contain scraped data as seen in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-01/steps/9/1.png)

`cat quotes.csv`{{execute}}

In this section, we explored various ways to traverse and search using Beautiful Soup. In the upcoming section, we will be using Scrapy, a web crawling framework.