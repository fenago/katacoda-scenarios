Selenium is used to test web applications. It is mostly used to perform browser automation using various programming language-based libraries and browser drivers. As we saw in a previous section, Exploring Selenium, we can navigate and locate elements in a page using Selenium and perform crawling and scraping-related activities. 

Let's look at a few examples of scraping contents from web pages using Selenium.

#### Example 1 – scraping product information
In this example, we will continue using the search results obtained from foundProducts in the Exploring Selenium section. 

We will extract some specific information from each individual product link found in foundProducts, listed as follows:

product_name : Product name
product_price: Listed price
image_url: URL of product's main image  
item_condition: Condition of product  
product_description: Short description of product
Each individual product link from foundProducts is loaded using driver.get():

```
dataSet=[]
if len(foundProducts)>0:
   for foundProduct in foundProducts:
       driver.get(foundProduct[1])

       product_url = driver.current_url
       product_name = driver.find_element_by_xpath('//*[@id="center_column"]//h1[@itemprop="name"]').text
       short_description = driver.find_element_by_xpath('//*[@id="short_description_content"]').text
       product_price = driver.find_element_by_xpath('//*[@id="our_price_display"]').text
       image_url = driver.find_element_by_xpath('//*[@id="bigpic"]').get_attribute('src')
       condition = driver.find_element_by_xpath('//*[@id="product_condition"]/span').text
       dataSet.append([product_name,product_price,condition,short_description,image_url,product_url])
   
print(dataSet)
```

Targeted fields or information to be extracted are obtained using XPath, and are appended to the dataSet.

Finally, system resources are kept free using close() and quit(). The complete code for this example is listed as follows:
