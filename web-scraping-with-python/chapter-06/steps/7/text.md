In this section, we will be exploring a task that's used to process basic user authentication, which is available from http://testing-ground.scraping.pro/login. User authentication is often processed with a unique combination of information, such as username, password, email, and so on, to identify the user on the website. 

The code in this section deals with logging in and changing the login credentials, as well as with obtaining the respective messages from the page. 

As we can see in the following screenshot, the HTML `<form>` exists with two `<input>` boxes that accept the username and password (that is, the login credentials) that are required to login. Login credentials are private and secure information, but for this particular testing site, the values are visible, predefined, and provided—namely, Username = "admin" and Password = "12345":


#### Login page
To process logging in with these credentials on http://testing-ground.scraping.pro/login, we need to find the `<form>` attributes—that is, action and method—that were used on the page to process the entered credentials. As we can see, the HTTP POST method will be applied to perform form submission on http://testing-ground.scraping.pro/login?mode=login: 



Inspecting `<form>` elements
Let's move on and set up the code. The pyquery and requests libraries need to be imported and the required URLs need to be collected so that they can be used:

```
from pyquery import PyQuery as pq
import requests
mainUrl = "http://testing-ground.scraping.pro"
loginUrl = "http://testing-ground.scraping.pro/login"
logoutUrl = "http://testing-ground.scraping.pro/login?mode=logout"
postUrl="http://testing-ground.scraping.pro/login?mode=login"
```

As shown in the following code, the responseCookies() function will accept response objects that are obtained from requests.get() before printing the headers and cookies information. Similarly, the processParams() function accepts `<form>`-based parameters that will be posted and prints the message that's obtained from the page:

```
def responseCookies(response):
    headers = response.headers
    cookies = response.cookies
    print("Headers: ", headers)
    print("Cookies: ", cookies)

def processParams(params):
    response = requests.post(postUrl, data=params)
    responseB = pq(response.text)
    message = responseB.find('div#case_login h3').text()
    print("Confirm Login : ",message)

if __name__ == '__main__': 
    requests.get(logoutUrl)

    response = requests.get(mainUrl)
    responseCookies(response)
    
    response = requests.get(loginUrl)
    responseCookies(response)
```

Now, let's request logoutUrl to clean the cookies and sessions, if they exist. Alternatively, for a completely new process, we can request mainUrl and loginUrl, respectively, and check the message that was received from responseCookies(). Here is the output:

```
Headers:{'Vary':'Accept-Encoding','Content-Type':'text/html','Connection':'Keep-Alive', ..........., 'Content-Encoding':'gzip','X-Powered-By':'PHP/5.4.4-14+deb7u12'}
Cookies: <RequestsCookieJar[]>

Headers:{'Vary':'Accept-Encoding','Content-Type':'text/html','Connection':'Keep-Alive',.............., 'Set-Cookie':'tdsess=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT',........., 'Keep-Alive':'timeout=5, max=100','X-Powered-By':'PHP/5.4.4-14+deb7u12'}
Cookies: <RequestsCookieJar[]>
```

As shown in the preceding output, cookies is empty for both mainUrl and loginUrl and no other unique header pairs are available except Set-Cookie, with a value of tdsess=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT from loginUrl. 

Now that responseA from the loginUrl `<form>` elements attribute name has been collected as username and password, this information will be used to create the paramsCorrect and paramsIncorrect parameter strings, which will be posted to postUrl:

```
responseA = pq(response.text)
username = responseA.find('input[id="usr"]').attr('name')
password = responseA.find('input[id="pwd"]').attr('name')

#Welcome : Success
paramsCorrect = {username: 'admin', password: '12345'} #Success
print(paramsCorrect)
processParams(paramsCorrect)
```

A successful form submission with the provided paramsCorrect parameter string will result in the following output:

```
{'pwd': '12345', 'usr': 'admin'}
Confirm Login : WELCOME :)
```

The preceding output is extracted from the response of postUrl, which in this test case is actually a redirected page with a URL of http://testing-ground.scraping.pro/login?mode=welcome:


![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-06/steps/7/1.png)

