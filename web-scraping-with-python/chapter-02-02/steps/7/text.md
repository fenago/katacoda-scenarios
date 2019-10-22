Let's confirm the differences between urlparse() and urlsplit(). The localUrl that's created is parsed with both urlsplit() and urlparse(). params is only available with urlparse():

`import urllib.parse as urlparse`{{execute}}

`localUrl= 'http://localhost/programming/books;2018?browse=yes&sort=ASC#footer'`{{execute}}

`print(urlparse.urlsplit(localUrl))`{{execute}}

`urlparse.SplitResult(scheme='http', netloc='localhost', path='/programming/books;2018', query='browse=yes&sort=ASC', fragment='footer')`{{execute}}

`parseLink = urlparse.urlparse(localUrl)`{{execute}}

`print(parseLink)`{{execute}}

`print(parseLink.path) #path without domain information`{{execute}}

`print(parseLink.params) #parameters`{{execute}} 

`print(parseLink.fragment) #fragment information from URL`{{execute}}

Basically, urllib.request.Request accepts data and headers-related information, and headers can be assigned to an object using `add_header()`; for example, object.add_header('host','hostname') or object.add_header('referer','refererUrl').

