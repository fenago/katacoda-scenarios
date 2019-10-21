In order to request data, Query Information, or URL arguments need to be used as key-value pair of information that are appended to the desired URL. Such a URL is usually processed with the HTTP GET method. Query information that's passed to the request object should be encoded using urlencode(). 

urlencode() ensures that arguments comply with the W3C standard and are accepted by the server. parse_qs() parses percent-encoded query strings to the Python dictionary. The following code demonstrates an example of using urlencode():


`import urllib.parse as urlparse`{{execute}}

`data = {'param1': 'value1', 'param2': 'value2'}`{{execute}}

`urlparse.urlencode(data)`{{execute}}

`param1=value1&param2=value2`

`urlparse.parse_qs(urlparse.urlencode(data))`{{execute}}

`{'param1': ['value1'], 'param2': ['value2']}`

`urlparse.urlencode(data).encode('utf-8')`{{execute}}

You may also need to encode the special characters in a URL before processing the request to the server:

**Note:**  that urllib.parse contains the quote(), quote_plus(), and unquote() functions, which permit error-free server requests:

quote() is generally applied to the URL path (listed with urlsplit() or urlparse()) or queried with reserved and special characters (defined by RFC 3986) before it's passed to urlencode() to ensure that the server's acceptable. Default encoding is done with UTF-8. 
quote_plus() also encodes special characters, spaces, and the URL separator, /. 
unquote() and unquote_plus() are used to revert the encoding that's applied by using quote() and quote_plus().
 