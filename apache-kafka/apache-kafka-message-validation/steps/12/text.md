The Writer class implements the producer interface. The idea is to modify that Writer and build a validation class with minimum effort. The Validator process is as follows:

- Read the Kafka messages from the input-messages topic
- Validate the messages, sending defective messages to the invalid-messages topic
- Write the well-formed messages to valid-messages topic

At the moment, for this example, the definition of a valid message is a message t0 which the following applies:

- It is in JSON format
- It contains the four required fields: event, customer, currency, and timestamp

If these conditions are not met, a new error message in JSON format is generated, sending it to the invalid-messages Kafka topic. The schema of this error message is very simple:

```
{"error": "Failure description" }
```
