

Individual request-based headers can also be retrieved when getheader() is passed with desired header element, as shown in the following code. Here, we can see we can obtain the value for the Content-Type header. The same result can also be achieved using the info() function:

`linkRequest.getheader("Content-Type")`{{execute}}  

`linkRequest.info()["content-type"]`{{execute}}
  
    'text/html; charset=ISO-8859-1'

**Note:** urllib.error deals with the exceptions raised by urllib.request. Exceptions like URLError and HTTPError can be raised for a request.The following code demonstrates the use of urllib.error:

Exception handling deals with error handling and management in programming. Code that uses exception handling is also considered an effective technique and is often prescribed to adapt.

`import urllib.request as request`{{execute}}

`import urllib.error as error`{{execute}}

**Note:** Please press enter to run multiline code after clicking following:

```try:  #attempting an error case
    request.urlopen("https://www.python.ogr") #wrong URL is passed to urlopen()
except error.URLError as e:
    print("Error Occurred: ",e.reason)```{{execute}}

```
Error Occurred: [Errno 11001] getaddrinfo failed #output
```

urllib.parse is used to encode/decode request(data) or links, add/update headers, and analyze, parse, and manipulate URLs. Parsed URL strings or objects are processed with urllib.request.

Furthermore, urlencode(), urlparse(), urljoin(), urlsplit(), quote_plus() are a few important functions that are available in urllib.parse, as shown in the following code:

`import urllib.parse as urlparse`{{execute}}

`print(dir(urlparse)) #listing features from urlparse`{{execute}}

We get the following output:

```
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', .........'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative']
```

The urlsplit() function from urllib.parse splits the URL that's passed into the namedtuple object. Each name in tuple identifies parts of the URL. These parts can be separated and retrieved in other variables and used as needed. The following code implements urlsplit() for amazonUrl:

`amazonUrl ='https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'`{{execute}}

`print(urlparse.urlsplit(amazonUrl)) #split amazonURL`{{execute}}

`urlparse.SplitResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', fragment='')`{{execute}}

`print(urlparse.urlsplit(amazonUrl).query) #query-string from amazonURL`{{execute}}

`url='search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books'`{{execute}}

`print(urlparse.urlsplit(amazonUrl).scheme) #return URL scheme`{{execute}}

Using the urlparse() function from urllib.parse results in the ParseResult object. It differs in terms of the parameters (params and path) that are retrieved in he URL compared to urlsplit(). The following code prints the object from urlparse():


`print(urlparse.urlparse(amazonUrl)) #parsing components of amazonUrl`{{execute}}

```
    ParseResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', params='', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Packt+Books', fragment='')
```
