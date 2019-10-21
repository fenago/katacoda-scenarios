CSS selectors (also referred to as CSS query or CSS selector query) are defined patterns used by CSS to select HTML elements, using the element name or global attributes (ID, and Class). CSS selectors, as the name suggests, select or provide the option to select HTML elements in various ways.

In the following example code, we can visualize a few elements found in <body>:

- `<h1>` is an element and a selector.
- The `<p>` element or selector has the class attribute with the header style type. When it comes to selecting, <p> we can use either the element name, the attribute name, or just the type name.
- Multiple `<a>` are found inside `<div>`, but they differ with their class attribute, id, and value for the href property:


```
<html>
<head>
    <title>CSS Selectors: Testing</title>
    <style>
        h1{color:black;}
        .header,.links{color: blue;}
        .plan{color: black;}
        #link{color: blue;}
    </style>
</head>
<body>
    <h1>Main Title</h1>
    <p class=”header”>Page Header</p>
    <div class="links">
         <a class="plan" href="*.pdf">Document Places</a>
         <a id="link" href="mailto:xyz@domain.com">Email Link1!</a>
         <a href="mailto:abc@domain.com">Email Link2!</a>    
    </div>
</body>
</html>

```

The distinguishable patterns we have identified in the preceding code can be used to select those particular elements individually or in groups. Numbers of DOM parsers are available online, which provide a CSS query-related facility. One of them, as shown in the following screenshot, is https://try.jsoup.org/:


![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-03-01/steps/8/1.png)
