kafkacat is a generic command-line non-JVM utility used to test and debug Apache Kafka deployments. kafkacat can be used to produce, consume, and list topic and partition information for Kafka. kafkacat is netcat for Kafka, and it is a tool for inspecting and creating data in Kafka.

kafkacat is similar to the Kafka console producer and Kafka console consumer, but more powerful. It is available at https://github.com/edenhill/kafkacat.

To install kafkacat on modern Linux, type the following:

`yes | apt-get install kafkacat`{{execute}}


You can verify kafkacat is installed on your System by running `kafkacat -h`{{execute}} command.

