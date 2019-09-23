If you have a lot of questions here, it is normal.

The first thought to consider is that in streaming aggregation, and in streaming in general, the Streams are unbounded. It is never clear when we will take the final results, that is, we as programmers have to decide when to consider a partial value of an aggregation as a final result.

Recall that the print of the Stream is an instant photo of the KTable at a certain time. Therefore, the results of a KTable are only valid at the time of the output. It is important to remember that in the future, the values of the KTable may be different. Now, to see results more frequently, change the value of the commit interval to zero, shown as follows:

```
props.put("commit.interval.ms", 0);
```

This line says that the results of the KTable will be printed when they are modified, that is, it will print new values every second. If you run the program, the value of the KTable will be printed with each update (every second), shown as follows:

```
1532529080000 6
1532529080000 7
1532529080000 8
1532529080000 9
1532529080000 10 <-- Window end
1532529090000 1  <-- Window beginning
1532529090000 2
1532529090000 3
1532529090000 5  <-- The 4th didn't arrive
1532529090000 6
1532529090000 7
1532529090000 8
1532529090000 9  <-- Window end
1532529100000 1
1532529100000 2
1532529100000 3
1532529100000 4
1532529100000 5
1532529100000 6
1532529090000 10 <-- The 4th arrived, so the count value is updated
1532529100000 7
1532529100000 8
...
```


 

 

 

 

 

Keep a note of two effects:

The aggregate result (the count) for the window stops at 9 when the window ends and the next window events begin to arrive
When the late event finally arrives, it produces an update in the window's count
Yes, Kafka Streams apply event time semantics in order to do the aggregation. It is important to remember that in order to visualize the data, we had to modify the commit interval. Leaving this value at zero would have negative repercussions on a production environment.