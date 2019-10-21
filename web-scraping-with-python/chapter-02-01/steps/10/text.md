Using Python code, we can find charset in the HTTP header:

`import urllib.request`{{execute}}

`someRequest = urllib.request.urlopen(link) #load/Open the URL`{{execute}} 

`someRequest.getheaders() #Lists all HTTP headers. `{{execute}} 

`someRequest.getheader("Content-Type") #return value of header 'Content-Type'`{{execute}} 

```
'text/html'
```

charset that was identified will be used to encode and decode with `requests.get(link).content.decode('utf-8')`{{execute}} .

**Note:** Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings. All text is Unicode; however, encoded Unicode is represented as binary data. The type that's used to hold text is [str](https://docs.python.org/3/library/stdtypes.html#str), and the type that's used to hold data is [bytes](https://docs.python.org/3/library/stdtypes.html#bytes).

In this section, we set up and verified our technical requirements, and also explored URL loading and content viewing.