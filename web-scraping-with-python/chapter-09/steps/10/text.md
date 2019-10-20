
We will now proceed with loading the page source for the desired URL and implementing Regex to find data:

```
dataSet=list() #collecting data extracted
sourceUrl = 'http://godfreysfeed.com/dealersandlocations.php'
page = read_url(sourceUrl) #load sourceUrl and return the page source
```

With the page source obtained from read_url(), let's do a basic analysis and build a pattern to collect latitude and longitude information. We will need two distinct patterns for the dealer's address and coordinate values, respectively. Output from both patterns can be combined to obtain the final results:

```
#Defining pattern matching latitude and longitude as found in page.
pLatLng= r'var latLng = new google.maps.LatLng\((?P<lat>.*)\,\s*(?P<lng>.*)\)\;'

#applying pattern to page source
latlngs = re.findall(pLatLng,page) 
print("Findall found total LatLngs: ", len(latlngs))

#Print coordinates found
print(latlngs)
```

Now that we have the dealer's coordinates, let's find out the dealer's name, address, and more: 

```
#Defining pattern to find dealer from page.
pDealers = r'infoWindowContent = infoWindowContent\+\s*\"(.*?)\"\;'

#applying dealers pattern to page source
dealers = re.findall(pDealers, page)
print("Findall found total Address: ", len(dealers))

#Print dealers information found
print(dealers)
```

There was also a total of 55 pieces of address-based information, which was found by using the pDealers pattern. **Note:**  that the dealer's content is in HTML format and that further implementation of Regex will be required to obtain individual titles such as name, address, and city.

Now that we have results from both latlngs and dealers, let's collect the individual portions of the dealer's address. Raw data for the dealers contains some HTML tags, and has been used to split and clean the dealer's address information. Since re.findall() returns the Python list, indexing can also be useful for retrieving address components:

```
d=0 #maintaining loop counter  
for dealer in dealers:
    dealerInfo = re.split(r'<br>',re.sub(r'<br><br>','',dealer))
    
    #extract individual item from dealerInfo
    name = re.findall(r'\'>(.*?)</span',dealerInfo[0])[0]
    address = re.findall(r'>(.*)<',dealerInfo[1])[0]
    city = re.findall(r'>(.*),\s*(.*)<',dealerInfo[2])[0][0]
    state = re.findall(r'>(.*),\s*(.*)<',dealerInfo[2])[0][1]
    zip = re.findall(r'>(.*)<',dealerInfo[3])[0]
    lat = latlngs[d][0]
    lng = latlngs[d][1]
    d+=1
    
    #appending items to dataset
    dataSet.append([name,address,city,state,zip,lat,lng])

print(dataSet)  #[[name,address, city, state, zip, lat,lng],]
```

#### Run Code
Now, run the python code by running: `python godfreysfeed.py`{{execute}}

Finally, dataSet will contain an individual dealer's information that's been merged from dealers and latlngs in the listing:

```
[['Akins Feed & Seed', '206 N Hill Street', 'Griffin', 'GA', '30223', '33.2509855', '-84.2633946'], ['Alf&apos;s Farm and Garden', '101 East 1st Street', 'Donalsonville', 'GA', '39845', '31.0426107', '-84.8821949'],...................................., 
['Twisted Fitterz', '10329 Nashville Enigma Rd', 'Alapaha', 'GA', '31622', '31.3441482', '-83.3002373'], 
['Westside Feed II', '230 SE 7th Avenue', 'Lake Butler', 'FL', '32054', '30.02116', '-82.329495'],
['White Co. Farmers Exchange', '951 S Main St', 'Cleveland', 'GA', '30528', '34.58403', '-83.760829']]
```

In this example, we tried to extract data using different patterns and retrieved a dealer's information from the URL provided.