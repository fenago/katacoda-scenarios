Obviously, if a greater number than the number of running servers on the cluster is specified, it will result in an error (you don't believe me? Try it in your environment). The error will be like this:

```
Error while executing topic command: replication factor: 3 larger than available brokers: 2

[2018-09-01 07:13:31,350] ERROR org.apache.kafka.common.errors.InvalidReplicationFactorException: replication factor: 3 larger than available brokers: 2

(kafka.admin.TopicCommand$)

```

The --partitions parameter, as its name implies, says how many partitions the topic will have. The number determines the parallelism that can be achieved on the consumer's side. This parameter is very important when doing cluster fine-tuning.

Finally, as expected, the --zookeeper parameter indicates where the Zookeeper cluster is running.

When a topic is created, the output in the broker log is something like this:

```
[2018-09-01 07:05:53,910] INFO [ReplicaFetcherManager on broker 1] Removed fetcher for partitions amazingTopic-0 (kafka.server.ReplicaFetcherManager)

[2018-09-01 07:05:53,950] INFO Completed load of log amazingTopic-0 with 1 log segments and log end offset 0 in 21 ms (kafka.log.Log)
````


In short, this message reads like a new topic has been born in our cluster.

How can I check my new and shiny topic? By using the same command: `kafka-topics`.

There are more parameters than `--create`. To check the status of a topic, run the kafka-topics command with the --list parameter, as follows:

`~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181`{{execute}} 

The output is the list of topics, as we know, is as follows:

```
amazingTopic
```

This command returns the list with the names of all of the running topics in the cluster. 