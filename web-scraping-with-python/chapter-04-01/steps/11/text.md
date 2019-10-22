
In the following code, we will be exploring a few more details that were retrieved from the upcomingevents iteration:


`eventsList = []`{{execute}}

`upcomingevents = page.find('div.event-widget ul.menu li')`{{execute}}

**Note:** Please press enter to run multiline code after clicking following:

```for event in upcomingevents.items():
     time = event.find('time').text()
     url = event.find('a[href*="events/python"]').attr('href')
     title = event.find('a[href*="events/python"]').text()
     eventsList.append([time,title,url])```{{execute}}

`eventsList`{{execute}}

eventsList contains extracted details from Upcoming Events, as shown in the preceding screenshot. The output from eventsList is provided here:

```
[['2019-02-19', 'PyCon Namibia 2019', '/events/python-events/790/'], ['2019-02-23', 'PyCascades 2019', '/events/python-events/757/'],
['2019-02-23', 'PyCon APAC 2019', '/events/python-events/807/'], ['2019-02-23', 'Berlin Python Pizza', '/events/python-events/798/'],
['2019-03-15', 'Django Girls Rivers 2019 Workshop', '/events/python-user-group/816/']]
```

DevTools can be used to identify a CSS selector for the particular section and can be further processed with the looping facility.
The following code illustrates a few more examples of the pyquery iterating process via the use of find() and items():


`buttons = page.find('a.button')`{{execute}}

```for item in buttons.items():
     print(item.text(),' :: ',item.attr('href'))```{{execute}}
 
`buttons = page.find('a.button:odd')`{{execute}}

```for item in buttons.items():
    print(item.text(),' :: ',item.attr('href'))```{{execute}}

 
`buttons = page.find('a.button:even')`{{execute}}

```for item in buttons.items():
    print(item.text(),' :: ',item.attr('href'))```{{execute}}
