In the following code, we are trying to matchFORTRAN that was found in sentence, which is being omitted with the patterns we tried in the code previously:


`matches = re.findall(r"\s*([\sorA-Z+]+)\)",sentence) #r'\s*([A-Z]+)\)' matches 'FORTRAN'`{{execute}}

`print("Findall found total ",len(matches)," Matches >> ",matches)`{{execute}}

`fortran = matches[0] # 'or FORTRAN'`{{execute}}

**Note:** Please press enter to run multiline code after clicking following:

```if re.match(r'or',fortran): 
        fortran = re.sub(r'or\s*','',fortran) #substitute 'or ' with empty string
        print(fortran)```{{execute}}


```if re.search(r'^F.*N$',fortran):  #using beginning and end of line searching pattern 
        print("True")```{{execute}}

As shown in the preceding code block, the Python library, re, possesses various functions.

![](https://github.com/fenago/katacoda-scenarios/raw/master/web-scraping-with-python/chapter-09/steps/5/2.JPG)

**Note:** r'[^a-z]' (the caret or ^), when used inside a character set, acts as negation. Here, this means except or exclude [a-z].
