
For finding all of the HTML tags that exist inside page, we used the find_all() method with soup as an object of BeautifulSoup using the lxml parser.

Here, we are finding all HTML tag names that don't have any attributes. \w+ matches any word with one or more character:

`applyPattern(r'<(\w+)>') #Finding Elements without attributes`


Finding all HTML tags or elements that don't end with > or contain some attributes can be found with the help of the space character, that is, \s: 

`applyPattern(r'<(\w+)\s') #Finding Elements with attributes`

Now, by combining all of these patterns, we are listing all HTML tags that were found in the page source. The same result was also obtained in the previous code by using soup.find_all() and the name attribute:

`applyPattern(r'<(\w+)\s?') #Finding all HTML element`

Let's find the attribute's name, as found in the HTML element:

`applyPattern(r'<\w+\s+(.*?)=') #Finding attributes name`


As we can see, there were only 10 attributes listed. In the HTML source, a few tags contain more than one attribute,such as `<a href="https://www.google.com" style="color:red;">Google</a>`, and only the first attribute was found using the provided pattern. 

Let's rectify this. We can select words with the = character after them by using the r'(\w+)=' pattern, which will result in all of the attributes found in the page source being returned:

`applyPattern(r'(\w+)=') #Finding names of all attributes`

Similarly, let's find all of the values for the attributes we've found. The following code lists the values of the attributes and compares the 18 attributes we listed previously. Only 9 values were found. With the pattern we used here, `r'=\"(\w+)\"'` will only find the word characters.

`applyPattern(r'=\"(\w+)\"')`


Here, the complete attribute values are listed by using the proper pattern we analyzed. The content attribute values also contained non-word characters such as ;, /, :, and .. In Regex, we can include such characters in the pattern individually, but this approach may not be appropriate in all cases. 

In this case, the pattern that includes \w and the non-whitespace character, \S, fits perfectly, that is, `r'=\"([\w\S]+)\"`: 

`applyPattern(r'=\"([\w\S]+)\"')`

Finally, let's collect all of the text inside the HTML elements that are found in-between the opening and closing HTML tags:

`applyPattern(r'\>(.*)\<')`


#### Run Code
Now, run the python code by running: `python regexHTML.py`{{execute}}

