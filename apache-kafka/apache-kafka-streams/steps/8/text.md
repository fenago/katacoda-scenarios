
From a new command-line window, we execute the same command, shown as follows:
`java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainStreamsProcessor

The output should be something like the following:

```
2017/07/05 15:03:18.045 INFO ... Setting newly assigned 
partitions [healthchecks-2, healthchecks -3]
```

Take a look at the following log:

```
...
2017/07/05 15:03:18.045 INFO ... Revoking previously assigned partitions [healthchecks -0, healthchecks -1, healthchecks -2, healthchecks -3]
2017/07/05 15:03:18.044 INFO ... State transition from RUNNING to PARTITIONS_REVOKED
2017/07/05 15:03:18.044 INFO ... State transition from RUNNING to REBALANCING
2017/07/05 15:03:18.044 INFO ... Setting newly assigned partitions [healthchecks-2, healthchecks -3]
...
```

We can read that the first instance was using the four partitions, then when we ran the second instance, it entered a state where the partitions were reassigned to consumers; to the first instance was assigned two partitions:healthchecks-0 and  healthchecks-1.

And this is how Kafka Streams smoothly scale out. Remember that all this works because the consumers are part of the same consumer group and are controlled from Kafka Streams through the application.id property.

We must also remember that the number of threads assigned to each instance of our application can also be modified by setting the num.stream.threads property. Thus, each thread would be independent, with its own producer and consumer. This ensures that the resources of our servers are used in a more efficient way.