There are various ways of finding elements in Beautiful Soup, such as using functions starting with the word find or using attributes in CSS Selectors. Patterns can be searched for attributes keys using * in CSS Selectors as illustrated in the following code:


`print(soup.select('a[href*="example.com"]'))`{{execute}}

```
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

`print(soup.select('a[id*="link"]'))`{{execute}}

```[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
We were searching for the `<a>` element with the text example.com, which might exist in the value of the href attribute. Also, we were searching for the `<a>` element, which contains an attribute ID with a text link. 

With basic knowledge of CSS Selectors, we can deploy it with Beautiful Soup for various purposes. Using the select() function is quite effective when dealing with elements, but there are also limitations we might face, such as extracting text or content from the obtained element.


**Important:** Type `quit()`{{execute}} to exit python shell.

We have introduced and explored the elements of Beautiful Soup in the preceding sections. To wrap up the concept, we will create a crawler example in the upcoming section.