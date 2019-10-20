In this section, we will use and introduce various properties for webdriver and webdriver.Chrome, while looking at some real cases. The following sections will illustrate the use of Selenium and explore its major properties.

#### Accessing browser properties
In this section, we will demonstrate the use of Selenium and Chrome WebDriver to load Google Chrome with URLs and access certain browser-based features.

Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `web-scraping-with-python/Chapter08/seleniumBrowser.py` to view python code file.


To begin with, let's import webdriver from selenium and set a path to chromedriver.exe—let's call it chromedriver_path. The path created will be required to load Google Chrome. Depending on the application location, the complete path to chromedriver.exe should be mentioned, and is required for successful implementation:

```
from selenium import webdriver
import re

#setting up path to 'chromedriver.exe'
chromedriver_path='chromedriver'
```

The selenium.webdriver is used to implement various browsers, in this case, Google Chrome. The webdriver.Chrome() phrase is provided with the path of Chrome WebDriver so that chromedriver_path can be used for execution.

The phrase driver, which is an object of the selenium.webdriver.chrome.webdriver.WebDriver class, is created using webdriver.Chrome(), which will now provide access to the various attributes and properties from webdriver:

```
driver = webdriver.Chrome(executable_path=chromedriver_path)
```

The get() phrase accepts the URL that is to be loaded on the browser. Let's provide https://www.python.org as an argument to get(); the browser will start loading the URL, as shown in the following screenshot:

```
driver.get('https://www.python.org')
```

As you can see in the following screenshot, a notice is displayed just below the address bar with the message Chrome is being controlled by automated test software. This message also confirms the successful execution of the selenium.webdriver activity, and it can be provided with further codes to act on or automate the page that has been loaded:   



Upon successful loading of the page, we can access and explore its properties using driver. To illustrate this, let's extract or print the title from the HTML `<title>` tag and print the current URL that is accessible:

```
print("Title: ",driver.title) #print <title> text
Title:  Welcome to Python.org

print("Current Page URL: ",driver.current_url) #print current url, loaded in the browser
```

As seen in the preceding code, the page title is available using driver.title, and the current page URL is found with driver.current_url. The current_url phrase can be used to verify whether any URL redirection has taken place after loading the initial URL. Let's save a page screenshot with a condition that is verified using search() from the Python library, re:

```
#check if pattern matches the current url loaded

if re.search(r'python.org',driver.current_url):
    driver.save_screenshot("pythonorg.png") #save screenshot with provided name
    print("Python Screenshot Saved!")
```

The save_screenshot() phrase is provided with the filename as an argument for the image, and it creates a PNG image. The image will be saved at the current code location; the full destination or desired path can also be provided.
