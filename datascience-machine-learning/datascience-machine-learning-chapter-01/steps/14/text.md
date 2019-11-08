**Negative syntax**

One more thing you can do is have this negative syntax:

```
x[-2:]
The output is as follows:

```
[5, 6]

By saying x[-2:], this means that I want the last two elements in the list. This means that go backwards two from the end, and that will give me 5 and 6, because those are the last two things on my list.

**Adding list to list**

You can also change lists around. Let's say I want to add a list to the list. I can use the extend function for that, as shown in the following code block:

```
x.extend([7,8])
x

The output of the above code is as follows:

```
[1, 2, 3, 4, 5, 6, 7, 8]

I have my list of 1, 2, 3, 4, 5, 6. If I want to extend it, I can say I have a new list here, [7, 8], and that bracket indicates this is a new list of itself. This could be a list implicit, you know, that's inline there, it could be referred to by another variable. You can see that once I do that, the new list I get actually has that list of 7, 8 appended on to the end of it. So I have a new list by extending that list with another list.
