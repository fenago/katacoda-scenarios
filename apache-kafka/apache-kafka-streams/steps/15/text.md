To explain late events, we need a system where the events arrive periodically and we want to know how many events are produced by unit of time. In Figure 6.1, we show this scenario:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-streams/steps/15/1.png)
	
Figure 6.1: The events as they were produced

In the preceding figure, each marble represents an event. They are not supposed to have dimensions as they are at a specific point in time. Events are punctual, but for demonstration purposes, we represent them as balls. As we can see in t1 and t2, two different events can happen at the same time.

In our figure, tn represents the nth time unit. Each marble represents a single event. To differentiate between them, the events on t1 have one stripe, the events on t2 have two stripes, and the events on t3 have three stripes.

We want to count the events per unit of time, so we have the following:

- **t1** has six events
- **t2** has four events
- **t3** has three events

As systems have failures (such as network latency, shutdown of servers, network partitioning, power failures, voltage variations, and so on), suppose that an event that happened during t2 has a delay and reached our system at t3, shown as follows in Figure 6.2:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-streams/steps/15/2.png)

If we count our events using the processing time, we have the following results:

- **t1** has six events
- **t2** has three events
- **t3** has four events

If we have to calculate how many events were produced per time unit, our results would be incorrect.

The event that arrived on t3 instead of t2 is called a late event. We just have two alternatives, they are given as follows:

- When **t2** ends, produce a preliminary result that the count for t2 is three events. And then, during processing, when we find in another time an event belonging to t2, we update the result for t2: t2 has four events.
- When each window ends, we wait a little after the end before we produce a result. For example, we could wait another time unit. In this case, the results for tn are obtained when t(n+1) ends. Remember, the time to wait to produce results might not be related to the time unit size.
As you can guess, these scenarios are quite common in practice, and there are currently many interesting proposals. One of the most complete and advanced suites for handling late events is the Apache Beam proposal. However, Apache Spark, Apache Flink, and Akka Streams are also very powerful and attractive.

As we want to see how it is solved with Kafka Streams here, let's see that.