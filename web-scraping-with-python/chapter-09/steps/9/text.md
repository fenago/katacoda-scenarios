In this example, we will be extracting content from http://godfreysfeed.com/dealersandlocations.php. This website contains dealer locations information, which is shown in the screenshot that follows:

```
import re
import requests

def read_url(url):
'''
Handles URL Request and Response
Loads the URL provided using requests and returns the text of page source
'''
    pageSource = requests.get(url).text
    return pageSource

if __name__ == "__main__":
```

For this and the other examples in this section, we will be using the re and requests libraries in order to retrieve the page source, that is, pageSource. Here, we will be using the read_url() function to do so.

The page contains HTML `<form>` elements so that we can search for dealers based on the zipcode entered. There's also a geographic map with markers:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/9/1.png)

You can either perform form submission with zipcode or extract content from the map.

By analyzing the page source, we will find that there's no HTML elements with dealers' information. Implementing Regex fits this case perfectly. Here, dealers' information is found inside JavaScript code with variables such as latLng and infoWindowContent, as shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/9/2.png)
