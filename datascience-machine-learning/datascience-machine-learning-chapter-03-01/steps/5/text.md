If I want to save this graph to a file, maybe I want to include it in a document or something, I can do something like the following code:

```
plt.plot(x, norm.pdf(x)) 
plt.plot(x, norm.pdf(x, 1.0, 0.5)) 
plt.savefig('\MyPlot.png', format='png')
```

Instead of just calling plt.show(), I can call plt.savefig() with a path to where I want to save this file and what format I want it in.


That's pretty cool. One other quick thing to note is that depending on your setup, you may have permissions issues when you come to save the file. You'll just need to find the folder that works for you. On Windows, your Users\Name folder is usually a safe bet. Alright, let's move on.
