
In the preceding code, we can see similar patterns with certain additional characters provided, but they differ in output. A general explanation is provided for some of these patterns, as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/5/1.JPG)

Regex quantifiers are also categorized as follows:

- **Greedy quantifiers:** These match any element as many times as possible. 
- **Lazy or non-greedy quantifiers:** These match any element as few times as possible. Normally, a greedy quantifier is converted into a lazy quantifier by adding ? to it.


Patterns such as `([A-Z+]+)\`, match the set of characters from A to Z and + that can exist in at least one or more characters, followed by ,. In sentence in the preceding code, we can find R, MATLAB, SAS, Mathematica, Java, C, C++, VB, and JavaScript (there's also FORTRAN), that is, names followed by , (but not in the case of FORTRAN; this is why it's been excluded in the output for provided patterns). 
