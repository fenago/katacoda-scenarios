To build the project, run the following command from the kioto directory:
`gradle jar`{{execute T1}} 

If everything is correct, the output is something like the following:

```
BUILD SUCCESSFUL in 3s
1 actionable task: 1 executed
```

**Note:** If above command fails first time, you can try again.

Our broker is running on port 9092, so to create the uptimes topic, execute the following command:
`~/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic uptimes --replication-factor 1 --partitions 4`{{execute T1}} 

Run a console consumer for the uptimes topic, as follows:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T1}} 
