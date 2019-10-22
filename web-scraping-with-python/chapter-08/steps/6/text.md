For the successful implementation of browser automation and application testing using Selenium, WebDriver needs to be set up. Let's go through the following steps to set up WebDriver for Google Chrome:

#### Install Selenium

`pip install selenium`{{execute}}

#### Download WebDriver for Google Chrome
`wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip`{{execute}}

`unzip chromedriver_linux64.zip`{{execute}}

**Note:** YOu also do that by following steps on your system:

- Visit https://www.seleniumhq.org/:
- Click Download (or browse to https://www.seleniumhq.org/download/).
- Under the Third Party Drivers, Bindings, and Plugins section, click `Google Chrome Driver`

#### Install Google Chrome

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`{{execute}}

`apt-get update`{{execute}}
 
`dpkg -i google-chrome-stable_current_amd64.deb`{{execute}}

`apt-get -f -y install`{{execute}}
 
`dpkg -i google-chrome-stable_current_amd64.deb`{{execute}}
