
As shown in the following code, get_details() uses a while loop for pagination purposes, and is controlled by the nextPage value:

```
def get_details(page):
    """read 'page' url and append list of queried items to dataSet"""
    nextPage = True
    pageNo = 1
    while (nextPage):
        response = read_url(page + 'page/' + str(pageNo))
        if response.find("ul.pager:has('li.next')"):
            nextPage = True
        else:
            nextPage = False

        quotes = response.find('.quote')
        print("\nTotal Quotes found :", quotes.__len__(), ' in Page: ', pageNo)
        for quote in quotes.items():
            title = quote.find('[itemprop="text"]:first').text()
            author = quote.find('[itemprop="author"]:first').text()
            authorLink = quote.find('a[href*="/author/"]:first').attr('href')
            tags = quote.find('.tags [itemprop="keywords"]').attr('content')

            if authorLink:
                authorLink = 'http://quotes.toscrape.com' + authorLink
                linkDetail = read_url(authorLink)
                born_date = linkDetail.find('.author-born-date').text()
                born_location = linkDetail.find('.author-born-location').text()
                if born_location.startswith('in'):
                    born_location = born_location.replace('in ','')
               
            dataSet.append(dict(zip(keys,[tags,authorLink,author,born_date,born_location,title[0:50]])))
        
        pageNo += 1
```

`:has()` returns the element that matches the selector that's passed to it. In this example, we are confirming whether the pager class has an `<li>` element with the next class, that is, ul.pager:has('li.next'). If the expression is true, then a page link exists for another page, and else terminates the loop.

quotes that are obtained are iterated using items() to obtain title, author, tags, and authorLink. The authorLink URL is further processed using the read_url() function in order to obtain author-related, specific information from the .author-born-date and .author-born-location classes for born_date and born_location, respectively.

The elements classes we used in the preceding code can be found in Page Source, as shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-04-02/steps/6/1.png)

The zip() Python function is used with keys and quotes fields, which is appended to dataSet as a Python Dictionary.

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter04/example2_quotes_authors.py` to view python code file.

#### Run Code
Now, run the python code by running: `python example2_quotes_authors.py`{{execute}}
