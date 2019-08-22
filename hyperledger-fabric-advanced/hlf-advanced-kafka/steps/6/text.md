In this step, we will publish a message using kafka. We will also verify that the message is consumed by the client.

#### Publish a message
We can publish a message to kafka topic and consumers can get these messages from the beginning.
`echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TestTopic > /dev/null`{{copy}}

#### Subscribe to a message
We can subscribe to a kafka topic and get messages from the beginning.
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic TestTopic --from-beginning`{{copy}}

You should get following message as output. This is the message which we published.
```
Hello, World
```

**Note** Press `Ctrl + C` after receiving the message to quit above script.