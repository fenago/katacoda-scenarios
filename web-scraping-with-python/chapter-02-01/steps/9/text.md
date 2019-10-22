We can use the decode() method to convert bytes into a string and the encode() method to convert a string into bytes, as shown in the following code:

`python`{{execute}}

`link="https://www.samsclub.com/sitemap.xml"`{{execute}} 

`import requests`{{execute}} 

`content = requests.get(link).text  #using 'text'`{{execute}} 

`content`{{execute}} 

`content = requests.get(link).content`{{execute}}

`content.decode() # decoding 'content' , decode('utf-8')`{{execute}} 

```
'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<sitemap><loc>https://www.samsclub.com/sitemap_categories.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_1.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_products_2.xml</loc></sitemap>\n<sitemap><loc>https://www.samsclub.com/sitemap_locators.xml</loc></sitemap>\n</sitemapindex>'
```

Identifying a proper character set or charset is important when dealing with various domains and type of documents. To identify a proper charset encoding type, we can seek help from the page source for the `<meta>` tag by using content-type or charset.

The `<meta>` tag with the charset attribute, that is, `<meta charset="utf-8"/>`, is identified from the page source.