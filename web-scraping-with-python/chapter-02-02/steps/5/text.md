
The urlopen() function accepts a URL or an urllib.request.Request object, such as requestObj, and returns a response through the urllib.response read() function, as shown in the following code:

`import urllib.request`{{execute}}

`link='https://www.google.com'`{{execute}}

`linkRequest = urllib.request.urlopen(link) #open link`{{execute}}

`print(type(linkRequest)) #object type`{{execute}}


`linkResponse = urllib.request.urlopen(link).read() #open link and read content`{{execute}}

`print(type(linkResponse))`{{execute}}


`requestObj = urllib.request.Request('https:/www.samsclub.com/robots.txt')`{{execute}}

`print(type(requestObj)) #object type`{{execute}}


`requestObjResponse = urllib.request.urlopen(link).read()`{{execute}}

`print(type(requestObjResponse))  #object type`{{execute}}

The object types that are returned are different in the case of linkRequest and requestObj from the urlopen() function and class request, respectively. The linkResponse and requestObjResponse objects were also created, which holds the urllib.response information of the read() function. 

Generally, urlopen() is used to read a response from the URL, while urllib.request.Request is used to send extra arguments like data or headers, and even to specify the HTTP method and retrieve a response. It can be used as follows:

`urllib.request.Request(link, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)`{{execute}}

urllib.response and its functions, such as read() and readline(), are used with the urllib.request objects.

If the request that was made was successful and received a response from the proper URL, we can check the HTTP status code, the HTTP method that was used, as well as the returned URL to view a description:

getcode() returns a HTTP status code. The same result can also be achieved using the code and status public attributes, as shown in the following code:

`linkRequest.getcode()  #can also be used as: linkRequest.code or linkRequest.status`{{execute}}

geturl() returns current the URL. It is sometimes handy to verify whether any redirection occurred. The url attribute can be used for a similar purpose:

`linkRequest.geturl()  # linkRequest.url`{{execute}}

_method returns a HTTP method; GET is the default response:

`linkRequest._method`{{execute}}

getheaders() returns a list with tuples that contains HTTP headers. As we can see from the following code, we can determine values regarding cookie, content type, date, and so on from the output:

`linkRequest.getheaders()`{{execute}}

```
[('Date','Sun, 30 Dec 2018 07:00:25 GMT'),('Expires', '-1'),('Cache-Control','private, max-age=0'),('Content-Type','text/html; charset=ISO-8859-1'),('P3P', 'CP="This is not a P3P policy! See g.co/p3phelp for more info."'),('Server', 'gws'),('X-XSS-Protection', '1; mode=block'),('X-Frame-Options','SAMEORIGIN'),('Set-Cookie', '1P_JAR=…..; expires=Tue, 29-Jan-2019 07:00:25 GMT; path=/; domain=.google.com'),('Set-Cookie 'NID=152=DANr9NtDzU_glKFRgVsOm2eJQpyLijpRav7OAAd97QXGX6WwYMC59dDPe.; expires=Mon, 01-Jul-2019 07:00:25 GMT; path=/; domain=.google.com; HttpOnly'),('Alt-Svc', 'quic=":443"; ma=2592000; v="44,43,39,35"'),('Accept-Ranges', 'none'),('Vary', 'Accept-Encoding'),('Connection', 'close')] 
```
