CSS Selectors have various combinators such as +, >, a space character, and so on, which show relationships between the elements. A few such combinators are used in the following example code:

`print(soup.select('p.story > a.sister'))#Selects all <a> with class='sister' that are direct child to <p> with class="story"`{{execute}}

`print(soup.select('p b'))#Selects <b> inside <p>`{{execute}}

`print(soup.select('p + h1'))#Selects immediate <h1> after <p>`{{execute}}

`print(soup.select('p.story + h1'))#Selects immediate <h1> after <p> with class 'story'`{{execute}}

`print(soup.select('p.title + h1'))#Selects immediate <h1> after <p> with class 'title'`{{execute}}
