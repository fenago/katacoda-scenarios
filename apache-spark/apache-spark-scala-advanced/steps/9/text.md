

Let us now see how we can access the first and the rest of elements using head and tail.

`println(shows.head)`{{execute}} 

`println(shows.tail)`{{execute}} 

 

Let us now use foreach to print each element of the list.
`shows.foreach(println)`{{execute}} 


Let us now use the map function to convert each and every show to lower case.
`shows.map(show => show.toLowerCase)`{{execute}} 

 

These are a few transformations we can apply over a list. There are so many more transformations and operations you can apply on. From the Scala console, simply type the list of the name and the dot operator as shown below and press tab key on your keyboard. The console should display you a huge list of transformations you can apply on your list.

```
shows.<press tab key>
```

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_050.png) 

If you are not sure what a function does, you can type its name after the dot operator and press tab twice. The console will show you what the function expects you to pass in. For example,

```
shows.reduce<press tab key twice>
```

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_051.png) 