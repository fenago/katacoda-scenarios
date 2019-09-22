
To scale out the architecture as promised, we must follow these steps:

Run a console consumer for the uptimes topic, shown as follows:
Copy
$ ./bin/kafka-console-consumer --bootstrap-server localhost:9092 
--topic uptimes --property print.key=true
Run the application jar from the command line, shown in the following code:
Copy
$ java -cp ./build/libs/kioto-0.1.0.jar 
kioto.plain.PlainStreamsProcessor
This is when we verify that our application really scales out.

