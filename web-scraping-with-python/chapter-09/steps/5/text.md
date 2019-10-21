The length of sentence and the Python splitSentence list object is obtained and printed using the preceding code. These counts of element and character will be helpful while comparing answers that are returned from the following examples: 


`matches = re.findall(r"([A-Z+]+)\,",sentence) #finding pattern with [A-Z+] and comma behind`{{execute}}

`print("Findall found total ",len(matches)," Matches >> ",matches)`{{execute}}


```
Findall found total  6  Matches >>  ['R', 'MATLAB', 'SAS', 'C', 'C++', 'VB']
```

`matches = re.findall(r"([A-Z]+)\,",sentence) #finding pattern with [A-Z] and comma behind`{{execute}}

`print("Findall found total ",len(matches)," Matches >> ",matches)`{{execute}}

```
Findall found total 5 Matches >> ['R', 'MATLAB', 'SAS', 'C', 'VB']
```

re.findall() accepts a pattern to search and the content to look for regarding the provided pattern. Normally, patterns can be provided directly to functions as an argument and as a raw string preceded with r, such as r'([A-Z]+)', or a variable containing a raw string. 
