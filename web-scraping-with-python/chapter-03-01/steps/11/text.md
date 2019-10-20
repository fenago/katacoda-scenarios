Attribute selectors are used to define selectors with the available attributes. HTML tags contain an attribute that helps to identify a particular element with the attribute and the value that it carries.

The following table lists a few ways to show the usage of attribute selectors:

CSS query | Description
--- | ---
`a[href*="domain"]` | Selects elements that contain the domain substring in its href
`a[href^="mailto"]` | Selects elements that start with the mailto substring of the href attributes:
`a[href$="pdf"]` | Selects elements that have a pdf substring at the end of its href attribute:
`[href~=do]` | Selects all elements with the href attribute and matches do in values. The two < a > elements listed in the following both contain do inside of their href value
`[class]` | Selects all elements or < p >, < div >, and < a > with the class attribute
`[class=plan]` | Selects < a > with class=plan:


