In the first command-line terminal, move to the Confluent directory and start it, as follows:
`~/kafka/bin/confluent start`{{execute T1}} 

Once the control center (Zookeeper and Kafka included) is running in the same command-line terminal, generate the two necessary topics, as follows:

`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic input-topic`{{execute T1}} 

`~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic output-topic`{{execute T1}} 

Recall, to display the topics running in our cluster type, use the following:
`~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181`{{execute T1}} 

In the same command-line terminal, start the console producer running the input-topic topic, as follows:
`~/kafka/bin/kafka-console-producer --broker-list localhost:9092 --topic input-topic`{{execute T1}} 