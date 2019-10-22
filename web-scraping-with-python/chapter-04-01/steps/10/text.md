In this section, we will be demonstrating the iterating (perform repeatedly) facility that's available with pyquery. It's effective and easy to process in many situations.

In the following code, we are searching for the name and property attributes that are found in the <meta> tags that contain the word Python.org. We are also using Python's List Comprehension technique to demonstrate the one-line coding feature:

`meta=page.find('meta[content*="Python.org"]')`{{execute}}

`print(meta)`{{execute}}

```
[item.attr('name') for item in meta.items() if item.attr('name') is not None]
['application-name', 'apple-mobile-web-app-title']
```

Continuing from code above list value for attribute 'property'

`[item.attr('property') for item in meta.items() if item.attr('property') is not None]`{{execute}}

As we can see in the preceding code, we are using the items() function in a loop with the element meta to iterate for the provided option. An expression resulting in iterable objects can be explored using items(). Results that return None are excluded from the list:

`social = page.find('a:contains("Socialize") + ul.subnav li a') `{{execute}}

`[item.text() for item in social.items() if item.text() is not None]`{{execute}}

`[item.attr('href') for item in social.items() if item.attr('href') is not None]`{{execute}}

```
['https://plus.google.com/+Python', 'https://www.facebook.com/pythonlang?fref=ts', 'https://twitter.com/ThePSF', '/community/irc/']
```

`webdevs = page.find('div.applications-widget:first ul.menu li:contains("Web Development") a')`{{execute}}

`[item.text() for item in webdevs.items() if item.text() is not None]`{{execute}}

```
['Django', 'Pyramid', 'Bottle', 'Tornado', 'Flask', 'web2py']
```

In the preceding code, the pyquery object collects the names and links that are available from the social and web development section. These can be found under Use Python for... in the following screenshot. The object is iterated using the Python list comprehension technique:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-04-01/steps/10/1.png)
