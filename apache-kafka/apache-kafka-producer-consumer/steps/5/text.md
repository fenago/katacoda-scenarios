How can I get details of a topic? Using the same command: kafka-topics.

For a particular topic, run the kafka-topics command with the --describe parameter, as follows:
`~/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic amazingTopic`{{execute}}

The command output is as follows:

```
Topic:amazingTopic PartitionCount:1 ReplicationFactor:1 Configs: Topic: amazingTopic Partition: 0 Leader: 1 Replicas: 1 Isr: 1
```

Here is a brief explanation of the output:

- **PartitionCount:** Number of partitions on the topic (parallelism)
- **ReplicationFactor:** Number of replicas on the topic (redundancy)
- **Leader:** Node responsible for reading and writing operations of a given partition
- **Replicas:** List of brokers replicating this topic data; some of these might even be dead
- **Isr:** List of nodes that are currently in-sync replicas

Let's create a topic with multiple replicas (for example, we will run with more brokers in the cluster); we type the following:
`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 1 --topic redundantTopic`{{execute}}

The output is as follows:
```
Created topic redundantTopic
````

Now, call the kafka-topics command with the --describe parameter to check the topic details, as follows:
`~/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic redundantTopic`{{execute}}

```
Topic:redundantTopic PartitionCount:1 ReplicationFactor:2 Configs:

Topic: redundantTopic Partition: 0 Leader: 1 Replicas: 1,2 Isr: 1,2
```

As you can see, Replicas and Isr are the same lists; we infer that all of the nodes are in-sync.

 