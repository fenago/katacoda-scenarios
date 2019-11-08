
**It's fast**

What's the big deal about Spark? I mean, there are similar technologies like MapReduce that have been around longer. Spark is fast though, and on the website they claim that Spark is "up to 100x faster than MapReduce when running a job in memory, or 10 times faster on disk." Of course, the key words here are "up to," your mileage may vary. I don't think I've ever seen anything, actually, run that much faster than MapReduce. Some well-crafted MapReduce code can actually still be pretty darn efficient. But I will say that Spark does make a lot of common operations easier. MapReduce forces you to really break things down into mappers and reducers, whereas Spark is a little bit higher level. You don't have to always put as much thought into doing the right thing with Spark.

Part of that leads to another reason why Spark is so fast. It has a DAG engine, a directed acyclic graph. Wow, that's another fancy word. What does it mean? The way Spark works is, you write a script that describes how to process your data, and you might have an RDD that's basically like a data frame. You might do some sort of transformation on it, or some sort of action on it. But nothing actually happens until you actually perform an action on that data. What happens at that point is, Spark will say "hmm, OK. So, this is the end result you want on this data. What are all the other things I had to do to get up this point, and what's the optimal way to lay out the strategy for getting to that point?" So, under the hood, it will figure out the best way to split up that processing, and distribute that information to get the end result that you're looking for. So, the key inside here, is that Spark waits until you tell it to actually produce a result, and only at that point does it actually go and figure out how to produce that result. So, it's kind of a cool concept there, and that's the key to a lot of its efficiency.

**It's young**

Spark is a very hot technology, and is relatively young, so it's still very much emerging and changing quickly, but a lot of big people are using it. Amazon, for example, has claimed they're using it, eBay, NASA's Jet Propulsional Laboratories, Groupon, TripAdvisor, Yahoo, and many, many others have too. I'm sure there's a lot of companies using it that don't confess up to it, but if you go to the Spark Apache Wiki page at http://spark.apache.org/powered-by.html.

There's actually a list you can look up of known big companies that are using Spark to solve real-world data problems. If you are worried that you're getting into the bleeding edge here, fear not, you're in very good company with some very big people that are using Spark in production for solving real problems. It is pretty stable stuff at this point.

**It's not difficult**

It's also not that hard. You have your choice of programming in Python, Java, or Scala, and they're all built around the same concept that I just described earlier, that is, the Resilient Distributed Dataset, RDD for short. We'll talk about that in a lot more detail in the coming sections of this chapter.
