In the second command-line window, start a command-line consumer listening to the valid-messages topic, as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic valid-messages`{{execute T2}} 
 
 

In the third command-line window, start a command-line consumer listening to invalid-messages topic, as follows:

`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic invalid-messages`{{execute T3}} 


