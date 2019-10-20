In this example, username and password are open string values, and test has been used for both:

```
responseA = pq(response.text)
csrf_token = responseA.find('input[name="csrf_token"]').attr('value')
username = responseA.find('input[id="username"]').attr('name')
password = responseA.find('input[id="password"]').attr('name')

params = {username: 'test', password: 'test', 'csrf_token': csrf_token}
print(params)
```

The form fields with the existing value and name are collected and params is configured, which results in the following output:

```
{'password':'test','username':'test','csrf_token':'jJgAHDQykMBnCFsPIZOoqdbflYRzXtSuiEmwKeGavVWxpNLUhrcT'}
```

The parameters to be submitted via a form action are built using the name attribute of the <form> element as a key and default, respectively, and is required to receive values as their value. 
The requests.post() phrase implements a HTTP POST request to loginURL with the params and customHeaders that have been setup. A customHeaders is created with the setCookie value that we received earlier:

```
customHeaders = getCustomHeaders(setCookie)
response = requests.post(loginUrl, data=params, headers=customHeaders)
setCookie = responseCookies(response)
#print("Set-Cookie: ",setCookie)

responseB = pq(response.text)
logoutText = responseB.find('a[href*="logout"]').text()
logoutLink = responseB.find('a[href*="logout"]').attr('href')

print("Current Page : ",response.url)
print("Confirm Login : ", responseB.find('.row h2').text())
print("Logout Info : ", logoutText," & ",logoutLink)
```

Finally, we receive a successful output, along with the redirected URL and information regarding the logout:

```
Current Page : http://quotes.toscrape.com/
Confirm Login : Top Ten tags
Logout Info : Logout & /logout
```

The following screenshot shows the successful authentication with the information verified:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-06/steps/11/3.png)

#### Run Code
Now, run the python code by running: `python toScrapeSessionCookie.py`{{execute}}