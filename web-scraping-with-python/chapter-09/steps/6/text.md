
Group matches can be individually explored by using the group() method, as shown in the following code:


`print("Group : ",dateMatches.group())`{{execute}}

`print("Groups : ",dateMatches.groups())`{{execute}}

`print("Group 1 : ",dateMatches.group(1))`{{execute}}

`print("Group 5 : ",dateMatches.group(5))`{{execute}}

As we can see, though the pattern has been searched against multiline timeDate, it results in a single group; an individual group can be returned using the index too. An re-related match object contains the groups() and group() functions; groups(0) results in the same output as groups(). Individual elements in groups() will require an index starting from 1. 

- **re.finditer():** This is used to iterate over resulting matches that are obtained for the pattern or pattern object found in the content that's provided. It returns a match (_sre.SRE_Match) object that's found from re.match()
- **re.match():** returns an object that contains various functions and attributes that are used in code examples. These are as follows:

- **start():** Returns the starting character index that matches the expression
- **end():** Returns the ending character index that matches the expression
- **span():** Returns the starting and ending character indexes of the matching expression
- **lastindex:** Returns the index of the last matched expression
- **groupdict():** Returns the matching group dictionary with a pattern string and matched values
- **groups():** Returns all matching elements
- **group():** Returns an individual group and can be accessed with the group name
- **lastgroup:** Returns the name of the last group

**Note:** Please press enter to run multiline code after clicking following:

```for match in re.finditer(pattern, timeDate):
        s = match.start()
        e = match.end()
        l = match.lastindex
        g = match.groups()
        print('Found {} at {}:{}, groups{} lastindex:{}'.format(timeDate[s:e], s, e,g,l))```{{execute}}

Patterns can also specify string names for the groups they are in; for example, r'(?P<year>[0-9]{4})' matches the year group. Using group-based patterns in Regex helps us to read the pattern and manage the output more accurately; this means that we don't have to worry about indexing.

Let's consider the patterns pDate (implementing group(), groupdict(), start(), end(), lastgroup, and lastindex) with a group name and code that are exhibiting the outputs for date and time, respectively:


`pDate = r'(?P<year>[0-9]{4})(?P<sep>[-])(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12][0-9]|3[01])'`{{execute}}

`recompiled = re.compile(pDate) #compiles the pattern`{{execute}}

**Note:** Please press enter to run multiline code after clicking following:

```for match in re.finditer(recompiled,timeDate): #apply pattern on timeDate
        s = match.start()
        e = match.end()
        l = match.lastindex
        print("Group ALL or 0: ",match.groups(0)) #or match.groups() that is all
        print("Group Year: ",match.group('year')) #return year
        print("Group Month: ",match.group('month')) #return month
        print("Group Day: ",match.group('day')) #return day
        print("Group Delimiter: ",match.group('sep')) #return seperator
        print('Found {} at {}:{}, lastindex: {}'.format(timeDate[s:e], s, e,l))
        print('year :',match.groupdict()['year']) #accessing groupdict()
        print('day :',match.groupdict()['day'])
        print('lastgroup :',match.lastgroup) #lastgroup name```{{execute}}

The preceding code results in the following output:


```
Group ALL or 0: ('2019', '-', '02', '11')
Group Year: 2019
Group Month: 02
Group Day: 11
Group Delimiter: -
Found 2019-02-11 at 16:26, lastindex: 4
year : 2019
day : 11
lastgroup : day
```

The following code shows the use of pTime (implementing span()):


`pTime = r'(?P<hour>[0-9]{2})(?P<sep>[:])(?P<min>[0-9]{2}):(?P<sec_mil>[0-9.:+]+)'`{{execute}}

`recompiled = re.compile(pTime)`{{execute}}

```for match in re.finditer(recompiled,timeDate):
        print("Group String: ",match.group()) #groups
        print("Group ALL or 0: ",match.groups())
        print("Group Span: ",match.span()) #using span()
        print("Group Span 1: ",match.span(1))
        print("Group Span 4: ",match.span(4))
        print('hour :',match.groupdict()['hour']) #accessing groupdict()
        print('minute :',match.groupdict()['min'])
        print('second :',match.groupdict()['sec_mil'])
        print('lastgroup :',match.lastgroup) #lastgroup name```{{execute}}

The preceding code will result in the following output:

```
Group String: 12:53:00+00:00
Group ALL or 0: ('12', ':', '53', '00+00:00')
Group Span: (245, 259)
Group Span 1: (245, 247)
Group Span 4: (251, 259)
hour : 12
minute : 53
second : 00+00:00
lastgroup : sec_mil
```

**Important:** Type `quit()`{{execute}} to exit python shell.

In this section, we have covered a general introduction to Regex and the features of the re Python library, along with some practical examples. Please refer to the Further reading section for more information regarding Regex. In the next section, we will be applying Regex to extract data from web-based content. 