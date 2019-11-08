Finally, the last data structure that we'll see a lot in Python is a dictionary, and you can think of that as a map or a hash table in other languages. It's a way to basically have a sort of mini-database,sort of a key/value data store that's built into Python. So let's say, I want to build up a little dictionary of Star Trek ships and their captains:

I can set up a captains = {}, where curly brackets indicates an empty dictionary. Now I can use this sort of a syntax to assign entries in my dictionary, so I can say captains for Enterprise is Kirk, for Enterprise D it is Picard, for Deep Space Nine it is Sisko, and for Voyager it is Janeway. Now I have, basically, this lookup table that will associate ship names with their captain, and I can say, for example, print captains["Voyager"], and I get back Janeway.

A very useful tool for basically doing lookups of some sort. Let's say you have some sort of an identifier in a dataset that maps to some human-readable name. You'll probably be using a dictionary to actually do that look up when you're printing it out.

We can also see what happens if you try to look up something that doesn't exist. Well, we can use the get function on a dictionary to safely return an entry. So in this case, Enterprise does have an entry in my dictionary, it just gives me back Kirk, but if I call the NX-01 ship on the dictionary, I never defined the captain of that, so it comes back with a None value in this example, which is better than throwing an exception, but you do need to be aware that this is a possibility:

```
print (captains.get("NX-01"))
```

The output of the above code is as follows:

```
None
```

The captain is Jonathan Archer, but you know, I'm get a little bit too geeky here now.

Iterating through entries

```
for ship in captains:
     print (ship + ": " + captains[ship])
```

The output of the above code is as follows:


Let's look at a little example of iterating through the entries in a dictionary. If I want to iterate through every ship that I have in my dictionary and print out captains, I can type for ship in captains, and this will iterate through every single key in my dictionary. Then I can print out the lookup value of each ship's captain, and that's the output that I get there.

There you have it. This is basically the main data structures that you'll encounter in Python. There are some others, such as sets, but we'll not really use them in this book, so I think that's enough to get you started. Let's dive into some more Python nuances in our next section.
