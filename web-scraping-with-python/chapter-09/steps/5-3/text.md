
The following code shows the use of some of these Regex patterns and the findall() function, along with their output:

`matches  = re.findall(r'\s(MAT.*?)\,',sentence,flags=re.IGNORECASE)`{{execute}}

`print("(MAT.*?)\,: ",matches)  #r'(?i)\s(MAT.*?)\,' can also be used`{{execute}}


`matches = re.findall(r'\s(MAT.*?)\,',sentence) #findall with 'MAT' case-sensitive`{{execute}}

`print("(MAT.*?)\,: ",matches)`{{execute}}

`matches = re.findall(r'\s(C.*?)\,',sentence)`{{execute}}

`print("\s(C.*?)\,: ",matches)`{{execute}}

The following functions were found in the preceding code:

re functions also support an optional flags argument. There's also an abbreviation for these flags (i for re.IGNORECASE, s for re.DOTALL, and M for re.MULTILINE). These can be used in patterns by including them at the beginning of the expressions. For example, r'(?i)\s(MAT.*?)\, will return [MATLAB, Mathematica]. The following are some other re functions that were found in the code:

- **re.IGNORECASE :** Ignores the case-sensitivity found in the pattern that's provided  
- **re.DOTALL :** Allows . (period) to match a newline, and works with strings containing multiple lines
- **re.MULTILINE :** Works with multiline strings and searches for patterns, including newline ("\n")
. or period: This matches any single character but not the newline ("\n"). It's used in patterns mostly with repetition characters. A period or . is required to be matched in the string, and should be used as \.:

`matchesOne = re.split(r"\W+",sentence)  #split by word, \w (word characters, \W - nonword)`{{execute}}

`print("Regular Split '\W+' found total: ",len(matchesOne ),"\n",matchesOne)`{{execute}}

```
Regular Split '\W+' found total: 43 
['Brief', 'information', 'about', 'Jobs', 'in', 'Python', 'Programming', 'and', 'Scripting', 'experience', 'in', 'some', 'language', 'such', 'as', 'Python', 'R', 'MATLAB', 'SAS', 'Mathematica', 'Java', 'C', 'C', 'VB', 'JavaScript', 'or', 'FORTRAN', 'is', 'expected', 'Participants', 'should', 'be', 'comfortable', 'with', 'basic', 'programming', 'concepts', 'like', 'variables', 'loops', 'and', 'functions', '']
```

`matchesTwo = re.split(r"\s",sentence) #split by space`{{execute}}

`print("Regular Split '\s' found total: ",len(matchesTwo),"\n", matchesTwo)`{{execute}}

- **re.split():** This splits the provided content based on the pattern and returns a list with results. A split() also exists, which can be used with a string to explode with the default or provided characters. It's used in a similar fashion to splitSentence, from earlier in this section.

#### DateTime
In code below we are trying to apply the regex pattern for the value found inside datetime attribute. Pattern defined will be compiled and then used to search in the code block:


```timeDate= '''<time datetime="2019-02-11T18:00:00+00:00"></time>
<time datetime="2018-02-11T13:59:00+00:00"></time>
<time datetime="2019-02-06T13:44:00.000002+00:00"></time>
<time datetime="2019-02-05T17:39:00.000001+00:00"></time>
<time datetime="2019-02-04T12:53:00+00:00"></time>'''```{{execute}}

`pattern = r'(20\d+)([-]+)(0[1-9]|1[012])([-]+)(0[1-9]|[12][0-9]|3[01])'`{{execute}}

`recompiled = re.compile(pattern)  # <class '_sre.SRE_Pattern'>`{{execute}}

`dateMatches = recompiled.search(timeDate)`{{execute}}

- **re.compile():** This is used to compile a Regex pattern and receive a pattern object (_sre.SRE_Pattern). The object that's received can be used with other Regex features.

