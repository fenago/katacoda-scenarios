The partially applied functions as the name suggests are applied partially by only passing some parameters while holding back other parameters. The partially applied functions are used when you do not want to pass all the parameters at once but instead, you can pass some parameters first and then the other parameters at later time.

For example, we can partially apply the function which we created above using currying.

```val part = sum(54)_```

This will return us a function object called part.

We can now pass the parameter which we held back as shown below.

```part(6)```
