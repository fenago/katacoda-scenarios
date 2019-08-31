Parameters can also have the following default values: 

```
parameters: 
- description: Myapp configuration data
  name: SHOW_DATA
  required: true
  value: Example value
```


In some cases, we may want to generate values according to a certain pattern, as shown here:

```
parameters:
  - description: Password used for Redis authentication
    from: '[A-Z0-9]{8}'
    generate: expression
    name: REDIS_PASSWORD
```

In the preceding example, instantiating the template will generate a random password, eight characters long, consisting of all upper and lowercase alphabet letters, as well as numbers. Although that syntax is highly reminiscent of regular expressions, it implements only a small subset of Perl Compatible Regular Expressions (PCRE), so you can still use the \w, \d, and \a modifiers.