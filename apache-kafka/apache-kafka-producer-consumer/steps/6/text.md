In this step, we will publish a message using kafka. We will also verify that the message is consumed by the client.

#### Publish a message
Kafka also has a command to send messages through the command line; the input can be a text file or the console standard input. Each line typed in the input is sent as a single message to the cluster.

In a command-line window, run the following commands to sent messages to the server:

`echo "Fool me once shame on you" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic amazingTopic > /dev/null`{{execute}}

`echo "Fool me twice shame on me" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic amazingTopic > /dev/null`{{execute}}

These lines push two messages into the amazingTopic running on the localhost cluster on the `9092` port.

This command is also the simplest way to check whether a broker with a specific topic is up and running as it is expected.

As we can see, the kafka-console-producer command receives the following parameters:

- **--broker-list:** This specifies the Zookeeper servers specified as a comma-separated list in the form, hostname:port.
- **--topic:** This parameter is followed by the name of the target topic.
- **--sync:** This specifies whether the messages should be sent synchronously.
- **--compression-codec:** This specifies the compression codec used to produce the messages. The possible options are: none, gzip, snappy, or lz4. If not specified, the default is gzip.
- **--batch-size:** If the messages are not sent synchronously, but the message size is sent in a single batch, this value is specified in bytes.
- **--message-send-max-retries:** As the brokers can fail receiving messages, this parameter specifies the number of retries before a producer gives up and drops the message. This number must be a positive integer.
- **--retry-backoff-ms:** In case of failure, the node leader election might take some time. This parameter is the time to wait before producer retries after this election. The number is the time in milliseconds.
- **--timeout:** If the producer is running in asynchronous mode and this parameter is set, it indicates the maximum amount of time a message will queue awaiting for the sufficient batch size. This value is expressed in milliseconds.
- **--queue-size:** If the producer is running in asynchronous mode and this parameter is set, it gives the maximum amount of messages will queue awaiting the sufficient batch size.
