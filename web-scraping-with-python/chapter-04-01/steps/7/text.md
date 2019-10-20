pyquery has a large set of attributes and methods that can be deployed to obtain the desired content. In the following examples, we'll identify the implementation from the code that's found in this section:


`page('title') #find element <title>`{{execute}}


`page.find('title').text() #find element <title> and return text content`{{execute}}


`page.find('meta[name="description"]').attr('content')`{{execute}}

`page.find('meta[name="keywords"]').attr('content')`{{execute}}


`buttons = page('a.button').html() #return HTML content for element <a> with class='button'`{{execute}}

`buttons`{{execute}}

The following are a few of their functions, along with a description, that can be seen in the preceding code:

- find(): Searches the provided element or evaluates the query expression build using CSS selectors
- text(): Returns the element content as a string
- attr(): Identifies the attribute and returns its content
- html(): Returns the HTML content of the evaluated expression
 
The class and id CSS attributes are represented with . and #, respectively, and are prefixed to the attribute's value. For example, `<a class="main" id="mainLink">` will be identified as a.main and a#mainLink.
In the following code, we are listing all the identified `<ul>` elements with the class attribute and the menu value:

`page('ul.menu') #<ul> element with attribute class='menu'`{{execute}}

```
[<ul.menu>, <ul.navigation.menu>, <ul.subnav.menu>, <ul.navigation.menu>, <ul.subnav.menu>, <ul.navigation.menu>,..............,<ul.subnav.menu>, <ul.footer-links.navigation.menu.do-not-print>]
```

The expression was passed to a PyQuery object, which generated a list of evaluated elements. These elements are iterated for their exact values or their content.
