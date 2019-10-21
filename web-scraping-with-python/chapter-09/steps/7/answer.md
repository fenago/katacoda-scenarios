Now, let's use requests:


>>> import requests
>>> link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
>>> response = requests.get(link)

>>> print(type(response))
    <class 'requests.models.Response'>

>>> content = response.content #response content received
>>> print(content[0:150])  #print(content) printing first 150 character from content

b'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title>List of most popular websites - Wikipedia</title>'
Here, we are using the requests module to load the page source, just like we did using urllib. requests with the get() method, which accepts a URL as a parameter. The response type for both examples has also been checked.


In the preceding examples, the page content—or the response object—contains the details we were looking for, that is, the Site, Domain, and Type columns.

We can choose any one library to deal with the HTTP request and response. Detailed information on these two Python libraries with examples is provided in the next section, URL handling and operations with urllib and requests.

Let's have a look at the following screenshot:

