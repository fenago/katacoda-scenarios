
The urllib library is a standard Python package that collects several modules to work with HTTP-related communication models. Modules inside urllib are specially designed and contain functions and classes that deal with various types of client-server communication. 

Similarly named packages also exist, like urllib2, an extensible library, and urllib3, a powerful HTTP client that addresses missing features from Python standard libraries.
Two of the most important urllib modules that deal with URL requests and responses are as follows. We will be using these modules in this and upcoming chapters:

urllib.request: Used for opening and reading URLs and requesting or accessing network resources (cookies, authentication, and so on)
urllib.response: This module is used to provide a response to the requests that are generated
There are a number of functions and public attributes that exist to handle request information and process response data that's relevant to HTTP requests, such as urlopen(), urlretrieve(), getcode(), getheaders(), getheader(), geturl(), read(), readline(), and many more. 

We can use Python's built-in dir() function to display a module's content, such as its classes, functions, and attributes, as shown in the following code:

`python`{{execute}}

`import urllib.request`{{execute}}

`dir(urllib.request) #list features available from urllib.request`{{execute}}

```
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor',....'Request', 'URLError', 'URLopener',......'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_registry', 'quote', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'to_bytes', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
```
