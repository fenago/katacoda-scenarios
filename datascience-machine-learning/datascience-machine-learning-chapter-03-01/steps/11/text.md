A little fun example here. If you're familiar with the webcomic XKCD, there's a little bit of an Easter egg in Matplotlib, where you can actually plot things in XKCD style. The following code shows how you can do that.

```
plt.xkcd() 
 
fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1) 
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none') 
plt.xticks([]) 
plt.yticks([]) 
ax.set_ylim([-30, 10]) 
 
data = np.ones(100) 
data[70:] -= np.arange(30) 
 
plt.annotate( 
    'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED', 
    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10)) 
 
plt.plot(data) 
 
plt.xlabel('time') 
plt.ylabel('my overall health') 
```

In this example, you call plt.xkcd(), which puts Matplotlib in XKCD mode. After you do that, things will just have a style with kind of a comic book font and squiggly lines automatically. This little simple example will show a funny little graph where we are plotting your health versus time, where your health takes a steep decline once you realize you can cook bacon whenever you want to. All we're doing there is using the xkcd() method to go into that mode. You can see the results below:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-03-01/steps/2/10.png)

There's a little bit of interesting Python here in how we're actually putting this graph together. We're starting out by making a data line that is nothing but the value 1 across 100 data points. Then we use the old Python list slicing operator to take everything after the value of 70, and we subtract off from that sub-list of 30 items, the range of 0 through 30. So that has the effect of subtracting off a larger value linearly as you get past 70, which results in that line heading downward down to 0 beyond the point 70.

So, it's a little example of some Python list slicing in action there, and a little creative use of the arange function to modify your data.
