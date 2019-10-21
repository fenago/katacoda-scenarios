Predicates are used to identify a specific node or element. Predicate expressions are written using square brackets that are similar to Python lists or array expressions.

A brief explanation of the XPath expression given in the preceding XML is listed in the following table:

XPath expression | Description
--- | ---
`//` | 	Selects nodes in the document, no matter where they are located
`//*` | Selects all elements in the document
`//food` | Selects the element food
`*` | Selects all elements
`//food/name` | Selects all the name elements inside food
`//food[last()]/name` | Selects the name element from the last food node
`//food[rating>3 and rating<5]/name` | Selects the name of food that fulfills the predicate condition
`sum(//food/feedback)` |  Provides the sum of feedback found in all foodnodes
`//food/name[contains(.,"Juice")]` | Selects the name of food that contains the Juice string
`//food/description[starts-with(.,"Fresh")]` | 	Selects text from description node that starts with Fresh
`//food[position()<3]` |  Selects the first and second food according to its position