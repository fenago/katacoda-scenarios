
These functions are demonstrated in the following code:

`import urllib.parse as urlparse`{{execute}}

`url="http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false"`{{execute}}

`urlparse.quote(url)`{{execute}}

    'http%3A//localhost%3A8080/~cache/data%20file%3Fid%3D1345322%26display%3Dyes%26expiry%3Dfalse'

`urlparse.unquote(url)`{{execute}}

    'http://localhost:8080/~cache/data file?id=1345322&display=yes&expiry=false'

`urlparse.quote_plus(url)`{{execute}}

 'http%3A%2F%2Flocalhost%3A8080%2F~cache%2Fdata+file%3Fid%3D1345322%26display%3Dyes%26expiry%3Dfalse' 

`urlparse.unquote_plus(url)`{{execute}}

The urljoin() function from urllib.parse helps obtain the URL from the provided arguments, as demonstrated in the following code:

`import urllib.parse as urlparse`{{execute}}

`urlparse.urljoin('http://localhost:8080/~cache/','data file') #creating URL`{{execute}}

`urlparse.urljoin('http://localhost:8080/~cache/data file/','id=1345322&display=yes')`{{execute}}

urllib.robotparser, as its name suggests, helps parse robots.txt and identifies agent-based rules.

As we can see in the following code, par, which is an object of RobotFileParser, can be used to set a URL via the set_url() function. It can also read contents with the read() function. Functions such as can_fetch() can return a Boolean answer for the evaluated condition:


`import urllib.robotparser as robot`{{execute}}

```par = robot.RobotFileParser()
par.set_url('https://www.samsclub.com/robots.txt') #setting robots URL
par.read()  #reading URL content
print(par)```{{execute}}


```
User-agent: *
Allow: /sams/account/signin/createSession.jsp
Disallow: /cgi-bin/
Disallow: /sams/checkout/
Disallow: /sams/account/
Disallow: /sams/cart/
Disallow: /sams/eValues/clubInsiderOffers.jsp
Disallow: /friend
Allow: /sams/account/referal/
```


`par.can_fetch('*','https://www.samsclub.com/category') #verify if URL is 'Allow' to Crawlers`{{execute}}


`par.can_fetch('*','https://www.samsclub.com/friend')`{{execute}}

As we can see, https://www.samsclub.com/friend returns `False` when passed with the `can_fetch()` function, thus satisfying the `Disallow: /friend` directives found in robots.txt. Similarly, https://www.samsclub.com/category returns True as there are no listed directives that restrict the category URL. 

However, there are some limitations to using urllib.request. Connection-based delays can occur while using functions like urlopen() and urlretrieve(). These functions return raw data and need to be converted into the required type for the parser before they can be used in the scraping process.

Deploying threads, or threading, is considered an effective technique when dealing with HTTP requests and responses.
