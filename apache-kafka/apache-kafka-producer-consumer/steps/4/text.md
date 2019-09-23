If a greater number than the number of running servers on the cluster is specified, it will result in an error. The error will be like this:
`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 10 --partitions 1 --topic amazingTopic2`{{execute}} 

```
Error while executing topic command : Replication factor: 10 larger than available brokers: 1.
[2019-09-23 11:52:34,889] ERROR org.apache.kafka.common.errors.InvalidReplicationFactorException: Replication factor: 10 larger than available brokers:1.
 (kafka.admin.TopicCommand$)
```

The --partitions parameter, as its name implies, says how many partitions the topic will have. The number determines the parallelism that can be achieved on the consumer's side. This parameter is very important when doing cluster fine-tuning.

Finally, as expected, the --zookeeper parameter indicates where the Zookeeper cluster is running.

#### Verify
How can I check my new and shiny topic? By using the same command: `kafka-topics`.

There are more parameters than `--create`. To check the status of a topic, run the kafka-topics command with the --list parameter, as follows:

`~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181`{{execute}} 

The output is the list of topics, as we know, is as follows:

```
amazingTopic
```

This command returns the list with the names of all of the running topics in the cluster. 