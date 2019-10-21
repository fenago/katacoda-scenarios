Now, let's extract information that's relevant to the URL by using category. The r'.*category' Regex pattern, which matches url from the iteration, is collected or appended to datasetCategoryURL. categoryTitle is extracted from url that matches the `r'category/([\w\s\-]+)` pattern and is added to dataSetCategory:

```
if re.match(r'.*category', url): #Category Related
    dataSetCategoryURL.append(url)
    categoryTitle = re.findall(r'category/([\w\s\-]+)', url)
    dataSetCategory.append(categoryTitle[0])

print("Category URL Count: ", len(dataSetCategoryURL))
print(dataSetCategoryURL)
```

Finally, the following output displays the title that was retrieved from dataSetCategory, as well as its counts:

```
print("Category Title Count: ", len(dataSetCategory))
print("Unique Category Count: ", len(set(dataSetCategory)))
print(dataSetCategory)
#returns unique element from List similar to dataSetCategory.
#print(set(dataSetCategory)) 
```

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter09/regex_xml.py` to view python code file.


#### Run Code
Now, run the python code by running: `python regex_xml.py`{{execute}}

From these example cases, we can see that, by using Regex, we can write patterns that target specific data from sources such as web pages, HTML, or XML.

Regex features such as searching, splitting, and iterating can be implemented with the help of various functions from the re Python library. Although Regex can be implemented on any type of content, unstructured content is preferred. Structured web content with elements that carry attributes are preferred when using XPath and CSS selectors.
