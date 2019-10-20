In this section, we will be requesting APIs and collecting the required data through them. Technically, data that's obtained through an API isn't similar to performing a scraping activity since we can't only extract data that's required from the API and process it further.

#### Example 1 – searching and collecting university names and URLs
In this example, we will be using an API provided by HIPO (https://hipolabs.com/) to search for universities: http://universities.hipolabs.com/search?name=Wales.

This API uses a query parameter called name, which will look for a university name. We will also provide an additional parameter, country, with country names such as United States, and United Kingdom. This API can be requested from the following URLs, while more information can be found at https://github.com/hipo/university-domains-list:

```
http://universities.hipolabs.com

http://universities.hipolabs.com/search?name=Wales

http://universities.hipolabs.com/search?name=Medicine&country=United Kingdom
```

Let's import the required libraries and use the readUrl() function to request the API and return the JSON response, as shown in the following code:

```
import requests
import json
dataSet = []

def readUrl(search):
    results = requests.get(url+search)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    return results.json()
```

With the JSON response returned, the required values can be retrieved with the keys and index that we have found, as shown in the following screenshot:


**JSON (formatted) obtained from the API**
name and url are traversed and appended to dataSet:

```
url = 'http://universities.hipolabs.com/search?name='
jsonResult = readUrl('Wales') # print(jsonResult)

for university in jsonResult:
    name = university['name']
    url = university['web_pages'][0]
    dataSet.append([name,url])

print("Total Universities Found: ",len(dataSet))
print(dataSet)
```

The final output is as follows:

```
Status Code: 200
Headers: Content-Type: application/json
Total Universities Found: 10

[['University of Wales', 'http://www.wales.ac.uk/'],
['University of Wales Institute, Cardiff', 'http://www.uwic.ac.uk/'], 
......., 
['University of Wales, Lampeter', 'http://www.lamp.ac.uk/'],
['University of Wales, Bangor', 'http://www.bangor.ac.uk/']]
```

#### Run Code
Now, run the python code by running: `python universities.py`{{execute}}