Generally, web-based interaction or communication between the web page and the user or reader is achieved as follows:

The user or reader can access the web page to read or navigate through information that's presented to them
The user or reader can also submit certain information to the web page using the HTML form, such as by searching, logging in, user registration, password recovery, and so on
In this section, we will be using the requests Python library to implement common HTTP methods (GET and POST) that execute the HTTP-based communication scenario we listed previously.

#### GET
A command way to request information is to use safe methods since the resource state is not altered. The GET parameters, also known as query strings, are visible in the URL. They are appended to the URL using ? and are available as key=value pairs.

Generally, a processed URLs without any specified HTTP methods are normally GET requests. A request that's made using GET can be cached and bookmarked. There are also length restrictions while making a GET request. Some examples URLs are as follows:

- http://www.test-domain.com
- http://www.test-domain.com/indexes/
- http://www.test-domain.com/datafile?id=1345322&display=yes

In the preceding sections, requests were made to normal URLs such as robots.txt and sitemap.xml, both of which use the HTTP GET method. The get() function from requests accepts URLs, parameters, and headers:


`import requests`{{execute}}

`link="http://www.test-domain.com/"`{{execute}}

`queries= {'id':'123456','display':'yes'}`{{execute}}

`addedheaders={'user-agent':''}`{{execute}}

```#request made with parameters and headers
r = requests.get(link, params=queries, headers=addedheaders) 
print(r.url)```{{execute}}

This is the output of the preceding code:

```
http://www.test-domain.com/?id=123456&display=yes
```
