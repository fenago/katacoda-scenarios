
Zookeeper and Kafka are already running, generate the two necessary topics, as follows:

`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic input-topic`{{execute T1}} 

`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic output-topic`{{execute T1}} 

Recall, to display the topics running in our cluster type, use the following:
`~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181`{{execute T1}} 

In the same command-line terminal, start the console producer running the input-topic topic, as follows:
`~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic input-topic`{{execute T1}} 