In this example, we will automate the browser to process the category and pagination link from the main URL provided. We are interested in extracting details from the Food and Drink category across multiple pages from http://books.toscrape.com/index.html.

An individual page from the category contains listings of products (Books), with certain information listed as follows:

- **title:** Title of the book listed
- **titleLarge:** Title of the book listed (complete title, found as a value to the title  attribute) 
- **price:** Listed book price 
- **stock:** Stock information relating to the listed book
- **image:** URL of book image
- **starRating:** Rating (number of stars found)
- **url:** URL of each listed book.

A similar example was also shown in Chapter 3, Using LXML, XPath and CSS Selectors in the section named Web Scraping Using LXML, under the name Example 2 – Looping with XPath and scraping data from multiple pages. There, we used the Python library lxml.  
With selenium.webdriver imported and the Chrome driver path set up, let's start loading http://books.toscrape.com/index.html. As the main page gets loaded, we will see various categories appear, listed one below the other.

The targeted category contains the text Food and Drink, and can be found using find_element_by_link_text() (we can use any applicable find_element... methods to find the particular category). The element found is processed further with click()—clicking on the element returned. This action will load the particular category URL in the browser:

```
driver.get('http://books.toscrape.com/index.html')

driver.find_element_by_link_text("Food and Drink").click()
print("Current Page URL: ", driver.current_url)
totalBooks = driver.find_element_by_xpath("//*[@id='default']//form/strong[1]")
print("Found: ", totalBooks.text)
```

To deal with multiple pages that are found during  iteration, NoSuchElementException from selenium.common.exceptions will be imported:

```
from selenium.common.exceptions import NoSuchElementException
```

As we will be using the pagination button next, NoSuchElementException will be helpful in dealing with the condition if no further next or pages are found. 

As seen in the following code, the pagination option next is located in the page and processed with the click() action. This action will load the URL it contains to the browser, and the iteration will continue until next is not located or found in the page, caught by the except block in the code:

```
try:
    #Check for Pagination with text 'next'
    driver.find_element_by_link_text('next').click()
    continue
except NoSuchElementException:
    page = False
```

The complete code for this example is already there. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter08/seleniumBooks.py` to view python code file.
