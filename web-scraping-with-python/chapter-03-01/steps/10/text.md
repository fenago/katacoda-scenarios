Element selectors are basic selectors that choose elements from HTML. Most often, these elements are the basic tags of HTML. The following table lists some of the selectors and their usage for this category:

CSS query | Description
--- | ---
`h1` | Selects `<h1>` elements
`a` | Selects all of the `<a>` elements
`*` | Selects all elements in the HTML code
`body *` | Selects all `<h1>, <p>, <div>, and <a>` elements
`div a` | Selects all `<a>` inside `<div>` (using space character in between)
`h1 + p` | Selects immediate `<p>` elements after `<h1>`
`h1 ~ p` | Selects every `<p>` elements preceded by `<h1>`
`h1,p` | Selects all `<h1> and `< p >` elements
`div > a` | Selects all `<a>` elements that are a direct child of `<div>`

#### ID and class selectors
ID and class selectors are additional features available with element selectors. We can find HTML tags with the class and id attributes. These are also known as global attributes. These attributes are mostly preferred over other attributes as they define the tags for structure and with identification.

The following table lists the usage of this category of selectors:

CSS query | Description
--- | ---
`.header` | Selects an element with class=header
`.plan` | Selects `<a>` with class=plan
`div.links` | Selects `<div>` with class=plan
`#link` | Selects an element with id=link
`a#link` | Selects `<a>` elements with id=link
`a.plan` | Selects `<a>` elements with class=plan