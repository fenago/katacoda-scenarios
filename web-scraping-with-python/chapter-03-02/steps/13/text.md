So, we can perform a loop with `li[position()>0]` that identifies each `<article>` field found inside `<li>` until it exists in `<ol>` with its traced position, that is:

`articles = XPath("//*[@id='default']//ol/li[position()>0]")`

```
#looping through 'articles' found in 'doc' i.e each <li><article> found in Page Source
for row in articles(doc): 
     title = titlePath(row)[0]
     price = pricePath(row)[0]
     availability = stockPath(row)[0].strip()
     image = imagePath(row)[0]
     rating = starRating(row)[0]
     
     #cleaning and formatting applied to image and rating
     dataSet.append([title,price,availability,image.replace('../../../..',baseUrl),rating.replace('star-rating','')])

page+=1 #updating Page Count for While loop

#Final Dataset with data from all pages. 
print(dataSet)
```

#### Run Code
Now, run the python code by running: `python scrapeXPathLoop.py`{{execute}}

Individual elements of the XPath expression are defined as the titlePath element, the imagePath element, and so on, targeting particular elements whose data is to be obtained. Finally, the expression set for articles is looped into the HTMLElement obtained for each page, that is, the doc element and collects the first occurrence of each title and image element and the other elements found. These collected data are appended to the dataSet field as a list with the cleaning and formatting done, which results in the output shown in the following screenshot:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-02/steps/13/1.JPG)

