
To explore further, let's collect the web cookies from https://www.python.org. The get_cookies() phrase is used to retrieve cookies, as follows: 

```
#get cookie information
cookies = driver.get_cookies() 
print("Cookies obtained from python.org")
print(cookies)
```

The page source can be obtained using driver.page_source.

To obtain the page source manually, right-click on the page and click View page source, or press Ctrl + U:

```
print(driver.page_source) #page source
```

The page can be reloaded or refreshed using driver.refresh().


```
driver.refresh() #reload or refresh the browser
```

With the features that were accessed using driver in the preceding code, let's continue loading, taking screenshots, and accessing cookies from https://www.google.com using the following code:

```
driver.get('https://www.google.com')
print("Title: ",driver.title)
print("Current Page URL: ",driver.current_url)

if re.search(r'google.com',driver.current_url):
    driver.save_screenshot("google.png")
    print("Google Screenshot Saved!")

cookies = driver.get_cookies()
```

The action performed with http://google.com will take place on the same browser window that was used for accessing http://python.org. With this, we can now perform actions using the browser history (that is, we will use the Back and Forward buttons that are available in the web browser) and retrieve the URL, as shown in the following code:

```
print("Current Page URL: ",driver.current_url)

driver.back() #History back action
print("Page URL (Back): ",driver.current_url)

driver.forward() #History forward action
print("Page URL (Forward): ",driver.current_url)
```

In the preceding code, back() takes the browser back a page, whereas forward() moves it a step forward along the browser history. The output received is as follows:

```
Current Page URL: https://www.google.com/
Page URL (Back): https://www.python.org/
Page URL (Forward): https://www.google.com/
```

Following successful execution of the code, it is recommended that you close and quit the driver to free up system resources. We can perform the termination actions using the following functions:

```
driver.close() #close browser
driver.quit()  #quit webdriver
```

The preceding code contains the following two phrases:

- close() terminates the loaded browser window
- quit() ends the WebDriver application


#### Run Code
Now, run the python code by running: `python seleniumBrowser.py`{{execute}}

This code demonstrated the use of selenium.webdriver and its various properties. In the next section, we will demonstrate the use of webdriver and web elements (elements from the web page).
