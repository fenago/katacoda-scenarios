Now that we've confirmed the required libraries and system requirements, we will proceed with loading the URLs. While looking for contents from a URL, it is also necessary to confirm and verify the exact URL that has been chosen for the required content. Contents can be found on single web pages or scattered across multiple pages, and it might not always be the HTML sources we are looking for.

We will load some URLs and explore the content using a couple of tasks.

Before loading URLs using Python script, it's also advisable to verify the URLs are working properly and contain the detail we are looking for, using web browsers. Developer tools can also be used for similar scenarios, as discussed in Chapter 1, Web Scraping Fundamentals, in the Developer tools section.


**Task 1:** To view data related to the listings of the most popular websites from Wikipedia. We will identify data from the Site, Domain, and Type columns in the page source.

We will follow the steps at the following link to achieve our task (a data extraction-related activity will be done in Chapter 3, Using LXML, XPath and CSS Selectors): https://en.wikipedia.org/wiki/List_of_most_popular_websites. 

Search Wikipedia for the information we are looking for. The preceding link can be easily viewed in a web browser. The content is in tabular format (as shown in the following screenshot), and so the data can be collected by repeatedly using the select, copy, and paste actions, or by collecting all the text inside the table.

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-02-01/steps/6/1.png)

After finalizing the link that contains the content we require, let's load the link using Python. We are making a request to the link and willing to see the response returned by both libraries, that is, urllib and requests:

Let's use urllib:

`import urllib.request as req #import module request from urllib`{{execute}}

`link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"`{{execute}}

`response = req.urlopen(link)  #load the link using method urlopen()`{{execute}}

`print(type(response))   #print type of response object`{{execute}}

`print(response.read()) #read response content`{{execute}}


The urlopen() function from urllib.request has been passed with the selected URL or request that has been made to the URL and response is received, that is, HTTPResponse. response that's received for the request made can be read using the read() method.