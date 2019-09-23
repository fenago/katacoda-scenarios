The last step is how to read the generated messages. Kafka also has a powerful command that enables messages to be consumed from the command line. Remember that all of these command-line tasks can also be done programmatically. As the producer, each line in the input is considered a message from the producer. 

Run the following command:

`~/kafka/bin/kafka-console-consumer.sh --topic amazingTopic --bootstrap-server localhost:9092 --from-beginning`{{execute}} 

The output should be as follows:

```
Fool me once shame on you
Fool me twice shame on me
```

**Note** Press `Ctrl + C` after receiving the message to quit above script.

The parameters are the topic's name and the name of the broker producer. Also, the --from-beginning parameter indicates that messages should be consumed from the beginning instead of the last messages in the log (now test it, generate many more messages, and don't specify this parameter).

There are more useful parameters for this command, some important ones are as follows:

- **--fetch-size:** This is the amount of data to be fetched in a single request. The size in bytes follows as argument. The default value is 1,024 x 1,024.
- **--socket-buffer-size:** This is the size of the TCP RECV. The size in bytes follows this parameter. The default value is 2 x 1024 x 1024.
- **--formater:** This is the name of the class to use for formatting messages for display. The default value is NewlineMessageFormatter.
- **--autocommit.interval.ms:** This is the time interval at which to save the current offset in milliseconds. The time in milliseconds follows as argument. The default value is 10,000.
- **--max-messages:** This is the maximum number of messages to consume before exiting. If not set, the consumption is continuous. The number of messages follows as the argument.
- **--skip-message-on-error:** If there is an error while processing a message, the system should skip it instead of halting.


The most requested forms of this command are as follows:

To consume just one message, use the following:
```
~/kafka/bin/kafka-console-consumer.sh --topic  amazingTopic --bootstrap-server localhost:9092 --max-messages 1
```