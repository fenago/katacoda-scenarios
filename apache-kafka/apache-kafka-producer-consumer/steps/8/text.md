Kafkacat is a command line utility that you can use to test and debug Apache Kafka® deployments. You can use kafkacat to produce, consume, and list topic and partition information for Kafka.

kafkacat is similar to the Kafka console producer and Kafka console consumer, but more powerful.

To install kafkacat on Linux, type the following:
`apt-get --assume-yes install kafkacat`{{execute}} 

#### Publish
To publish message to amazingTopic, run the following:
`kafkacat -P -b localhost -t amazingTopic`{{execute}} 

Type following message and press enter in the above prompt `Hello kafkacat!`{{copy}} 

**Note** Press `Ctrl + C` after sending the message to quit above prompt.

#### Subscribe
To subscribe to amazingTopic and print to stdout, type the following:
`kafkacat -C -b localhost -t amazingTopic`{{execute}} 