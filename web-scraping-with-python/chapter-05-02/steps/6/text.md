
With the project successfully created, let's explore the individual components inside the project folder:

- scrapy.cfg is a configuration file in which default project-related settings for deployment are found and can be added.
- Subfolder will find Quotes named same as project directory, which is actually a Python module. We will find additional Python files and other resources in this module as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-05-02/steps/6/1.png)

As seen in the preceding screenshot, the module is contained in the spiders folder and the items.py, pipelines.py, and settings.py Python files. These content found inside the Quotes module has specific implementation regarding the project scope explored in the following list:

- **spiders:** This folder will contain Spider classes or Spider writing in Python. Spiders are classes that contain code that is used for scraping. Each individual Spider class is designated to specific scraping activities.
- **items.py:** This Python file contains item containers, that is, Python class files inheriting scrapy. Items are used to collect the scraped data and use it inside spiders. Items are generally declared to carry values and receive built-in support from other resources in the main project. An item is like a Python dictionary object, where keys are fields or objects of scrapy.item.Field, which will hold certain values.

Although the default project creates the items.py for the item-related task, it's not compulsory to use it inside the spider. We can use any lists or collect data values and process them in our own way such as writing them into a file, appending them to a list, and so on. 

- **pipelines.py:** This part is executed after the data is scraped. The scraped items are sent to the pipeline to perform certain actions. It also decides whether to process the received scraped items or drop them.
- **settings.py:** This is the most important file in which settings for the project can be adjusted. According to the preference of the project, we can adjust the settings. Please refer to the official documentation from Scrapy for settings at https://scrapy2.readthedocs.io/en/latest/topics/settings.html