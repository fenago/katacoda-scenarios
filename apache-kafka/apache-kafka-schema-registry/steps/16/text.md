To build the project, run the following command from the kioto directory:
`gradle jar`{{execute}} 

If everything is OK, the output is something like the one shown here:

```
BUILD SUCCESSFUL in 3s
 1 actionable task: 1 executed
```

**Note:** If above command fails first time, you can try again.

#### Kafka Consumer
The broker is running on port 9092. To create the `healthchecks-avro` topic, execute the following command:
`~/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic healthchecks-avro --replication-factor 1 --partitions 4`{{execute}} 

Note that we are just creating a normal topic and nothing indicates the messages format.

Run a console consumer for the healthchecks-avro topic:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic healthchecks-avro`{{execute}} 