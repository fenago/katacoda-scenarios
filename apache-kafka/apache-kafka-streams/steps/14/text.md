Previously, we talked about message processing, but now we will talk about events. An event in this context is something that happens at a particular time. An event is a message that happens at a point in time.

In order to understand events, we have to know the timestamp semantics. An event always has two timestamps, shown as follows:

- **Event time:** The point in time when the event happened at the data source
- **Processing time:** The point in time when the event is processed in the data processor

Due to limitations imposed by the laws of physics, the processing time will always be subsequent to and necessarily different from the event time, for the following reasons: 

- **There is always network latency:** The time to travel from the data source to the Kafka broker cannot be zero.
- **The client could have a cache:** If the client cached some events before, send them to the data processor. As an example, think about a mobile device that is not always connected to the network because there are zones without network access, and the device holds some data before sending it.
- **The existence of back pressure:** Sometimes, the broker will not process the events as they arrive, because it is busy and there are too many.
Having said the previous points, it is always important that our messages have a timestamp. Since version 0.10 of Kafka, the messages stored in Kafka always have an associated timestamp. The timestamp is normally assigned by the producer; if the producer sends a message without a timestamp, the broker assigns it one.

As a professional tip, when generating messages, always assign a timestamp from the producer.