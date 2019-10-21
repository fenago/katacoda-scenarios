Let's clear the text inside searchBox and input the text Dress to be searched. We also need to submit the button located on the right-hand side of the searchBox and click it to execute the search using the WebElement method, click():

```
searchBox.clear() 
searchBox.send_keys("Dress")
submitButton = driver.find_element_by_name("submit_search")
submitButton.click()
```

The browser will process the search action for the submitted text Dress and load the results page.

Now that the search action is complete, to verify the successful search, we will extract information regarding the product numbers and count using the following code:

```
#find text or provided class name
resultsShowing = driver.find_element_by_class_name("product-count")
print("Results Showing: ",resultsShowing.text) 

#find results text using XPath
resultsFound = driver.find_element_by_xpath('//*[@id="center_column"]//span[@class="heading-counter"]')
print("Results Found: ",resultsFound.text)
```

With the number of items and the count of the products that were found, this conveys a successful message to our search process. Now, we can proceed with looking for products using XPath, CSS selectors, and so on:

```
#Using XPath
products = driver.find_elements_by_xpath('//*[@id="center_column"]//a[@class="product-name"]')

#Using CSS Selector
#products = driver.find_elements_by_css_selector('ul.product_list li.ajax_block_product a.product-name')

foundProducts=[]
for product in products:
    foundProducts.append([product.text,product.get_attribute("href")])
```

From the preceding code,  products obtained is iterated and an individual item is added to the Python list foundProducts. product is an object of WebElement, in other words, selenium.webdriver.remote.webelement.WebElement,  while properties are collected using text and get_attribute():

```
print(foundProducts) 
```

In this section, we explored the various properties and methods from selenium.webdriver that are used to deal with the browser, use HTML forms, read page content, and so on. Please visit https://selenium-python.readthedocs.io for more detailed information on Python Selenium and its modules. In the next section, we will use most of the methodologies that were used in the current section to scrape information from a web page.


#### Run Code
Now, run the python code by running: `python seleniumLocator.py`{{execute}}

