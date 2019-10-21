These are known as secure requests that are made to a source. The requested resource state can be altered. Data that's posted or sent to the requested URL is not visible in the URL; instead, it's transferred to the request body. A request that's made using POST isn't cached or bookmarked and has no restrictions in terms of length.

In the following example, a simple HTTP request and response service (source: http://httpbin.org/) has been used to make a POST request.

pageUrl accepts data to be posted, as defined in params to postUrl. Custom headers are assigned as headers. The post() function from the requests library accepts URLs, data, and headers, and returns a response in JSON format:


```import requests
pageUrl="http://httpbin.org/forms/post"
postUrl="http://httpbin.org/post"```{{execute}} 

```params = {'custname':'Mr. ABC','custtel':'','custemail':'abc@somedomain.com','size':'small',
'topping':['cheese','mushroom'],'delivery':'13:00','comments':'None'}```{{execute}}

```headers={ 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Content-Type':'application/x-www-form-urlencoded',
'Referer':pageUrl
}```{{execute}}


```#making POST request to postUrl with params and request headers, response will be read as JSON
response = requests.post(postUrl,data=params,headers=headers).json()
print(response)```{{execute}}

The previous code will result in the following output:

```
{
'args': {}, 
'data': '', 
'files': {}, 
'form': {
'comments': 'None', 
'custemail': 'abc@somedomain.com',
'custname': 'Mr. ABC', 
'custtel': '',
'delivery': '13:00', 
'size': 'small', 
'topping': ['cheese', 'mushroom']
}, 
'headers': {    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 
'Connection': 'close', 
'Content-Length': '130', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': 'httpbin.org', 
'Referer': 'http://httpbin.org/forms/post', 
'User-Agent': 'python-requests/2.21.0'
}, 
'json': None, 'origin': '202.51.76.90', 
'url': 'http://httpbin.org/post'
}
```

It's always beneficial to learn and detect the request and response sequences that are made with URLs through the browser and the available DevTools.