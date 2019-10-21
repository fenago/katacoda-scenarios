In this example, we will be extracting contents from the sitemap.xml file, which can be downloaded from [here](https://webscraping.com/sitemap.xml)

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/11/1.png)

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter09/sitemap.xml` to view xml file.

By analyzing the XML content, we can see that different types of URLs exist as child nodes, that is, `<loc>`. From these URLs, we will be extracting the following:

- Blog URLs (URLs with a `/blog/` string, such as [webscraping](https://webscraping.com/blog/Why-Python/)
- Titles obtained from the blog URLs
- Category URLs (URLs with a `/category/` string, such as [webscraping](https://webscraping.com/blog/category/beautifulsoup)
- Category titles obtained from category URLs (beautifulsoup)

**Note:** Blog titles and category titles that are obtained from code are retrieved from the URL or representations of the real content that's available from the URL. Actual titles might be different. 

To begin with, let's import the re Python library and read the file's contents, as well as create a few Python lists in order to collect relevant data:

```
import re

filename = 'sitemap.xml'
dataSetBlog = [] # collect Blog title information from URLs except 'category'
dataSetBlogURL = [] # collects Blog URLs
dataSetCategory = [] # collect Category title
dataSetCategoryURL = [] # collect Category URLs

page = open(filename, 'r').read()
```

From the XML content, that is, page, we need to find the URL pattern. pattern used in code matches and returns all of the URLs inside the <loc> node. urlPatterns (<class 'list'>) is a Python list object that contains searched URLs and is iterated to collect and process the desired information:

```
#Pattern to be searched, found inside <loc>(.*)</loc>
pattern = r"loc>(.*)</loc"

urlPatterns = re.findall(pattern, page) #finding pattern on page

for url in urlPatterns: #iterating individual url inside urlPatterns
```

Now, let's match a url, such as https://webscraping.com/blog/Google-App-Engine-limitations/, which contains a blog string and append it to dataSetBlogURL. There are also few other URLs, such as https://webscraping.com/blog/8/, which will be ignored while we extract blogTitle. 

Also, any blogTitle that's found as text equal to category will be ignored. The r'blog/([A-Za-z0-9\-]+) pattern matches alphabetical and numerical values with the - character:

```
if re.match(r'.*blog', url): #Blog related
    dataSetBlogURL.append(url)
    if re.match(r'[\w\-]', url):
        blogTitle = re.findall(r'blog/([A-Za-z0-9\-]+)', url)
        
        if len(blogTitle) > 0 and not re.match('(category)', blogTitle[0]):
            #blogTitle is a List, so index is applied.
            dataSetBlog.append(blogTitle[0]) 
```

dataSetBlog will contain the following titles (URL portion). The set() method, when applied to dataSetBlog, will return unique elements from dataSetBlog. As shown in the following code,there's no duplicate title inside dataSetBlog:

```
print("Blogs Title: ", len(dataSetBlog))
print("Unique Blog Count: ", len(set(dataSetBlog)))
print(dataSetBlog)
#print(set(dataSetBlog)) #returns unique element from List similar to dataSetBlog.
```
