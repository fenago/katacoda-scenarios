**Selenium projects**

Selenium consists of multiple components or tools that are also known as Selenium projects, which makes it a complete framework for web-based application testing. We will now look at some of the major components of these Selenium projects. 

**Selenium WebDriver**

Selenium WebDriver is a component of Selenium that is used to automate the browser. Automating the browser can be conducted by providing commands with various language bindings available for Java, Python, JavaScript, and so on by using third-party drivers such as Google Chrome driver, Mozilla Gecko driver, and Opera (https://github.com/mozilla/geckodriver/). Selenium WebDriver has no external dependency on any other software or servers.

WebDriver is an object-oriented API with updated features that overcomes and addresses the limitations of previous Selenium versions and Selenium Remote Control (RC). Please visit the Selenium WebDriver web page (https://www.seleniumhq.org/projects/webdriver/) for more information.

**Selenium RC**

Selenium RC is a server that is programmed in Java. It uses HTTP to accept commands for the browser and is used to test complex AJAX-based web applications.

Selenium RC has been officially deprecated following the release of Selenium 2 (Selenium version 2). However, WebDriver contains the major features of Selenium RC. Please visit https://www.seleniumhq.org/projects/remote-control/ for more information. 
Selenium Grid
Selenium Grid is also a server that allows tests to run parallel on multiple machines across multiple browsers and operating systems, distributing the system load and cutting down performance issues, such as time consumption. 

Complex tests were used to process Selenium RC and Selenium Grid together. Since the release of version 2.0, the Selenium server now has built-in support for WebDriver, Selenium RC, and Selenium Grid. Please visit the Selenium Grid [web page](https://www.seleniumhq.org/projects/grid/) for more information. 

**Selenium IDE**

An open source Selenium integrated development environment (IDE) is used to build test cases with Selenium. It's basically a web browser extension available with features such as the ability to record and play back web automation through a graphical user interface (GUI).

The following are a few key features of the Selenium IDE:

- Extendable and easy to use for debugging
- Resilient tests
- Cross-browser support
- Can create scripts that can run commands and support control-flow structures

Please visit the Selenium IDE [web page](https://www.seleniumhq.org/selenium-ide/) for more information and installation procedures. Please visit the Selenium projects web page (https://www.seleniumhq.org/projects/) for more information on Selenium components.

Now that we know what Selenium is used for and some of its major components, let's look at how we can install and perform general tests using Selenium WebDriver.