
PyQuery also contains pseudo classes or :pseudo element, and are used for indexing and obtaining predefined expression results. :pseudo element can also be appended to an existing selector query. The following code implements some of the pseudo elements that are common while traversing:

`page('nav:first') #first <nav> element`{{execute}}

`page('a:first') #first <a> element`{{execute}}

`page('ul:first') #first <ul> element`{{execute}}

`page('ul:last') #last <ul> element`{{execute}}

Let's go over the pseudo elements that were used in the preceding code:

- `:first:` Returns the first occurrence of an element from the content provided
- `:last:` Returns the last occurrence of an element from the content provided

Let's look at a general implementation of a few more :pseudo element to list the HTML elements:

`page(':header') #header elements found`{{execute}}

`page(':input') #input elements found`{{execute}}

`page(':empty') #empty elements found`{{execute}}

`page(':empty:odd') #empty elements, only Odd ones are listed`{{execute}}


The following are the :pseudo element that we used in the preceding code:

- **:header:** Returns the header elements (h1, h2,..., h5, h6) found in the page.
- **:input:** Returns all the input elements. Large numbers of HTML `<form>-based` pseudo elements exist. Please refer to https://pythonhosted.org/pyquery/ for more information.
- **:empty:** Returns all the elements that don't have any child element.
- **:odd:** Returns elements indexed as odd numbers. They can be used with other :pseudo element as :empty:odd.
- **:even:** Similar to :odd, but returns evenly indexed elements.

The following code demonstrates an expression for traversing, :pseudo element, and element attributes together:


`page.find('ul:first').attr('class') #class name of first <ul> element`{{execute}}

`page.find('a:first').attr('href') #href value of first <a> element`{{execute}}

`page.find('a:last').attr('href') #href value of last <a> element`{{execute}}

`page.find('a:eq(0)').attr('href') #href value of first <a> element using Index!`{{execute}}

`page.find('a:eq(0)').text() #text from first <a> element`{{execute}}

The following are a few more :pseudo element. We can use these to address the index of the elements:

- `:eq:` Selects the particular index number; evaluates to equals to.
- `:lt:` Evaluates to less than for the provided index number.
- `:gt:` Evaluates to greater than for the provided index numbers.
 
