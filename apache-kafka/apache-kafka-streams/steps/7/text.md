
To scale out the architecture as promised, we must follow these steps:

Run a console consumer in **terminal 4** for the uptimes topic, shown as follows:
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic uptimes --property print.key=true`{{execute T4}} 


Run the application jar in **terminal 5** from the command line, shown in the following code:
`cd ~/kafka/Chapter06/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.plain.PlainStreamsProcessor`{{execute T5}} 

This is when we verify that our application really scales out.

