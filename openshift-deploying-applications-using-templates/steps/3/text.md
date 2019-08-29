Parameters can also have the following default values: 

Copy
parameters: 
- description: Myapp configuration data
  name: SHOW_DATA
  required: true
  value: Example value
In some cases, we may want to generate values according to a certain pattern, as shown here:

Copy
parameters:
  - description: Password used for Redis authentication
    from: '[A-Z0-9]{8}'
    generate: expression
    name: REDIS_PASSWORD
In the preceding example, instantiating the template will generate a random password, eight characters long, consisting of all upper and lowercase alphabet letters, as well as numbers. Although that syntax is highly reminiscent of regular expressions, it implements only a small subset of Perl Compatible Regular Expressions (PCRE), so you can still use the \w, \d, and \a modifiers:

[w]{10}: This expands to 10 alphabet characters, numbers, and underscores. This follows the PCRE standard and is the same as [a-zA-Z0-9_]{10}.
[\d]{10}: This expands to 10 numbers. This is the same as [0-9]{10}.
 [\a]{10}: This expands to 10 alphabetical characters. This is the same as [a-zA-Z]{10}.
This capability is very useful for generating random passwords.