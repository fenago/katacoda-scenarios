
Apart from the general features that are used to identify the index and find elements, :pseudo element can also be used to search the element with the provided text, as shown in the following code:

`page('p:contains("Python")') #return elements <p> with text 'Python"`{{execute}}

`page('p:contains("python.org")') #return elements <p> with text "python.org"`{{execute}}

Return text from second `<p>` element containing text "python.org"
`page('p:contains("python.org")').eq(1).text()`{{execute}}

The following list describe simple definitions of :contains and eq(), as used in the previous code:

- **:contains:** Matches all elements that contain the provided text.
- **eq():** Returns the element that was found for a particular index number. Evaluates as equals to and is similar to :eq.
 

pyquery has a few functions that return a Boolean answer, which is quite effective in circumstances where you need to search for an element with attributes and also confirm the attribute's value:


Check if class is `python-logo`
`page('h1.site-headline:first a img').is_('.python-logo') `{{execute}}

Check if `<img>` has class `python-logo`
`page('h1.site-headline:first a img').has_class('python-logo') `{{execute}}

The following are the functions that were used in the previous code, along with their definitions:

- **is_():** Accepts a selector as an argument and returns True if the selector matches elements, otherwise, it returns False.
- **has_class():** Returns True if the selector matches the class that's provided. It is useful for identifying elements with the class attribute.
 
We have used a few important functions and tools with pyquery that enhance element identification and traversal-related properties. In the next section, we will learn about and demonstrate iteration.