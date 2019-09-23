kafkacat is similar to the Kafka console producer and Kafka console consumer, but more powerful.

To install kafkacat on Linux, type the following:
`apt-get --assume-yes install kafkacat`{{execute}} 

#### Publish
To publish message to amazingTopic, run the following:
`kafkacat -b localhost:9092 –t amazingTopic -P`{{execute}} 

Type following message  `Hello kafkacat!`{{execute}} 

**Note** Press `Ctrl + C` after sending the message to quit above prompt.

#### Subscribe
To subscribe to amazingTopic and print to stdout, type the following:
`kafkacat -b localhost:9092 –t amazingTopic -C`{{execute}} 