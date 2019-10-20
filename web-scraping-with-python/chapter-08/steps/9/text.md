
In this section, we will perform a search on http://automationpractice.com to obtain a list of products that match the search query, illustrating the use of selenium.webdriver. Web elements are elements that are listed in a web page or that are found in a page source. We also look at a class called WebElement, used as selenium.webdriver.remote.webelement.WebElement.

The automation practice [website](http://automationpractice.com/) is a sample e-commerce website from [selenium](http://www.seleniumframework.com) that you can use for practice.

To begin with, let's import webdriver from selenium, set a path to chromedriver.exe, create an object of webdriver—that is, driver, as implemented in the previous section, Accessing browser properties—and load the URL, http://automationpractice.com:

```
driver.get('http://automationpractice.com')
```

The new Google Chrome window will be loaded with the URL provided. Find the search (input) box just above Cart, as shown in the following screenshot: 

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-08/steps/9/1.png)

**Note:** We will run chrome in a headless mode in the lab environments. You will not see this.

To continue searching through the script, we need to identify the element with the HTML `<input>`.

In our case, the search box can be identified by the attributes shown in the preceding screenshot, or even by using the XPath or CSS selectors:

- id="search_query_top"
- name="search_query"
- class="search_query" 

The selenium.webdriver provides lots of locators (methods that are used to locate elements) that can be applied conveniently as applicable to the cases encountered.
