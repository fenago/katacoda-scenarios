In order to log in, you need to log in with a CSRF token (any username/password works). 
Let's set up the code. The pyquery and requests libraries need to be imported and the required URLs will be collected and used. The getCustomHeaders() function, together with the cookieHeader argument, is used to set the cookie value for the URL request headers. The responseCookies() function, together with the response argument, displays the headers and cookies, and also returns the Set-Cookie value from cookies: 

```
from pyquery import PyQuery as pq
import requests
mainUrl = "http://toscrape.com/"
loginUrl = "http://quotes.toscrape.com/login"
quoteUrl = "http://quotes.toscrape.com/"

def getCustomHeaders(cookieHeader):
    return {
        'Host': 'quotes.toscrape.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://quotes.toscrape.com/login',
        'Content-Type': 'application/x-www-form-urlencoded', 
        'Cookie': cookieHeader
    }

def responseCookies(response):
    headers = response.headers
    cookies = response.cookies
    print("Headers: ", headers)
    print("Cookies: ", cookies)
    return headers['Set-Cookie']

if __name__ == '__main__':
```

For more information on HTTP and HTTP headers, please visit Chapter 1, Web Scraping Fundamentals, the Understanding Web Development and Technologies and HTTP sections.
