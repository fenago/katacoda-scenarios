
We will be using the requests library and accessing some of its properties. The get() function from requests is used to send a GET HTTP request to the URL provided. The object that's returned is of the requests.model.Response type, as shown in the following code:

`import requests`{{execute}}

`link="http://www.google.com"`{{execute}}

`r = requests.get(link)`{{execute}}

`dir(r)`{{execute}}

`print(type(r))`{{execute}}

The requests library also supports HTTP requests such as PUT, POST, DELETE, HEAD, and OPTIONS using the put(), post(), delete(), head(), and options() methods, respectively.

The following are some requests attributes, along with a short explanation of each:

- url outputs the current URL
- The HTTP status code is found using status_code
- history is used to track redirection:

`r.url #URL of response object`{{execute}}

`r.status_code #status code`{{execute}}

`r.history #status code of history event`{{execute}}

We can also obtain some details that are found when we use developer tools, such as HTTP Header, Encoding, and so on:

- headers returns response-related HTTP headers
- requests.header returns request-related HTTP headers 
- encoding displays the charset that's obtained from the content:

`r.headers #response headers with information about server, date..`{{execute}}

```
{'Transfer-Encoding': 'chunked', 'Content-Type': 'text/html', 'Content-Encoding': 'gzip', 'Last-Modified': '....'Vary': 'Accept-Encoding', 'Server': 'nginx/1.14.0 (Ubuntu)', 'X-Cname-TryFiles': 'True', 'X-Served': 'Nginx', 'X-Deity': 'web02', 'Date': 'Tue, 01 Jan 2019 12:07:28 GMT'}
```

`r.headers['Content-Type'] #specific header Content-Type`{{execute}}

`r.request.headers  #Request headers`{{execute}}

`r.encoding  #response encoding`{{execute}}

Page or response content can be retrieved using the content in bytes, whereas text returns a str string:

`r.content[0:400]  #400 bytes characters`{{execute}}

`r.text[0:400]  #sub string that is 400 string character from response`{{execute}}

Furthermore, requests also returns a raw socket response from the server by using the stream argument in a get() request. We can read a raw response using the raw.read() function:

`r = requests.get(link,stream=True) #raw response`{{execute}}

`print(type(r.raw))   #type of raw response obtained`{{execute}}

`r.raw.read(100)  #read first 100 character from raw response`{{execute}}

A raw response that's received using the raw attribute is raw bytes of characters that haven't been transformed or automatically decoded.
requests handles JSON data very effectively with its built-in decoder. As we can see, URLs with JSON content can be parsed with requests and used as required:


```import requests
link = "https://feeds.citibikenyc.com/stations/stations.json"
response = requests.get(link).json()```{{execute}}

**Note:** Please press enter to run multiline code after clicking following:

```for i in range(10): #read 10 stationName from JSON response.
        print('Station ',response['stationBeanList'][i]['stationName'])```{{execute}}

```
Station W 52 St & 11 Ave
Station Franklin St & W Broadway
Station St James Pl & Pearl St
........
Station Clinton St & Joralemon St
Station Nassau St & Navy St
Station Hudson St & Reade St
```

**Note:**  that, requests uses urllib3 for session and for raw socket response.

Crawling the script might use any of the mentioned or available HTTP libraries to make web-based communications. Most of the time, functions and attributes from multiple libraries will make this task easy. In the next section, we will be using the requests library to implement the HTTP (GET/POST) methods.