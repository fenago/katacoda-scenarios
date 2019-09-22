Now that we have our project skeleton, let's recall the project requirements for the stream processing engine. Remember that our event customer consults ETH price occurs outside Monedero and that these messages may not be well formed, that is, they may have defects. The first step in our pipeline is to validate that the input events have the correct data and the correct structure. Our project will be called ProcessingEngine.

The `ProcessingEngine` specification shall create a pipeline application that does the following:

- Reads each message from a Kafka topic called input-messages
- Validates each message, sending any invalid event to a specific Kafka topic called invalid-messages
- Writes the correct messages in a Kafka topic called valid-messages

These steps are detailed below, the first sketch for the pipeline processing engine:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-message-validation/steps/3/1.png)
	
The processing engine reads events from the input-messages topic, validates the messages, and routes the defective ones to invalid-messages topic and the correct ones to valid-messages topic.

The processing engine stream construction has two phases:

- Create a simple Kafka worker that reads from the input-messages topic in Kafka and writes the events to another topic
- Modify the Kafka worker to make the validation