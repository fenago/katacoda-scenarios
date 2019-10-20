In this section, we will be exploring various APIs that are available on the web, send requests to them, and receive responses, before explaining how they work via the Python programming language.

Let's consider the following sample URL, https://www.someexampledomain.com. The API it provides comes with parameters, locators, and authentication. By using these, we can access the following resources:

- https://api.someexampledomain.com 
- https://api.someexampledomain.com/resource?key1=value1&key2=value2
- https://api.someexampledomain.com/resource?api_key=ACCESS_KEY&key1=value1&key2=value2
- https://api.someexampledomain.com/resource/v1/2019/01

Parameters or collections of key-value pairs are actually sets of predefined variables that are provided by the web. Usually, the API provides some sort of documentation or basic guidelines regarding its usage, HTTP methods, available keys and types, or permitted values that the key can receive, along with other information on the features that are supported by the API, as shown in the following screenshot: 

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-07/steps/6/1.png)

End users and systems can only use the API with the features and functions that the provider permits.
