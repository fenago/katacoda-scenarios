In the **second** command-line window, start a command-line consumer listening to the valid-messages topic, as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic valid-messages`{{execute T2}} 

**Important:** Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 2`.


In the **third** command-line window, start a command-line consumer listening to invalid-messages topic, as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic invalid-messages`{{execute T3}}

**Important:** Interface will keep switching back to terminal 1 because producer is running there after executing command, you can manually switch by clicking `terminal 3`.