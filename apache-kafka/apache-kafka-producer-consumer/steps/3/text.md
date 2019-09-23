Is it possible to only manage (create, modify, or destroy) brokers through programming? No, we can also manage the topics. The topics can also be created through the command line. Kafka has pre-built utilities to manage brokers as we already saw and to manage topics, as we will see next.

To create a topic called amazingTopic in our running cluster, use the following command:
`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic amazingTopic`{{execute}} 

The output should be as follows:

```
Created topic amazingTopic
```

Here, the kafka-topics command is used. With the `--create` parameter it is specified that we want to create a new topic. The --topic parameter sets the name of the topic, in this case, amazingTopic.

Do you remember the terms parallelism and redundancy? Well, the `–-partitions` parameter controls the parallelism and the --replication-factor parameter controls the redundancy.

The `--replication-factor` parameter is fundamental as it specifies in how many servers of the cluster the topic is going to replicate (for example, running). On the other hand, one broker can run just one replica.