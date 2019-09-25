In the second command-line terminal, start a console consumer listening to `output-topic` by typing the following: 

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic output-topic`{{execute T2}} 

**Important:** Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 2`.