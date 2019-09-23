kafkacat is similar to the Kafka console producer and Kafka console consumer, but more powerful.

To install kafkacat on Linux, type the following:
`apt-get install kafkacat`{{execute}} 

To subscribe to amazingTopic and redundantTopic and print to stdout, type the following:
`kafkacat -b localhost:9092 –t amazingTopic redundantTopic`{{execute}} 